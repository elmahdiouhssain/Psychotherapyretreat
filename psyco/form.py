from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, SelectField, TextAreaField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from psyco.database import User, RolesUsers, Role, Blog, Contact, db_session, init_db



class RegistrationForm(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email()])

	username = StringField('Username', validators=[DataRequired()])

	password = PasswordField('Password', validators=[
										DataRequired(),
										validators.Length(min=4, max=8),
										EqualTo('confirm_password')
										])

	confirm_password = PasswordField('Confirm Password')

	recaptcha = RecaptchaField()

	submit = SubmitField('Register')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email.')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')


class Signin(FlaskForm):

	email = StringField('Email Address', validators=[DataRequired(), Email()])

	password = PasswordField('Password', validators=[DataRequired(), validators.Length(min=4, max=8)])

	rem = BooleanField('Member Me', default=False)

	submit = SubmitField('Send')


class ContactForm(FlaskForm):

	name = StringField('Name', validators=[DataRequired()])

	mail = StringField('Email Address', validators=[DataRequired(), Email()])

	msg = TextAreaField('Message', validators=[DataRequired()])

	recaptcha = RecaptchaField()

	submit = SubmitField('Send')



class Addpost(FlaskForm):

	title = StringField('Title', validators=[DataRequired()])

	body = TextAreaField('Description', validators=[DataRequired()])

	tags = StringField('Tags', validators=[DataRequired()])

	img_off = StringField('Official Image', validators=[DataRequired()])

	categorie = SelectField('Categorie', choices=[('TREATMENTS', 'TREATMENTS'), ('ANXIETY AND STRESS', 'ANXIETY AND STRESS'), ('DEPRESSION', 'DEPRESSION'), ('ADHD / ADD', 'ADHD / ADD'), ('ADOPTION / GUARDIANSHIP', 'ADOPTION / GUARDIANSHIP'), ('INFOGRAPHICS', 'INFOGRAPHICS'), ('ANXIETY AND STRESS', 'ANXIETY AND STRESS'), ('CHILD ANXIETY', 'CHILD ANXIETY'), ('MISCELLANEOUS', 'MISCELLANEOUS')])

	submit = SubmitField('Send')