import random
import requests
from datetime import datetime
from flask import Flask, render_template
my_name = "".capitalize()
app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.now().year
    random_number = random.randint(0,10)
    return render_template("index.html", number=random_number, year=current_year)

# CHALLENGE: try to write a code that will auto generate age and gender using flask
# @app.route('/guess/<my_name>')
# def guess(my_name):
#     myage = requests.get(url=f"https://api.agify.io?name={my_name}").json()["age"]
#     mygender = requests.get(url=f"https://api.genderize.io?name={my_name}").json()["gender"]
#     return render_template("index.html",age=myage, gender=mygender, name=my_name)

# CHALLENGE 2: Create a blog post using jinja
@app.route('/blog')
def myblog():
    response = requests.get(url="https://api.npoint.io/4226d56e6f2454c5aa7c").json()
    return render_template("index.html", post=response)


# We will talk about URL BUILDING. this is how we can create a link that can redirect to our other page
# we go to our html file, build an ankar tag and assign "url_for(the function that you want a url for)

if __name__ == "__main__":
    app.run(debug=True)