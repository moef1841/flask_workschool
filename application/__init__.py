#!/usr/bin/python
from flask import Flask, render_template, request, Response, json, flash, redirect
from config import Config
from flask_mongoengine import MongoEngine
from application.forms import LoginForm, RegisterForm



app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)


courseData = [
    {"courseID": "1111", "title": "PHP 101", "description": "Intro to PHP", "credits": 3, "term": "Fall, Spring"},
    {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": 4, "term": "Spring"},
    {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming", "credits": 3, "term": "Fall"},
    {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": 3, "term": "Fall, Spring"},
    {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": 4, "term": "Fall"}
]


# home page.
@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html", index=True)


# login page.
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("You are successfully logged in!.")
        return redirect("/index")
    return render_template("login.html", login=True, form=form, title="Login:")


# courses offerings page.
@app.route("/course_offerings")
@app.route("/course_offerings/<term>")
def course_offerings(term="Fall 2020"):
    return render_template("course_offerings.html", courseData=courseData, course_offerings=True, term=term)


# register page.
@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html", register=True)


# enrollment page.
@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    id = request.form.get("courseID")
    title = request.form.get("title")
    term = request.form.get("term")
    description = request.form.get("description")
    credits = request.form.get("credits")
    return render_template("enrollment.html", enrollment=True,
                           data={"id": id, "title": title, "term": term, "description": description,
                                 "credits": credits})


# create api.
@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if idx == None:
        json_data = courseData
    else:
        json_data = courseData[int(idx)]

    return Response(json.dumps(json_data), mimetype="application/json")


# create user page.
@app.route("/user")
def user():
    # User(user_id=1, first_name="Mohammed", last_name= "Alrubaye", email="moefareed88@gmail.com", password="abcdefgh").save()
    # User(user_id=2, first_name="Adam", last_name= "Zuhir", email="adamzuhir@gmail.com", password="12345678").save()
    users = User.objects.all()
    return render_template("user.html", users=users)
