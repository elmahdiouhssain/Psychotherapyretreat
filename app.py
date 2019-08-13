from psyco import app
import os
#from surf.database import db_session
from flask import Flask, session, g, render_template
from datetime import datetime

from flask_security import Security, login_user, current_user
from psyco.database import User, Contact, Blog, db_session



from psyco.views import main
app.register_blueprint(main.main)

from psyco.views import blog
app.register_blueprint(blog.blog)

from psyco.views import panel
app.register_blueprint(panel.panel)

@app.before_request
def before_request():
    g.user = current_user


@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404


#@app.teardown_appcontext
#def shutdown_session(exception=None):
	#db_session.remove()