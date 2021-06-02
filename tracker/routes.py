from tracker import app
from flask import render_template, redirect, url_for, flash
from tracker.models import User
from tracker.forms import RegisterForm, LoginForm
from tracker import db
from flask_login import login_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/data')
def data_page():
    return render_template('data.html')


@app.route('/report')
def report_page():
    return render_template('report.html')


@app.route('/admin')
def admin_page():
    users = User.query.all()
    return render_template('admin.html', users=users)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              first=form.first.data,
                              last=form.last.data,
                              password=form.password_1.data)

        db.session.add(user_to_create)
        db.session.commit()

        return redirect(url_for('home_page'))

    #   if there are no errors from the validations
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password(
                attempted_password=form.password.data):

            login_user(attempted_user)
            flash(f'Login success: You are logged in as: {attempted_user.username}', category='success')

            return redirect(url_for('home_page'))

        else:

            flash('Username and password do not match. Please try again', category='danger')

    return render_template('login.html', form=form)
