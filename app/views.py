# -*- coding: utf-8 -*-
from app import app
from flask import request, render_template
from flask import Flask, url_for

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/login')
def loginpage():
	return render_template('login.html')


@app.route('/register')
def register():
	return render_template('register.html')


@app.route('/user/<username>')
def show_user_profile(username):
	# показать профиль данного пользователя
	return 'User %s' % username
@app.route('/post/<int:post_id>')
def show_post(post_id):
	# вывести сообщение с данными
	return 'Post %d' % post_id
