from app import app
from flask import render_template

from app.form import RegistrationForm




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    Registration= RegistrationForm()

    
    return render_template('form.html, Registration=RegistrationForm')
       

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('success.html')

@app.route('/profile', methods=['GET','POST'])
def profile():
    return 