from flask import Flask,render_template,request,redirect,url_for,flash
#from src.models import usersModel
from src import app


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        return render_template ("login.html")
    else:
         return render_template ("login.html")
