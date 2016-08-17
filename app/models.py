from app import db
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required


ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_last_name = db.Column(db.String(64), unique = False)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.Integer, default = ROLE_USER) 
    def __repr__(self):
        return '<User %r>' % (self.nickname)
    def __init__(self , username ,password , email,role,first_last_name):
        self.first_last_name = first_last_name
        self.nickname = username
        self.password = password
        self.email = email
        self.role = role

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_publication = db.Column(db.DateTime)
    def __repr__(self):
        return '<Post %r>' % (self.test)