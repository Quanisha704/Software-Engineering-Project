"""Server for Family Ties Flask app."""

from flask import (Flask, request, render_template, redirect, session, flash, url_for, jsonify)
#from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db
from sqlalchemy import *
from jinja2 import StrictUndefined
import cloudinary.uploader
import json
import crud
import os
from datetime import datetime


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True
app.secret_key = "FAMILY"



CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_KEY_SECRET = os.environ['CLOUDINARY_SECRET']

################################### LANDING PAGE, REGISTER, SIGN IN, SIGN OUT ##############################
@app.route('/')
def welcomepage():
    """Welcome page for app to ask the user to sign in or register"""
    
    return render_template('welcomepage.html')    


@app.route('/sign_in')
def sign_in_form():
    """Prompts the user to sign in"""   
    
    return render_template('sign_in.html')


@app.route('/sign_in', methods= ['POST'])
def sign_in_post():
    """Grabs the information from sign form and checks against the database.
    If email and password match, then user will be sent to personal dashboard. Otherwise 
    the user will need to attempt to sign in again"""
    
    #required information for user to input
    email = request.form.get('email') 
    password = request.form.get('password')
    
    #searches for the user in the database
    user = crud.get_user_by_email(email) 
    
    #checks to see if user exist or not
    # if not user:
    #     flash('Account does not exist! Please try again or register for a new account.', 'error')
    #     return redirect('/')
    
    # #checks to see if user email or password matches
    # if user.email != email or user.password != password:
    #     flash('Incorrect email or password! Please try again.', 'error')
    #     return redirect('/')
    
    #if user exists   
    if user is not None:
        #adds users information to session
        session['user_id'] = user.user_id
        session['email'] = email
        session['password'] = password  
        session['fname'] = user.fname
        session['lname'] = user.lname
        session['job'] = user.job
        session['current_location'] = user.current_location
        session['place_of_birth'] = user.place_of_birth
        session['dob'] = user.dob
        session['isAdmin'] = user.isAdmin
        
        flash('Sign in successful!', 'success')
        return redirect('/dashboard')
    else:
        flash('Incorrect email or password! Please try again.', 'error')
        return redirect('/')


@app.route('/sign_out')
def sign_out():
    """Signs the current user out and return the user to the landing page"""
    
    del session['email']
    flash('Sign out successful', 'success')   
    
    return redirect('/sign_in')



@app.route('/register')
def register_form():
    """Prompts the user to register for new account."""
    
    return render_template('register.html') 


@app.route('/register', methods = ['POST'])
def register_post():
    """Grabs the information from registration form"""
    
    #required information for new user to input
    email = request.form.get('email') 
    password = request.form.get('password')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    job = request.form.get('job')
    current_location = request.form.get('current_location')
    place_of_birth = request.form.get('place_of_birth')
    dob = request.form.get('dob')
    isAdmin = request.form.get('isAdmin') == 'on'
    
    
    #adds new user information to session
    session['email'] = email
    session['password'] = password 
    session['fname'] = fname
    session['lname'] = lname
    session['job'] = job
    session['current_location'] = current_location
    session['place_of_birth'] = place_of_birth
    session['dob'] = dob
    session['isAdmin'] = isAdmin 
   
    
    #Check to make sure user doesn't already exist
    verify_user = crud.get_user_by_email(email)
   
    
    if verify_user:
        flash('A user with that email already exist', 'error')
        return redirect('/register')
    else:
        #creates a new user and adds the new user to the database
        crud.create_user(email, password, fname, lname, job, current_location, place_of_birth, dob, isAdmin)
        flash('Registration is successful. Please sign in.', 'success')
        return redirect('/')
         

################################### DASHBOARD, PROFILE, CALENDAR, ADMIN, USERS PAGES############################

@app.route('/dashboard')
def dashboard():
    """Displays the user dashboard"""
    
    # email = session['email']
    
    # user = crud.get_user_by_email(email)
    
    if 'email' not in session:
        flash("You must sign in to access the dashboard!")
        return redirect('/sign_in')
    else:
       return render_template('dashboard.html')


@app.route('/user_profile', methods = ['GET'])
def profile():
    """Displays user profile information"""
   
    if 'email' not in session:
        flash("You must sign in to access the profile page!")
        return redirect('/sign_in')
    else:
        email = session['email']
        user = crud.get_user_by_email(email)
        return render_template('user_profile.html', user = user)

           
@app.route('/user_profile', methods=['POST'])
def profile_form_post():
    """Get the image the user submits and display it on the page"""   
    
    
    my_file = request.files['my-file']
    
    result = cloudinary.uploader.upload(my_file,
                                        api_key=CLOUDINARY_KEY,
                                        api_secret=CLOUDINARY_KEY_SECRET,
                                        cloud_name="dhtz9dptw")
    profile_url = result['secure_url']
   
    email = session['email'] 
   
    user = crud.get_user_by_email(email)
    
    user.profile_url = profile_url
    
    
    return render_template("user_profile.html", user = user)


@app.route('/admin')
def admin_create_event():
    """Allows the admin to create events"""
    
    email = session['email'] 
     
    verify_isAdmin = crud.get_user_by_email(email)
    
    
    if verify_isAdmin.isAdmin == True:
        flash("Welcome to your admin page", 'success')
        return render_template("admin.html") 
    else:
        flash("Admin privileges only!", 'error')
        return redirect('/dashboard')
   


@app.route('/admin', methods = ['POST'])
def admin_create_event_post():
    """Grabs the information from the form that admin uses to create an event"""
    
    title = request.form.get('title') 
    start = request.form.get('start')
    url = request.form.get('url')
     
    #Check to make sure event doesn't already exist
    verify_event = crud.get_event_by_name(title)
   
    
    if verify_event:
        flash('An event with that name already exist. Please try again', 'error')
        return redirect('/admin')
    else:
        #creates a new event and adds the new event to the database
        crud.create_event(title, start, url)
        flash('Event successfully created!', 'success')
        return redirect('/dashboard')
         
                   
@app.route('/calendar')
def calendar():
    """Displays calendar of events"""
    
    
    if 'email' not in session:
        flash("You must sign in to access the calendar!", "error")
        return redirect('/sign_in')
    else:
        return render_template('calendar.html')

    
@app.route('/all_events')
def all_events():
    events = crud.all_events()

    events_to_jsonify = []

    for event in events:
        events_to_jsonify.append({
          "start": event.start.strftime("%Y-%m-%d"), 
          "title": event.title,
          "url": event.url,
          "popup":{"title": "this is it", "descri": "this is des",}
        })
    return jsonify(events_to_jsonify)

    

@app.route('/all_users')
def all_users():
    """Displays all users"""
    
    users = crud.all_users()
    
    if 'email' not in session:
        flash("You must sign in to access this page", "error")
        return redirect('/sign_in')
    else:
        return render_template('all_users.html', users=users)
    

    
    
    
   


if __name__ == '__main__':
    
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
    
    
