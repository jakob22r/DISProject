from flask import Blueprint, render_template, flash, request
from flask_bcrypt import Bcrypt
from . import forms, queries as q, models, conn, bcrypt
from flask import render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, current_user, logout_user, login_required

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

            if result and bcrypt.check_password_hash(result[1], password):
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
    flash('Logout successful.', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = forms.CreateUserForm()
    if request.method == 'GET':
        return render_template('signup.html', form=form)
    elif request.method =='POST':
        id = form.id.data
        username = form.username.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        #TODO: Check user with given ID does not already exist

        q.insert_user(conn, id, username, hashed_password)
        flash('New user successfully registered!', 'success')
        return redirect(url_for('auth.signup'))

@auth.route('/vote', methods=['GET','POST'])
@login_required
def vote():
    votes = q.count_votes(conn)
    titles = q.upcomingsongs_titleNCountry(conn)
    upTitles = []
    for title in titles:
        upTitles.append(title[0].strip() + " (" + title[1].strip() + ")")

    form = forms.TitelForm()
    form.dropdown.choices = [(title, title) for title in upTitles]

    if request.method == 'POST':

        if form.validate_on_submit():            
            titel = request.form.get('dropdown').split()[0]
            userID = current_user.get_id()

            #ensure user has not voted for the song already
            if len(q.unique_vote(conn, titel, userID)) == 0:
                q.add_vote(conn, userID, titel)
                #recalculate the placings after the user at voted
                votes = q.count_votes(conn)
                return render_template('vote.html', votes_tups=votes, form=form)
            else: 
                #render men med besked om du ikke kan stemme på den samme
                flash("You cannot vote for the same song more than once. Pick another favourite!")
       
    return render_template('vote.html', votes_tups=votes, form=form)


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
