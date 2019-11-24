from blogapp.app import app
from flask import render_template, flash, redirect
from blogapp.forms import RegForm, LogForm

@app.route('/')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/register')
def register():
    form = RegForm()
    return render_template('register.html', title='Register', form=form)