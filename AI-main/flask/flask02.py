from flask08_파일업로드 import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('input.html')

if __name__ == "__main__":
		app.run()