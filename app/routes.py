from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user

from app import app
from app.forms import LoginForm
from app.models import User


@app.route('/')
# @app.route('/homepage')
# def homepage():
#     return "hello world ! from homepage "

@app.route('/index')

def index():
    user = {'username':'Zhibo Liu'}
    posts =[
        {'author':{'username':'Yilin'},
        'body':'Beautiful day in Portland!'},
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title = 'Home',user = user,posts = posts)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filterby(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('INVALID USERNAME OR PASSWORD !')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
        # flash('Login requested for user {}, remember_me = {}'.format(
        #     form.username.data, form.remember_me.data
        # ))
        return redirect(url_for('index'))
    return render_template('login.html',title = 'Sign In',form = form)


