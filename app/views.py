# -*- coding: utf-8 -*-
from app import app, db, lm
from app.forms import RegistrationForm
from flask import g,request, render_template, Flask, url_for, flash, redirect,session, abort, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from models import User
from app.forms import RegistrationForm, LoginForm
from flask.ext.login import login_user , logout_user , current_user , login_required
import re
from passlib.hash import sha256_crypt


def valid_name_password(self):
	data = re.findall(r'\W',self)
	if len(data) > 0:
		return True
	else:
		return None

def valid_name(stroke):
    final = []
    L = []
    print len(stroke)
    for n in xrange(len(stroke)):
        r = stroke[n]
        L.append(r)
    print L, len(L)

        
    for i in L:
        
        st = re.findall(r'[a-zA-Z]',i)
        if st:
            final.append(st[0])
        mt = re.findall(r'\s',i)
        if mt:
            final.append(mt[0])
            
    print final,'final'
            
    if len(final) == len(L):
        return True
    else:
        return None

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/login_page')
def loginpage():
	form = LoginForm()
	return render_template('login.html',form = form)

@app.route('/register_page')
def registerpage():
	form = RegistrationForm()
	return render_template('register.html',form = form)


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
		form = LoginForm()
		return render_template('login.html',form = form)
	username = request.form['username']
	password = request.form['password']
	auth_user = User.query.filter_by(username=username).first()
	if auth_user is None:
		form = LoginForm()
		error = [u'Введите правильно имя пользователя или пароль',hash_pass]
		return render_template('login.html', form=form, error = error)
	if User.check_password(auth_user,password) is None:
		form = LoginForm()
		error = [u'Введите правильно имя пользователя или пароль',hash_pass]
		return render_template('login.html', form=form, error = error)

	login_user(auth_user)
	current_user = User.query.get(username)
	session['username'] = username
	#session['password'] = password
	session['loged_in'] = True
	#logened = User.is_authenticated()
	#return render_template('index.html',username = username, registered_user = registered_user, current_user = current_user)
	return redirect(url_for('index'))

@app.route('/register',methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	name = request.form.get('first_last_name')
	username = request.form.get('username')
	password = request.form.get('password')
	user = User.query.filter_by(username=username).first()
	if user:
		error = u'Пользователь с таким username уже существует'
		form = RegistrationForm()
		return render_template('register.html', form = form, error = error)
	
	if not valid_name(name):
		error = u'Придумаете имя и фамилию состоящию только из латинских букв'
		form = RegistrationForm()
		return render_template('register.html', form = form, error = error)



	if valid_name_password(username):
		error = u'Никнейм должен состоять только из букв латиницы и цифр'
		form = RegistrationForm()
		return render_template('register.html', form = form, error = error)
	


	if valid_name_password(password):
		error = u'Пароль должен состоять только из букв латиницы и цифр'
		form = RegistrationForm()
		return render_template('register.html',form = form, error = error)
			
	if request.form['password'] == request.form['confirm']:
		#hash_pass = sha256_crypt.encrypt(password)
		hash_pass = User.hash_password(password)
		user = User(first_last_name =  request.form.get('first_last_name'), username = request.form.get('username'), email = request.form.get('email'), password = hash_pass, role = 0)
	else:
		session['register_error'] = True
		error = u'Неправильный повтор пароля'
		form = RegistrationForm()
		return render_template('register.html', form = form, error = error)
	db.session.add(user)
	db.session.commit()
	session['username'] = username
	session['loged_in'] = True
	session['registretion_error'] = None
	
	
	return render_template('index.html')


@app.route('/user/<username>')
@login_required
def user(username):
	user = User.query.filter_by(username = username).first()
	if user == None:
		error = 'Пользователь не найден'
		return render_template('login_error.html', error = error)
	sigin_user = User.query.filter_by(username = session['username']).first()
	if sigin_user.getrole() == 0:
		return render_template('user_profile.html')
	if sigin_user.getrole() == 1:
		return render_template('admin_profile.html')
	