from flask import render_template, redirect, url_for, flash, send_from_directory
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import os
from ProjectManagement.models import User, Register
from ProjectManagement import app, db
from ProjectManagement.form import LoginForm, SignupForm, RegisterForm, UpdateForm


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        flash("Already logged in as: " + current_user.email, category='warning')
        return redirect(url_for('dashboard'))
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(first_name=form.first_name.data, surname=form.surname.data, email=form.email.data,
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account creation successful, login to proceed', category='success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("Already logged in as: " + current_user.email, category='warning')
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Welcome and successful login: ' + current_user.email, category='success')
            return redirect(url_for('dashboard'))
        flash('Invalid email or password', category='danger')
        return render_template('welcome.html')
    return render_template('login.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    results = db.session.query(Register).filter_by(email=current_user.email)
    return render_template('dashboard.html', results=results)


@app.route('/project/new', methods=['GET', 'POST'])
@login_required
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        project = Register(project_name=form.project_name.data, start_date=form.start_date.data,
                           end_date=form.end_date.data, team_no=form.team_no.data, project_type=form.project_type.data,
                           organization=form.organization.data)
        project.email = current_user.email
        db.session.add(project)
        db.session.commit()
        flash("Project creation successful", category='success')
        return redirect(url_for('dashboard'))
    return render_template('register.html', form=form)


@app.route('/project/edit/<int:project_id>', methods=['POST', 'GET'])
@login_required
def edit(project_id):
    project = Register.query.filter_by(id=project_id).first()
    form = UpdateForm()
    if form.validate_on_submit():
        name = project.project_name
        project.project_name = form.project_name.data
        project.start_date = form.start_date.data
        project.end_date = form.end_date.data
        project.team_no = form.team_no.data
        project.project_type = form.project_type.data
        project.organization = form.organization.data
        project.status = form.status.data

        db.session.add(project)
        db.session.commit()
        flash("You have successfully edited project: " + name, category='info')
        return redirect(url_for('dashboard'))
    return render_template('edit.html', project_id=project_id, form=form)


@app.route('/project/delete/<int:project_id>')
@login_required
def delete(project_id):
    project = Register.query.filter_by(id=project_id).first()
    name = project.project_name
    db.session.delete(project)
    db.session.commit()
    flash("You have successfully deleted project: " + name, category='danger')
    return redirect(url_for('dashboard'))


@app.route('/reports')
@login_required
def reports():
    pass


@app.route('/statistics')
@login_required
def statistics():
    pass


@app.route('/chats')
@login_required
def chats():
    pass


@app.route('/calendar')
@login_required
def calendar():
    pass


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout successful", category='success')
    return redirect(url_for('welcome'))


@app.route('/favicon.ico')
def fav():
    return send_from_directory(os.path.join(app.root_path, './static/img'), 'favicon.ico')
