from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.fptpyyx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.fptpyyx.mongodb.net/fanlog?retryWrites=true&w=majority',
                     tlsCAFile=ca)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    nickName_receive = request.form['nickName_give']
    comment_receive = request.form['comment_give']
    doc = {'nickName': nickName_receive, 'comment': comment_receive}
    db.fanlog.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})


@app.route("/homework", methods=["GET"])
def homework_get():
    log_list = list(db.fanlog.find({}, {'_id': False}))
    return jsonify({'fanlist':log_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
