from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!12'


@app.route('/submit', methods=['POST'])
def submit():
    if request.form:
        # 使用request.form来获取x-www-form-urlencoded数据
        name = request.form['name']
        email = request.form['email']
        # 处理数据...
        return 'Received data: name=%s, email=%s' % (name, email)
    else:
        return 'No data received', 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
