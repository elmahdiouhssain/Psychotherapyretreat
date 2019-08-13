# -*- coding: utf-8 -*-
from flask import Blueprint, abort, flash, g, jsonify, redirect, \
	render_template, request, url_for
from datetime import datetime
#from flask_website.utils import format_creole, request_wants_json, \
	#requires_admin, requires_login
from psyco.database import db_session, User, Role, Contact, Blog
from psyco.form import Addpost, ContactForm, Signin
from flask_security import login_required, login_user, current_user, logout_user, roles_required

from sqlalchemy.orm import subqueryload

from sqlalchemy import desc, func


panel = Blueprint('panel', __name__, url_prefix='/panel')

@panel.route('/administrator/authentication', methods=['GET', 'POST'])
#@login_required
#@roles_required('superadmin')
def log():

	form = Signin()

	return render_template('security/login.html', form=form, title='Login First')

@panel.route('/logout')
@login_required
def logout():
	logout_user()
	flash("You are now loggin out !!", 'success')
	return redirect(url_for('main.index'))



@panel.route('/administrator/', methods=['GET', 'POST'])
#@login_required
#@roles_required('superadmin')
def index():

	#contacts = Contact.query.order_by(func.count(Contact.id)).scalar()

	#blogs = Blog.query.order_by(desc(Blog.id)).limit(5)


	return render_template('panel/index.html', title='Panel Area')

######################################################################################################################


@panel.route('/messages/', methods=['GET', 'POST'])
#@login_required
#@roles_required('superadmin')
def message():

	contacts = Contact.query.order_by(desc(Contact.id)).limit(5)



	return render_template('panel/messages.html', contacts=contacts, title='Massages')


@panel.route('xpxR/messages/show/<id_slug:contact_id>', methods=['GET', 'POST'])
def showmsg(contact_id):

	#checkouts = Checkout.query.all()
	#checkouts = Checkout.query.order_by(desc(Checkout.id)).limit(5)

	contacts = Contact.query.filter_by(id=contact_id).one()

	url_for('panel.showmsg', contact_id=contacts)

	#form = Addpost()

	return render_template('/panel/show_message.html', contacts=contacts, title='Open Message')


@panel.route('xpxR/messages/delete/<int:id>', methods=['GET', 'POST'])
#@login_required
#@roles_required('superadmin')
def delete_msg(id):
	"""
	Delete a department from the database
	"""
	#check_admin()

	contacts = Contact.query.get(id)
	db_session.delete(contacts)
	db_session.commit()
	flash('You have successfully delete Message.', "success")

	# redirect to the departments page
	return redirect(url_for('panel.message'))

	return render_template(title="Delete Message")
########################################### BLOG AREA ###############################################################



@panel.route('/users/', methods=['GET', 'POST'])
#@login_required
#@roles_required('superadmin')
def users():

	users = User.query.order_by(desc(User.id)).limit(5)



	return render_template('panel/users.html', users=users, title='Users')

###########################################################################################################################""


@panel.route('/blog/', methods=['GET', 'POST'])
#@login_required
#@roles_required('superadmin')
def blog():

	blogs = Blog.query.order_by(desc(Blog.id)).limit(5)



	return render_template('panel/blog.html', blogs=blogs, title='Posts')

@panel.route('xpxR/blog/addpost', methods=['GET', 'POST'])
def addpost():

	form = Addpost()
	if form.validate_on_submit():

		blogs = Blog(title=form.title.data,body=form.body.data,img_off=form.img_off.data,tags=form.tags.data,categorie=form.categorie.data)


		db_session.add(blogs)
		db_session.commit()

		flash('Post Added seccussfly ;) .', 'success')

		# redirect to the login page
		return redirect(url_for('panel.addpost'))

	return render_template('/panel/addpost.html', form=form, title='New Post', legend='Add Post')


@panel.route('xpxR/blog/delete/<int:id>', methods=['GET', 'POST'])
#@login_required
#@roles_required('superadmin')
def delete_blog(id):
	"""
	Delete a department from the database
	"""
	#check_admin()

	blogs = Blog.query.get(id)
	db_session.delete(blogs)
	db_session.commit()
	flash('You have successfully delete Post.', "success")

	# redirect to the departments page
	return redirect(url_for('panel.blog'))

	return render_template(title="Delete Post")


@panel.route('xpxR/updatblog/<int:blogs_id>/', methods=['GET', 'POST'])
def updatblog(blogs_id):

	blogs = Blog.query.get(blogs_id)
	form = Addpost()

	if form.validate_on_submit():

		blogs.title = form.title.data
		blogs.img_off = form.img_off.data
		blogs.body = form.body.data
		blogs.tags = form.tags.data
		blogs.categorie = form.categorie.data


		db_session.commit()

		flash('Your Post Has been Updated !', 'success')
		return redirect(url_for('panel.blog', blogs_id=blogs.id))

	elif request.method == 'GET':

		form.title.data = blogs.title
		form.img_off.data = blogs.img_off
		form.body.data = blogs.body
		form.tags.data = blogs.tags
		form.categorie.data = blogs.categorie


	return render_template('/panel/addpost.html', form=form, title='Update Post', legend='Update Post')


#################################################Reservation Area#################################################################

