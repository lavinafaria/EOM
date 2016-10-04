from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
	print ("test")

	if _name_ == "__main__":
		app.run(debug = True)