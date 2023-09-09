import datetime

from py3dbp import Packer, Bin, Item
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import matplotlib as mpl
mpl.use('Agg') # 메인스레드에서 matplotlib 실행 안할 경우
import matplotlib.pyplot as plt
import time
import random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)




@app.route('/', methods=['POST'])
def run_simulation():
    data = request.get_json()  # 요청 데이터를 JSON 형태로 받음
    containers = data['containers']
    items = data['items']
    # 랜덤한 이미지 이름과 컨테이너 이름 생성
    img_name = generate_random_string(10)
    container_name = generate_random_string(10)

    # simulation 함수 실행
    total_count, unloadable_count, loaded_weight,execution_date = simulation(containers, items, img_name)

    formatted_date = execution_date.strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({
        "container_name":container_name,
        "total_count": total_count,
        "unloadable_count": unloadable_count,
        "loaded_weight": loaded_weight,
        "image": img_name,
        "execution_date": formatted_date
    })

def generate_random_string(length):
    # string.ascii_letters는 모든 대소문자 알파벳을 포함합니다.
    # string.digits는 0부터 9까지의 숫자를 포함합니다.
    letters_and_digits = string.ascii_letters + string.digits

    # 지정된 길이만큼의 랜덤한 문자열을 반환합니다.
    return ''.join(random.choice(letters_and_digits) for _ in range(length))
def simulation(containers,items,img_name):
    # 현재 날짜와 시간 가져오기
    execution_date = datetime.datetime.now()
    total_count = 0 # 총 물류 수
    unloadable_count = 0 # 적재 불가 물류 수
    loaded_weight = 0 # 적재 물류 무게



    colorList = ["crimson", "limegreen", "g", "r", "c", "m", "y", "k"]
    # 3D화
    def cuboid_data2(o, size=(1, 1, 1)):
        X = [[[0, 1, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]],
            [[0, 0, 0], [0, 0, 1], [1, 0, 1], [1, 0, 0]],
            [[1, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]],
            [[0, 0, 1], [0, 0, 0], [0, 1, 0], [0, 1, 1]],
            [[0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0]],
            [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]]
        X = np.array(X).astype(float)
        for i in range(3):
            X[:, :, i] *= size[i]
        X += np.array(o)
        return X


    def plotCubeAt2(positions, sizes=None, colors=None, **kwargs):
        if not isinstance(colors, (list, np.ndarray)): colors = ["C0"] * len(positions)
        if not isinstance(sizes, (list, np.ndarray)): sizes = [(1, 1, 1)] * len(positions)
        g = []
        for p, s, c in zip(positions, sizes, colors):
            g.append(cuboid_data2(p, size=s))
        return Poly3DCollection(np.concatenate(g),
                                facecolors=np.repeat(colors, 6), **kwargs)


    # 컨테이너 적재
    for t in range(len(containers)):
        packer = Packer()

        truckX = containers[t][0]
        truckY = containers[t][1]
        truckZ = containers[t][2]

        #무게 제약 -> 4번째 요소
        packer.add_bin(Bin('LB', truckX, truckY, truckZ, 10000.0))

        # 물류 등록 - (물류 이름, 가로, 세로, 높이, 무게) * 수량
        for i in range(len(items)):
            # 물류의 수량 만큼 곱해주기기
            each_items_cnt = int(items[i][5])
            total_count += each_items_cnt # 총 물류 수 구하기
            # 물류의 수량이 0이면 안됨^^
            if each_items_cnt > 0:
                for _ in range(each_items_cnt):
                    packer.add_item(Item(items[i][0], items[i][1], items[i][2], items[i][3], items[i][4]))

        # packer.pack()
        packer.pack(bigger_first=False)  # 큰 것 우선

        positions = []
        sizes = []
        colors = []

        for b in packer.bins:
            print(":::::::::::", b.string())

            print("FITTED ITEMS:")
            # 적합한 물류는 list 만들어주기기
            fitted_list = []
            for item in b.items:
                print("====> ", item.string())
                x = float(item.position[0])
                y = float(item.position[1])
                z = float(item.position[2])
                positions.append((x, y, z))
                sizes.append(
                    (float(item.get_dimension()[0]), float(item.get_dimension()[1]), float(item.get_dimension()[2])))

                # 적합한 물류는 적재하고 item list에서 빼주기
                # print("적합 물류 정보 : ", item.name)
                fitted_list.append(item.name)
                loaded_weight += item.weight # 적재된 물류 무게
            print(fitted_list)
            fitted_rows = [i for i, item in enumerate(items) if item[0] in fitted_list]

            print("UNFITTED ITEMS:")
            for item in b.unfitted_items:
                print("====> ", item.string())
                unloadable_count += 1 # 적재 불가 물류 수

            print("***************************************************")
            print("***************************************************")

            # 적합한 물류들은 items에서 삭제해줌으로서 이미 컨테이너에 적재된 물류들은 물류 정보에서 제거
            for index in sorted(fitted_rows, reverse=True):
                del items[index]

        # 색깔 선정
        for i in range(len(b.items)):
            f = random.randint(0, 7)
            colors.append(colorList[f])

        # print(colors)

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.set_aspect('auto')

        pc = plotCubeAt2(positions, sizes, colors=colors, edgecolor="k")
        ax.add_collection3d(pc)

        ax.set_xlim([0, truckX])
        ax.set_ylim([0, truckY])
        ax.set_zlim([0, truckZ])

        time.sleep(10)
        plt.savefig("./share/static/images/"+ img_name + ".png")
        #plt.savefig("./result.png")
        #plt.savefig(img_name+".png")

        return total_count,unloadable_count,loaded_weight,execution_date