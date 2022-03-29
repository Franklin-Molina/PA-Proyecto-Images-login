from flask import Flask,render_template,request,redirect,url_for,flash
from src.models import usersModel
from src import app
from werkzeug.security import generate_password_hash,check_password_hash
app.secret_key='15sdf153f525a1d'

import re

        
@app.route("/createuser", methods =['GET','POST'])
def createUser():    
        if request.method ==  'POST':
                name=request.form.get('name')
                email=request.form.get('email')
                password=request.form.get('password')
                encriptar= generate_password_hash(password)                 
                isValid=True

                lenpass =  len(password)
                minuscula = False
                mayuscula= False
                numeros = False
                special = False

                if name == "":
                        flash("Nombre Obligatorio")
                        isValid=False        
                if email == "":
                        flash("Correo Obligatorio")   
                        isValid=False    
                
                if password == "":
                        flash("Contraseña Obligatoria")  
                        isValid=False  
                if lenpass < 8 :                       
                        flash("La contraseña debe tener minimo 8 caracteres")                       
                        isValid=False 
               
                
                for caracter in password:
                        if caracter.islower()== True:
                                minuscula= True
                        if caracter.isupper()== True:
                                mayuscula= True
                        if caracter.isdigit()==True:
                                numeros= True                   
                               
                if minuscula == False:
                        flash("Ingrese al menos una Minuscula a la contraseña")
                if mayuscula == False:
                        flash("Ingrese al menos una Mayusculas a la contraseña")
                if numeros == False:
                        flash("Ingrese al menos un Número a la contraseña")
                
                if re.search('[@_!#$%^&*()<>?/\|}{~:]',password):                        
                        special= True
                       
                if special == False:
                        flash("Ingrese al menos un caracter a la contraseña")

                if isValid==False:
                        return render_template("CreateUser.html",name=name,email=email,password=password)
        
                usersModel.createUser(name=name,email=email,claveEncritada=encriptar)                 
                return redirect(url_for("index"))
        else:
                return render_template ("CreateUser.html")
