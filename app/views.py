# -*- coding: utf-8 -*-
from app import app, db, lm
from app.forms import RegistrationForm
from flask import g,request, render_template, Flask, url_for, flash, redirect,session, abort, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from models import User
from app.forms import RegistrationForm, LoginForm
from flask.ext.login import login_user , logout_user , current_user , login_required

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/login_page')
def loginpage():
	form = LoginForm()
	return render_template('login.html',form = form)



#@app.before_request
#def load_user():
    #if session["loged_in"]:
        #user = User.query.filter_by(username=session["username"]).first()
    #else:
        #user = {"username": "Guest"}  # Make it better, use an anonymous User instead

    #g.user = user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/logout')
def logout():
    logout_user()
    session.pop('loged_in', None)
    session.pop('username',None)
    session.pop('password', None)
    return redirect(url_for('index')) 

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	username = request.form['username']
	password = request.form['password']
	registered_user = User.query.filter_by(nickname=username,password=password).first()
	if registered_user is None:
		return render_template('login.html', form=form)
	login_user(registered_user)
	current_user = User.query.get(username)
	session['username'] = username
	session['password'] = password
	session['loged_in'] = True
	#logened = User.is_authenticated()
	#return render_template('index.html',username = username, registered_user = registered_user, current_user = current_user)
	return redirect(url_for('index'))

@app.route('/register',methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	if request.form['password'] == request.form['confirm']:
		user = User(first_last_name = request.form.get('first_last_name'), username = request.form.get('username'), email = request.form.get('email'), password = request.form.get('password'), role = 0)
	else:
		#session['register_error'] = True
		error = u'Неправильный повтор пароля'
		form = RegistrationForm()
		return render_template('register.html', form = form, error = error)
	db.session.add(user)
	db.session.commit()
	username = request.form.get('username')
	password = request.form.get('password')
	session['username'] = username
	session['password'] = password
	session['loged_in'] = True
	session['registretion_error'] = None
	
	name = request.form.get('first_last_name')
	return render_template('index.html')


@app.route('/register_page')
def registerpage():
	form = RegistrationForm()
	return render_template('register.html',form = form)
