from flask08_파일업로드 import Flask
from flask08_파일업로드 import request

app = Flask(__name__)


@app.route('/')
def user_juso():
    temp = request.args.get('name', "user01")
    temp1 = request.args.get('juso', "평택시")

    return temp + "-" + temp1


if __name__ == "__main__":
    app.run()