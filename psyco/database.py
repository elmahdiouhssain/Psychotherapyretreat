from datetime import datetime
from sqlalchemy import create_engine, Column, TEXT, Integer, String, Boolean, DateTime, \
	 ForeignKey, event

from flask import flash, g, jsonify

from sqlalchemy.orm import scoped_session, sessionmaker, backref, relationship
from sqlalchemy.ext.declarative import declarative_base

from flask import url_for, Markup

from flask_security import UserMixin, RoleMixin, SQLAlchemySessionUserDatastore, Security
from werkzeug.security import generate_password_hash, check_password_hash

#from mysql.connector import (connection)
import os
from flask_login import LoginManager
import pymysql

login_manager = LoginManager()



#DATABASE_CONNECT_OPTIONS = {}
#cnx = connection.MySQLConnection()

#dba = mysql+mysqlconnector://acomplexbc:acomplexbc@127.0.0.1:3306/acomplexbc

engine = create_engine('mysql+pymysql://psyco4:psyco4@localhost/psyco4?charset=utf8mb4&binary_prefix=true')

#mysql+pymysql://acomplexbc:acomplexbc@localhost/acomplexbc?charset=utf8mb4&binary_prefix=true

db_session = scoped_session(sessionmaker(autocommit=False,
										 autoflush=False,
										 bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	Model.metadata.create_all(bind=engine)


Model = declarative_base(name='Model')
Model.query = db_session.query_property()

#Stop the connection to db
#cnx.close()

class RolesUsers(Base):

	__tablename__ = 'roles_users'
	id = Column(Integer(), primary_key=True)
	user_id = Column('users_id', Integer(), ForeignKey('users.id'))
	role_id = Column('role_id', Integer(), ForeignKey('role.id'))

class Role(Base, RoleMixin):

	__tablename__ = 'role'
	id = Column(Integer(), primary_key=True)
	name = Column(String(80), unique=True)
	description = Column(String(255))

	def __init__(self, name, description):
		super(Role, self).__init__()
		self.name = name
		self.description = description

class User(Base, UserMixin):

	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	email = Column(String(255), unique=True)
	username = Column(String(255))
	password_hash = Column(String(255))
	social_id = Column(String(64))
	last_login_ip = Column(String(100))
	current_login_ip = Column(String(100))
	#bio = Column(String(255))

	roles = relationship('Role', secondary='roles_users',
backref=backref('users', lazy='dynamic'))

	posts = relationship('Blog', backref='user', lazy='dynamic')

	tokens = Column(TEXT)
	created_at = Column(DateTime, default=datetime.utcnow())

	

	@property
	def password(self):
		"""
		Prevent pasword from being accessed
		"""
		raise AttributeError('password is not a readable attribute.')

	@password.setter
	def password(self, password):
		"""
		Set password to a hashed password
		"""
		#pepper = os.environ.get('SECRET_SALT')
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		"""
		Check if hashed password matches actual password
		"""
		#pepper = os.environ.get('SECRET_SALT')
		return check_password_hash(self.password_hash, password)

	def __init__(self, email, username, password):
		super(User, self).__init__()
		self.email = email
		self.username = username
		self.password = password



	def is_authenticated(self):
		return True
 
	def is_active(self):
		return True
 
	def is_anonymous(self):
		return False

	def get_id(self):
		
		return str(self.id)  # python 3

 
	def __repr__(self):
		return '<User %r>' % (self.username)


class Contact(Base, UserMixin):

	__tablename__ = 'contacts'

	id = Column(Integer, primary_key=True)
	name = Column(String(60), index=True)
	mail = Column(String(60), index=True)

	msg = Column(String(500), index=True)
	msg_time = Column(DateTime, default=datetime.utcnow())

	def __init__(self, name, mail, msg):
		super(Contact, self).__init__()
		self.name = name
		self.mail = mail
	
		self.msg = msg

class Blog(Base, UserMixin):

	__tablename__ = 'blogs'

	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	img_off = Column(String(255), nullable=False)
	body = Column(TEXT, nullable=False)
	tags = Column(String(100), nullable=False)
	categorie = Column(String(255))
	
	posted_on = Column(DateTime, default=datetime.utcnow())

	user_id = Column(Integer, ForeignKey('users.id'))

	def __init__(self, title, img_off, body, tags, categorie):
		super(Blog, self).__init__()
		self.title = title
		self.img_off = img_off
		self.body = body
		self.tags = tags
		self.categorie = categorie
		
		#self.posted_on = posted_on

#datetime.utcnow().strftime('%B %d %Y - %H:%M:%S')

