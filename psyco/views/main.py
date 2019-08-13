# -*- coding: utf-8 -*-
from flask import Blueprint, abort, flash, g, jsonify, redirect, \
	render_template, request, url_for

from psyco.form import ContactForm 
from psyco.database import Contact, Blog
from sqlalchemy.orm import subqueryload
from sqlalchemy import desc


main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():

	posts = Blog.query.order_by(desc(Blog.id)).limit(3)


	return render_template('/main/index.html', posts=posts, title='Home')


@main.route('/about-us')
def about():


	return render_template('/main/about_us.html', title='About Us')


@main.route('/about-me')
def aboutme():


	return render_template('/main/about_me.html', title='About Me')


@main.route('/contact', methods=['GET', 'POST'])
def contact():

	form = ContactForm()
	if form.validate_on_submit():
		cnt = Contact(name=form.name.data,mail=form.mail.data,msg=form.msg.data)
		session.add(cnt)
		session.commit()
		flash('Thank you, We will replay as soon possible', 'success')

		# redirect to the login page
		return redirect(url_for('main.index'))



	return render_template('/main/contacts.html', form=form, title='Contact Us')

