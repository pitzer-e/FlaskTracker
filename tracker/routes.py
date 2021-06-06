from tracker import app
from flask import render_template, redirect, url_for, flash, request
from tracker.models import *
from tracker.forms import RegisterForm, LoginForm, EnterDataForm
from tracker import db
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, time


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/data', methods=['GET', 'POST'])
@login_required
def data_page():
    data_form = EnterDataForm()
    if request.method == "POST":
        location = request.form.get('Location')
        hour = request.form.get('Hour')
        minute = request.form.get('Min')
        form_date = request.form.get('date')

        date_split = form_date.split('/')
        python_date = date(int(date_split[2]), int(date_split[0]), int(date_split[1]))
        python_time = time(int(hour), int(minute))
        #   create a location
        location_to_create = Location(name=location,
                                      owner=current_user.id,
                                      date=python_date,
                                      time=python_time)

        #   commit to database
        db.session.add(location_to_create)
        db.session.commit()
        flash('Location and date added successfully!', category='success')
        return redirect(url_for('data_page'))

    if request.method == "GET":
        owned_locations = Location.query.filter_by(owner=current_user.id)
        return render_template('data.html', data_form=data_form, owned_locations=owned_locations)


@app.route('/report')
@login_required
def report_page():
    return render_template('report.html')


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin_page():
    admin_form = EnterDataForm()

    #   first check, is the user an admin?
    if current_user.username == 'admin':

        if request.method == "POST":
            form_value = request.form.get('locationVal')
            form_location = request.form.get('Location')

            if admin_form.validate_on_submit():
                location = db.session.query(Location).filter(Location.name == form_location).one()
                location.infection = float(form_value)
                db.session.commit()

                flash(f'Location {form_location} updated successfully!', category='success')
                return redirect(url_for('admin_page'))

            if admin_form.errors != {}:
                for err_msg in admin_form.errors.values():
                    flash(f'There was an error with creating a user: {err_msg}', category='danger')
                return redirect(url_for('admin_page'))

        if request.method == "GET":
            users = User.query.all()
            return render_template('admin.html', admin_form=admin_form, users=users)

    #   if not an admin, give them the boot
    else:
        flash(f'The account {current_user.username} does not have adequate privileges for this page', category='danger')
        return redirect(url_for('home_page'))


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
        login_user(user_to_create)
        flash(f'Account creation successful! You are now logged in as {user_to_create.username}', category='success')

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

            if attempted_user.username == 'admin':
                return redirect(url_for('admin_page'))

            else:
                return redirect(url_for('home_page'))

        else:

            flash('Username and password do not match. Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out!', category='info')
    return redirect(url_for('home_page'))

