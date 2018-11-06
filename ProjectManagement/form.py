from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from wtforms.fields.html5 import DateField
from datetime import datetime
from datetime import date

from ProjectManagement.models import User


def calculate_duration(dt):
    birth = datetime.strptime(dt, '%Y-%m-%d')
    today = date.today()
    print(float(today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))), )
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))


class SignupForm(FlaskForm):
    first_name = StringField("First Name", [DataRequired(message='Kindly input your first name'),
                                            Length(min=4, max=20, message="Invalid length (4-20)")])
    surname = StringField("Surname", [DataRequired(message="Kindly input your last name"),
                                      Length(min=4, max=20, message="Invalid length (4-20)")])
    email = StringField("Email", [DataRequired(message="Kindly input your Email Address"),
                                  Email(message="Invalid Email Address, missing '@' symbol"),
                                  Length(max=50, message="Invalid length (more than 50)")])
    password = PasswordField("Password", [DataRequired(message="Input Password"),
                                          Length(min=8, message="Password too short > 8"),
                                          EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField("Repeat Password", [DataRequired(message="Confirm Password"),
                                                         EqualTo('password', message='Passwords must match')])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email address already exists')

    def validate_first_name(self, first_name):
        if not str(first_name):
            raise ValidationError('No special characters eg.(@, #, [space]) allowed, only letters')

    def validate_surname(self, surname):
        if not str(surname):
            raise ValidationError('No special characters eg.(@, #, [space]) allowed, only letters')

    def validate_duration(self, dob):
        form = ProjectForm()
        if calculate_duration(str(form.dob.data)) < 18:
            raise ValidationError('Invalid date of birth, age is less than 18 years')
        if calculate_duration(str(form.dob.data)) > 120:
            raise ValidationError('Invalid date of birth, age more than 120 years')


class LoginForm(FlaskForm):
    email = StringField("Email", [DataRequired(message="Email Address required"),
                                  Email(message="Invalid Email Address, missing '@' symbol")])
    password = PasswordField("Password", [DataRequired(message="Password required")])
    remember = BooleanField("Remember me")


class ProjectForm(FlaskForm):
    project_name = StringField("Project Name", [DataRequired(message="Kindly input your project name")])
    start_date = DateField("Start Date", [DataRequired(message="Kindly input your start date")])
    end_date = DateField("End Date", [DataRequired(message="Kindly input your end date")])
    team_no = IntegerField("Team No", [DataRequired(message="Kindly input your team no")])
    project_type = StringField("Project Type", [DataRequired(message="Kindly input your project type")])
    organization = StringField("Organization", [DataRequired(message="Kindly input your organization")])


class UpdateForm(FlaskForm):
    project_name = StringField("Project Name", [DataRequired(message="Kindly input your project name")])
    start_date = DateField("Start Date", [DataRequired(message="Kindly input your start date")])
    end_date = DateField("End Date", [DataRequired(message="Kindly input your end date")])
    team_no = IntegerField("Team No", [DataRequired(message="Kindly input your team no")])
    project_type = StringField("Project Type", [DataRequired(message="Kindly input your project type")])
    organization = StringField("Organization", [DataRequired(message="Kindly input your organization")])
    status = SelectField("Progress", [DataRequired(message="Kindly input your organization")],
                         choices=[('Pending', 'Pending'), ('Complete', 'Complete'), ('Incomplete', 'Incomplete')])
