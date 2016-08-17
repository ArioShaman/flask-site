# -*- coding: utf-8 -*-
from flask import Flask
import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask.ext.login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))



app = Flask(__name__)
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
#app.config['DEBUG'] = True
#app.config['SECRET_KEY'] = 'super-secret'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' + os.path.join(basedir, 'app.db')
#app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(basedir, 'db_repository')

#app.config['MAIL_SERVER'] = 'smtp.example.com'
#app.config['MAIL_PORT'] = 465
#app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_USERNAME'] = 'username'
#app.config['MAIL_PASSWORD'] = 'password'
app.config.from_object('config')
mail = Mail(app)



from app import views, models