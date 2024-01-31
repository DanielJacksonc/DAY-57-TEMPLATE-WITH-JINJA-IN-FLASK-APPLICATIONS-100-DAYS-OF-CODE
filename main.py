from flask import Flask, render_template
import requests

posts = requests.get(url="https://api.npoint.io/4226d56e6f2454c5aa7c").json()

app = Flask(__name__)

@app.route('/')
def home():

    return render_template("index.html", all_post=posts)

@app.route('/post/<int:id>')
def read(id):

    return render_template("post.html", num=id, all_post=posts)


if __name__ == "__main__":
    app.run(debug=True)
