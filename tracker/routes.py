from tracker import app
from flask import render_template, redirect, url_for, flash, request
from tracker.models import *
from tracker.forms import RegisterForm, LoginForm, EnterDataForm
from tracker import db
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, time
from tracker.graph import Graph
import report


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


@app.route('/report', methods=['GET', 'POST'])
@login_required
def report_page():
    report_form = EnterDataForm()

    try:
        if request.method == "POST":
            graph = Graph()
            entered_date = request.form.get('Date')
            infected_user = User.query.filter_by(is_infected=True).first()

            date_to_check = request.form.get('Date')
            location_to_check = Location.query.filter_by(date=date_to_check, owner=current_user.id).first()
            report.gen_report(location_to_check)

            flash(f'User ID of infected user: {infected_user.id}', category='info')

            record = Location.query.filter_by(date=entered_date).all()

            #   algorithm that adds people to graph if in same area at same time
            for i, obj1 in enumerate(record):
                for j in range(i + 1, len(record)):
                    obj2 = record[j]
                    if obj1.name == obj2.name and obj1.time > obj2.time:
                        current_user.infection_chance = obj1.infection
                        graph.add_edge(obj1.owner, obj2.owner)

            print('Printing connections from infected individual to users for the day:')
            graph.dfs(infected_user.id)

            return redirect(url_for('report_page'))

    except Exception:
        flash(f'Error in generating report...no infected user?', category='danger')
        return redirect(url_for('report_page'))

    if request.method == "GET":
        owned_locations = Location.query.filter_by(owner=current_user.id)

        return render_template('report.html', report_form=report_form, owned_locations=owned_locations)


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin_page():
    admin_form = EnterDataForm()

    #   first check, is the user an admin?
    if current_user.username == 'admin':

        #   is this a post request??
        if request.method == "POST":

            #   if so, is it an update location call??
            if request.form.get("submit_a"):
                form_value = request.form.get('locationVal')
                form_location = request.form.get('Location')

                try:
                    Location.query.filter_by(name=form_location).update({Location.infection: form_value})
                    db.session.commit()
                    flash(f'Location {form_location} updated successfully!', category='success')
                except Exception:
                    flash('Bad entry. Please try again', category='danger')

            #   or perhaps it is an update user call?
            elif request.form.get("submit_b"):
                form_user = request.form.get('userID')
                form_infected = request.form.get('options')

                try:
                    if form_infected == 'infected':
                        db.session.query(User).filter(User.id == form_user).first().is_infected = True
                        db.session.query(User).filter(User.id == form_user).first().infection_chance = 100
                        Location.query.filter_by(owner=form_user).update({Location.visited: True})
                    else:
                        db.session.query(User).filter(User.id == form_user).first().is_infected = False
                        db.session.query(User).filter(User.id == form_user).first().infection_chance = 0
                        Location.query.filter_by(owner=form_user).update({Location.visited: False})

                    db.session.commit()
                    flash(f'User {form_user} updated successfully!', category='success')
                except Exception:
                    flash(f'Bad entry with user: {form_user}. Please try again', category='danger')

            return redirect(url_for('admin_page'))

        if request.method == "GET":
            locations = Location.query.all()
            users = User.query.all()
            return render_template('admin.html', admin_form=admin_form, users=users, locations=locations)

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

