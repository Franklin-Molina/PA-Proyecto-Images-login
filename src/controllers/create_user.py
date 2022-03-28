from flask import Flask,render_template,request,redirect,url_for,flash
#from models import usersModel
from src import app

@app.route("/", methods=['GET'])
def index():
        return render_template ("index.html")
