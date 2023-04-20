from flask08_파일업로드 import Flask, url_for
app = Flask(__name__)

user = ''
@app.route("/")
def hello():
	return "Hello Page!"

@app.route('/profile/<username>')
def get_profile(username):
    user = username
    return 'profile : ' + username

@app.route('/message/<int:message_id>')
def get_message(message_id):
    return 'message_id : %d' % message_id

if __name__ == "__main__":
    app.run()
