from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:jungle@sukyeong.o2xkdoo.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/todo/show', methods=['GET'])
def show_todo():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    todos = list(db.todos.find({},{'_id':False}))

    # 2. articles라는 키 값으로 도서정보 내려주기
    return jsonify({'result':'success', 'todos':todos})

## API 역할을 하는 부분
@app.route('/todo/post', methods=['POST'])
def make_todo():
    todo_receive = request.form['todo_give']
    doc = {
        'todo': todo_receive
    }

    db.todos.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '등록 완료!'})

@app.route('/todo/update', methods=['POST'])
def update_todo():

    return jsonify({'result': 'success', 'msg': '할 일 업데이트 완료!'})

@app.route('/todo/complete', methods=['POST'])
def complete_todo():
    
    return jsonify({'result': 'success', 'msg': '할 일 체크 완료!'})




@app.route('/todo/delete', methods=['POST'])
def delete_todo():
    
    return jsonify({'result': 'success', 'msg': '할 일 삭제 완료!'})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)