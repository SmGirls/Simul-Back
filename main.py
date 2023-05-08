from py3dbp import Packer, Bin, Item
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import matplotlib.pyplot as plt
import random

# Container 가로, 세로, 높이 (나중에 이 값 받아오자... 지금은 일단 임의의 한 규격을 넣어둠)
containers_size = [250, 250, 500]

# 사용자가 사용가능한 컨테이너 수를 지정 (이것도 나중에 값 받아오기 지금은 임의의 숫자 넣어둠)
max_container=5

#컨테이너 리스트 만들기
containers=[]
for x in range(max_container):
  containers.append(containers_size)
  
# 물류 등록 - 물류 이름, 가로, 세로, 높이, 무게,수량
items = [
    ["box1",200,100,50,1000,2],
    ["box2",200,100,50,1000,1],
    ["box3",200,100,50,1000,0],
    ["box4",200,100,50,1000,1],
    ["box5",200,100,50,1000,1],
    ["box6",200,100,50,1000,1],
    ["box7",200,100,50,1000,1]
]
#3D에 필요한 색깔 list
colorList = ["crimson","limegreen","g","r","c","m","y","k"]

#3D화 
def cuboid_data2(o, size=(1,1,1)):
    X = [[[0, 1, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]],
        [[0, 0, 0], [0, 0, 1], [1, 0, 1], [1, 0, 0]],
        [[1, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]],
        [[0, 0, 1], [0, 0, 0], [0, 1, 0], [0, 1, 1]],
        [[0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0]],
        [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]]
    X = np.array(X).astype(float)
    for i in range(3):
        X[:,:,i] *= size[i]
    X += np.array(o)
    return X

def plotCubeAt2(positions,sizes=None,colors=None, **kwargs):
    if not isinstance(colors,(list,np.ndarray)): colors=["C0"]*len(positions)
    if not isinstance(sizes,(list,np.ndarray)): sizes=[(1,1,1)]*len(positions)
    g = []
    for p,s,c in zip(positions,sizes,colors):
        g.append( cuboid_data2(p, size=s) )
    return Poly3DCollection(np.concatenate(g),
                            facecolors=np.repeat(colors,6), **kwargs)

# 컨테이너 적재
for t in range(len(containers)):
    packer = Packer()

    truckX = containers[t][0]
    truckY = containers[t][1]
    truckZ = containers[t][2]

    packer.add_bin(Bin('LB', truckX, truckY, truckZ, 3000.0))

    # 물류 등록 - (물류 이름, 가로, 세로, 높이, 무게) * 수량
    for i in range(len(items)):
        #물류의 수량 만큼 곱해주기
        each_items_cnt=items[i][5]
        #물류의 수량이 0이면 안됨^^
        if each_items_cnt>0:
          for _ in range(each_items_cnt):
            packer.add_item(Item(items[i][0], items[i][1], items[i][2], items[i][3],items[i][4]))
        
        

    #packer.pack()
    packer.pack(bigger_first=False)

    positions = []
    sizes = []
    colors = []


    for b in packer.bins:
        print(":::::::::::", b.string())

        print("FITTED ITEMS:")
        # 적합한 물류는 list 만들어주기기
        fitted_list=[]
        for item in b.items:
            print("====> ", item.string())
            x = float(item.position[0])
            y = float(item.position[1])
            z = float(item.position[2])
            positions.append((x,y,z))
            sizes.append((float(item.get_dimension()[0]), float(item.get_dimension()[1]), float(item.get_dimension()[2])))
          
            # 적합한 물류는 적재하고 item list에서 빼주기
            #print("적합 물류 정보 : ", item.name)
            fitted_list.append(item.name)
        print(fitted_list)
        fitted_rows =[i for i, item in enumerate(items) if item[0] in fitted_list]

        print("UNFITTED ITEMS:")
        for item in b.unfitted_items:
            print("====> ", item.string())
            
        print("***************************************************")
        print("***************************************************")

        if fitted_list is None:
          break
        
        # 적합한 물류들은 items에서 삭제해줌으로서 이미 컨테이너에 적재된 물류들은 물류 정보에서 제거
        for index in sorted(fitted_rows, reverse=True):
            del items[index]
        

    
    #색깔 선정
    for i in range(len(b.items)):
        f = random.randint(0,7)
        colors.append(colorList[f])

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_aspect('auto')

    pc = plotCubeAt2(positions,sizes,colors=colors, edgecolor="k")
    ax.add_collection3d(pc)    

    ax.set_xlim([0,truckX])
    ax.set_ylim([0,truckY])
    ax.set_zlim([0,truckZ])

    plt.show()
    plt.savefig("./image/test"+str(t)+".png")