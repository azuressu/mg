# pymongo 기본코드
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.qtyaim8.mongodb.net/?retryWrites=true&w=majority') # 내 url
db = client.dbsparta

# flask 시작코드
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# URL 별로 함수명이 같거나, route('/') 등의 주소가 같으면 안됨
@app.route('/')
def home () :
    return render_template('index.html')

@app.route('/movie')
def main () :
    return render_template('movie_delete.html')

# GET 요청 API코드
@app.route('/test', methods=['GET'])
def movie_get() :
    movie_data = list(db.movies.find({}, {'_id':False}))
    return jsonify({'result': movie_data})

# POST 요청 API코드
@app.route('/test', methods=['POST'])
def movie_post() :
    title_receive = request.form['title']
    # doc = db.movies.find_one({'title': title_receive})
    db.movies.delete_one({'title': title_receive})
    return jsonify({'msg' : '삭제완료!'})

if __name__ == '__main__':
    app.run("0.0.0.0", port = 5000, debug = True)