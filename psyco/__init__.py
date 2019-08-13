from datetime import datetime, timedelta
from flask import Flask, g, session, render_template, make_response
from flask_bootstrap import Bootstrap
from flask_wtf.recaptcha import RecaptchaField
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore, login_user, current_user, logout_user, login_required
from psyco.database import User, Role, Contact, Blog, db_session, init_db
from psyco.form import RegistrationForm, Signin, ContactForm, Addpost
#from urhdiptv import utils
from flask_login import LoginManager, AnonymousUserMixin


from inflection import parameterize
from werkzeug.routing import BaseConverter



# db variable initialization
db = SQLAlchemy()

#ckeditor = CKEditor()

app = Flask(__name__)

#ckeditor = CKEditor(app)

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session,
										User, Role)
security = Security(app, user_datastore)
# Set config values for Flask-Security.
# We're using PBKDF2 with salt.
app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
app.config['SECURITY_PASSWORD_SALT'] = 'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
app.config['SECURITY_REGISTERABLE'] = True	
app.config['SECURITY_TRACKABLE'] = True
app.config['SECURITY_LOGIN_URL'] = 'security/login.html',
#app.config['SECURITY_REGISTER_URL'] = 'security/register_user.html',
app.config['SECURITY_LOGOUT_URL'] = 'panel/logout',
app.config['SECRET_KEY'] = 'b951cbe3a050f545c7d576d51312bb3eef39100f64ba5c718'
app.config['WTF_CSRF_SECRET_KEY'] = 'b951cbe3a0sdhjkjklsj98lks50f545c7d576d51312bb3eef39100f64ba5c718'

bootstrap = Bootstrap(app)
db.init_app(app)


#Login manager configurations
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'panel.log'
#login_manager.session_protection = "strong"

#Login manager configurations
login_manager = LoginManager()
login_manager.init_app(app)

#login_manager.login_view = 'areaclients.index'
#login_manager.session_protection = "strong"

app.url_map.strict_slashes = False



# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    try:
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=(datetime.now() - timedelta(days=7)).date().isoformat()
      # static pages
      for rule in app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0:
              pages.append(
                           ["https://PSYCOTHERAPYRETREAT.com"+str(rule.rule),ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"    
    
      return response
    except Exception as e:
        return(str(e))   

## LIVE VERSION ####
@app.route('/robots.txt/')
def robots():
    return("User-agent: *\nDisallow: /signup/\nDisallow: /signin/\nDisallow: /panel/")

class IDSlugConverter(BaseConverter):
    """Matches an int id and optional slug, separated by "/".

    :param attr: name of field to slugify, or None for default of str(instance)
    :param length: max length of slug when building url
    """

    regex = r'-?\d+(?:/[\w\-]*)?'

    def __init__(self, map, attr='title', length=80):
        self.attr = attr
        self.length = int(length)
        super(IDSlugConverter, self).__init__(map)

    def to_python(self, value):
        id, slug = (value.split('/') + [None])[:2]
        return int(id)

    def to_url(self, value):
        raw = str(value) if self.attr is None else getattr(value, self.attr, '')
        slug = parameterize(raw)[:self.length].rstrip('-')
        return '{}/{}'.format(value.id, slug).rstrip('/')



app.url_map.converters['id_slug'] = IDSlugConverter


if __name__ == '__main__':
	#app.run()
  app.run(host='0.0.0.0', debug=True)