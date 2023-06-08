from flask import Blueprint, render_template, flash
from . import forms, queries as q, models, conn
from flask import render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, current_user, logout_user, login_required
#from queries imp



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    form = forms.LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            result = q.lookup_user(conn, username)

            if result and password == result[1]:
                user_id = result[0]
                user = models.User(user_id, username)
                login_user(user)
                return redirect(url_for('auth.stats'))
            else:
                print("Invalid login")
                flash('Invalid username or password.', 'danger')

        return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    print("Logged out")
    flash('Logout successful.', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/stats', methods=('GET', 'POST'))
@login_required #Check that user is logged in
def stats():

    winners = q.select_winner_songs_last10years(conn)
    null_p = q.select_null_points(conn)

    form = forms.SearchYearForm()
    if request.method == 'POST':

        if form.validate_on_submit():
            year = form.year.data
            #Process data as needed
            winner_year_x = q.select_winner_by_year(conn,year)
            return render_template('stats.html', winner_tups=winners, null_tups=null_p, form=form, qrs=winner_year_x)

    return render_template('stats.html', winner_tups=winners, null_tups=null_p, form=form)
