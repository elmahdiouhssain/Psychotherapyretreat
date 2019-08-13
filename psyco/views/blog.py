# -*- coding: utf-8 -*-
from flask import Blueprint, abort, flash, g, jsonify, redirect, \
	render_template, request, url_for
from psyco.database import Blog
from sqlalchemy.orm import subqueryload
from sqlalchemy import desc

blog = Blueprint('/blog', __name__, url_prefix='/blog')

@blog.route('/')
def index():


	return render_template('/blog/index.html', title='Blog')


@blog.route('/post/<id_slug:post_id>')
def post(post_id):

	posts = Blog.query.filter_by(id=post_id).one()

	url_for('/blog.post', post_id=posts)


	return render_template('/blog/blog_post.html', posts=posts, title=posts.title)