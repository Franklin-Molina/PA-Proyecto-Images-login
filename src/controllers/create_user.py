from flask import Flask,render_template,request,redirect,url_for,flash
from src.models import usersModel
from src import app
from werkzeug.security import generate_password_hash,check_password_hash
app.secret_key='15sdf153f525a1d'



        
@app.route("/createuser", methods =['GET','POST'])
def createUser():    
        if request.method ==  'POST':
                name=request.form.get('name')
                email=request.form.get('email')
                password=request.form.get('password')
                encriptar= generate_password_hash(password)                 
                isValid=True
                if name == "":
                        flash("Nombre Obligatorio")
                        isValid=False        
                if email == "":
                        flash("Correo Obligatorio")   
                        isValid=False        
                if password == "":
                        flash("Contraseña Obligatoria")  
                        isValid=False  
                if isValid==False:
                        return render_template("CreateUser.html",name=name,email=email,password=password)
        
                usersModel.createUser(name=name,email=email,claveEncritada=encriptar)                 
                return redirect(url_for("index"))
        else:
                return render_template ("CreateUser.html")
