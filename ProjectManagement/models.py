from flask_login import UserMixin
from ProjectManagement import db, login_manager


@login_manager.user_loader
def get_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, first_name, surname, email, password):
        self.first_name = first_name
        self.surname = surname
        self.email = email
        self.password = password


class Projects(db.Model):
    __tablename__ = 'Projects'

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String)
    email = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    team_no = db.Column(db.String)
    project_type = db.Column(db.String)
    organization = db.Column(db.String)
    status = db.Column(db.String, default="Incomplete")
    active = db.Column(db.Boolean, default=True)

    def __init__(self, project_name, start_date, end_date, team_no, project_type, organization):
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.team_no = team_no
        self.project_type = project_type
        self.organization = organization
