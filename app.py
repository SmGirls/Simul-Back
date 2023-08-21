from flask import Flask, render_template, url_for, request, jsonify
from flask_restx import Resource, Namespace, Api
from flask_cors import CORS
import pandas as pd
import os
import json

# app = Flask(__name__)
app = Flask(__name__,
            static_url_path='',
            static_folder='share/static',
            template_folder='templates')
CORS(app)
struck_list = []
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

# 선택한 물류 보기 
@app.route('/select_list', methods=['GET'])
def view_select_list():
    global select_list
    return jsonify(select_list)

# 물류 정보 중 컨테이너에 적재하고 싶은 물류 선택
@app.route('/select_list', methods=['POST'])
def create_select_list():
    data = request.get_json()    # post로 이런 json 형식으로 넘겨주면 됨 {"selected_product_list": ["box1", "box2"]}
    selected_product_names = data['selected_product_list']
    
    global select_list
    # Create the select_list based on the selected product names
    select_list = [item for item in struck_list if item['productname'] in selected_product_names]
    
    return jsonify(select_list)

# 시뮬레이션한 물류에 대한 컨테이너 적재 이미지 리스트
@app.route('/container_list')
def container_manage():
    return "container_manage"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7000,debug=True)

