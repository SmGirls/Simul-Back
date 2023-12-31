from flask import Flask, render_template, url_for, request, jsonify
from flask_cors import CORS
import pandas as pd
import json
import requests

import visualize_func

# app = Flask(__name__)
app = Flask(__name__,
            static_url_path='',
            static_folder='share/static',
            template_folder='templates')
CORS(app)
struck_list = []
select_list =[]
# @app.route('/')
# def webserver():
#     path = './share/static/images'
#     file_list = os.listdir(path)
#     img_name_list = [file for file in file_list if file.endswith('.png')]  ## 파일명 끝이 .csv인 경우
#     return render_template('index.html', pics=img_name_list, test = img_name_list)
#     #return render_template('index.html', test=img_name_list)

# Main 페이지, 여기서 csv파일 업로드
@app.route('/',methods=['POST'])
def upload_csvlist():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Check if the file is a CSV file
    if file and file.filename.endswith('.csv'):
        df = pd.read_csv(file)
        processed_data = df.to_dict(orient='records')
        # 이 코드를 통해 csv 파일이 struck_list.json 파일명으로 저장됨
        with open('struck_list.json', 'w') as json_file:
            json_file.write(pd.Series(processed_data).to_json(orient='records'))
            struck_list.extend(processed_data)
        return jsonify({'message': 'CSV data processed and saved as JSON.'})
    else:
        return jsonify({'error': 'Invalid file format. Only CSV files are supported.'})

# 물류 정보를 보는 페이지
@app.route('/struck_list')
def show_struck_list():
    return jsonify(struck_list)

# 물류 수량 수정
@app.route('/struck_list/<string:productname>', methods=['PUT'])
def struck_list_put(productname):
    update_data = request.get_json()
    for list in struck_list:
        if list['productname'] == productname:
            list['count'] = update_data['count']
            return jsonify(struck_list)
    return jsonify("Failure! Index Error!")

#물류 삭제 
@app.route('/struck_list/<string:productname>', methods=['DELETE'])
def struck_list_delete(productname):
    for i, list in enumerate(struck_list):
        if list['productname'] == productname:
            struck_list.pop(i)
            return jsonify(struck_list)
    return jsonify("Failure! Index Error!")

# # 선택한 물류 보기 
# @app.route('/select_list', methods=['GET'])
# def view_select_list():
#     global select_list
#     return jsonify(select_list)

# # 물류 정보 중 컨테이너에 적재하고 싶은 물류 선택
# @app.route('/select_list', methods=['POST'])
# def create_select_list():
#     global select_list
    
#     data = request.get_json()    # post로 이런 json 형식으로 넘겨주면 됨 {"selected_product_list": ["box1", "box2"]}
#     selected_product_names = data['selected_product_list']
    
#     # Create the select_list based on the selected product names
#     select_list = [item for item in struck_list if item['productname'] in selected_product_names]
#     print("값:",select_list) # [{'productname': 'box1', 'width': 250, 'depth': 220, 'height': 220, 'weight': 100, 'count': 5}, {'productname': 'box2', 'width': 180, 'depth': 160, 'height': 250, 'weight': 300, 'count': 4}]
#     return jsonify(select_list)

# test 중 ...
@app.route('/simul_test')
def send_req():

    # request 통신
    url = "http://127.0.0.1:7001/"
    response = requests.get(url)

    if response.status_code==200:
        return response.json()
    else:
        return "Error: {}".format(response.status_code)

# 물류 선택 후 시뮬레이션
@app.route('/simulation', methods=['POST'])
def post_simulation():
    global select_list
    select_items_list = []
    
    data = request.get_json()    # post로 이런 json 형식으로 넘겨주면 됨 {"selected_product_list": ["box1", "box2","box3."]}
    selected_product_names = data['selected_product_list']

    # Create the select_list based on the selected product names
    select_list = [item for item in struck_list if item['productname'] in selected_product_names]

    # 컨테이너 사이즈
    containers = [
        [1000, 1000, 1000]
    ]
    # 물류 100개 넣었을 경우
    if len(selected_product_names) == 100:
        all_select_items_lists = slicing_data(select_list)
        # Initialize an empty dictionary to store all responses
        all_responses = {}

        # First request
        data1 = {
            'containers': containers,
            'items': all_select_items_lists[0],
        }
        response1 = requests.post("http://127.0.0.1:7001/", json=data1)
        if response1.status_code == 200:
            all_responses["response_1"] = response1.json()

        # Second request
        data2 = {
            'containers': containers,
            'items': all_select_items_lists[1],
        }
        response2 = requests.post("http://127.0.0.1:7001/", json=data2)
        if response2.status_code == 200:
            all_responses["response_2"] = response2.json()

        # 3 request
        data3 = {
            'containers': containers,
            'items': all_select_items_lists[2],
        }
        response3 = requests.post("http://127.0.0.1:7001/", json=data3)
        if response3.status_code == 200:
            all_responses["response_3"] = response3.json()

        # 4 request
        data4 = {
            'containers': containers,
            'items': all_select_items_lists[3],
        }
        response4 = requests.post("http://127.0.0.1:7001/", json=data4)
        if response4.status_code == 200:
            all_responses["response_4"] = response4.json()


        # 5 request
        data5 = {
            'containers': containers,
            'items': all_select_items_lists[4],
        }
        response5 = requests.post("http://127.0.0.1:7001/", json=data5)
        if response5.status_code == 200:
            all_responses["response_5"] = response5.json()

        # 6 request
        data6 = {
            'containers': containers,
            'items': all_select_items_lists[5],
        }
        response6 = requests.post("http://127.0.0.1:7001/", json=data6)
        if response6.status_code == 200:
            all_responses["response_6"] = response6.json()

        # 7 request
        data7 = {
            'containers': containers,
            'items': all_select_items_lists[6],
        }
        response7 = requests.post("http://127.0.0.1:7001/", json=data7)
        if response7.status_code == 200:
            all_responses["response_7"] = response7.json()

        # 8 request
        data8 = {
            'containers': containers,
            'items': all_select_items_lists[7],
        }
        response8 = requests.post("http://127.0.0.1:7001/", json=data8)
        if response8.status_code == 200:
            all_responses["response_8"] = response8.json()

        # 9 request
        data9 = {
            'containers': containers,
            'items': all_select_items_lists[8],
        }
        response9 = requests.post("http://127.0.0.1:7001/", json=data9)
        if response9.status_code == 200:
            all_responses["response_9"] = response9.json()

        # Tenth request
        data10 = {
            'containers': containers,
            'items': all_select_items_lists[9],
        }
        response10 = requests.post("http://127.0.0.1:7001/", json=data10)
        if response10.status_code == 200:
            all_responses["response_10"] = response10.json()

        # Convert all_responses to a JSON string for storage or display, after you've received and processed every single one of them.
        all_responses_json = json.dumps(all_responses)
        return all_responses_json

    else:
        for item in select_list:
            select_items_list.append([
                item['productname'],
                item['width'],
                item['depth'],
                item['height'],
                item['weight'],
                item['count']
            ])
        # request 통신
        url = "http://127.0.0.1:7001/"
        data = {
            'containers': containers,
            'items': select_items_list,
        }
        response = requests.post(url, json=data)  # POST 요청 보내기

        if response.status_code == 200:
            return response.json()
        else:
            return "Error: {}".format(response.status_code)



    #visualize_func.simulation(containers,select_items_list,img_name)  # Pass the select_list to visualize.py 이부분은ㄹ rest api로 따서 넘겨줘야됨
    #return jsonify(select_items_list)

def slicing_data(select_list):
    # Initialize a list to hold all select_items_lists
    all_select_items_lists = []

    # Loop over select_list in chunks of 10
    for i in range(0, len(select_list), 10):
        # Create a new select_items_list for every chunk of 10 items
        select_items_list = []
        for item in select_list[i:i + 10]:
            select_items_list.append([
                item['productname'],
                item['width'],
                item['depth'],
                item['height'],
                item['weight'],
                item['count']
            ])
        # Add this list to the overall list
        all_select_items_lists.append(select_items_list)

    return all_select_items_lists

# 시뮬레이션한 물류에 대한 컨테이너 적재 이미지 리스트
@app.route('/container_list')
def container_manage():
    return "container_manage"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7000,debug=True)

