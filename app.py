from flask import Flask, render_template, jsonify, request
from redis import Redis
import json

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/posts')
def posts():
    sendMessages = [{ "post": s.decode("utf-8")} for s in redis.lrange("posts", 1, -1)]

    return jsonify(Posts=sendMessages)


@app.route('/add', methods=["POST"])
def add():
    data = json.loads(request.data)
    redis.lpush("posts", data["post"])

    return "200"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
