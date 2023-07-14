from flask import Flask, render_template, url_for
import os
from service import struck_manage
# app = Flask(__name__)
app = Flask(__name__,
            static_url_path='',
            static_folder='share/static',
            template_folder='templates')

@app.route('/')
def webserver():
    path = './share/static/images'
    file_list = os.listdir(path)
    img_name_list = [file for file in file_list if file.endswith('.png')]  ## 파일명 끝이 .csv인 경우
    return render_template('index.html', pics=img_name_list, test = img_name_list)
    #return render_template('index.html', test=img_name_list)

@app.route('/struck_manage')
def struck_manage():
    return struck_manage.struck_list()

@app.route('/container_manage')
def container_manage():
    return "contaienr_manage"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7000)

