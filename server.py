"""Server for Family Ties Flask app."""

from flask import (Flask, request, render_template, redirect, session, flash, url_for)
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db
from sqlalchemy import *
from jinja2 import StrictUndefined
import crud
import os

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True
app.secret_key = "FAMILY"




################################### LANDING PAGE, REGISTER, SIGN IN, SIGN OUT ##############################
@app.route('/')
def welcomepage():
    """Welcome page for app to ask the user to sign in or register"""
    
    return render_template('welcomepage.html')    


@app.route('/sign_in')
def sign_in_form():
    """Prompts the user to sign in"""   
    
    return render_template('sign_in.html')


@app.route('/sign_in', methods= ['GET', 'POST'])
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
    if not user:
        flash('Account does not exist! Please try again or register for a new account.', 'error')
        return redirect('/')
    
    #checks to see if user email or password matches
    if user.email != email or user.password != password:
        flash('Incorrect email or password! Please try again.', 'error')
        return redirect('/')
    
    #if user exists   
    if user:
        #adds users information to session
        session['email'] = email
        session['password'] = password  
        session['user_id'] = user.user_id
        session['name'] = user.name
        session['current_location'] = user.current_location
        session['dob'] = user.dob
        session['place_of_birth'] = user.place_of_birth
        session['isAdmin'] = user.isAdmin
        
        flash('Sign in successful!', 'success')
        return redirect('/dashboard')


@app.route('/sign_out')
def sign_out():
    """Signs the current user out and return the user to the landing page"""
    
    session.pop('user', None)
    flash('You have been signed out', 'success')   
    
    return redirect('/')



@app.route('/register')
def register_form():
    """Prompts the user to register for new account."""
    
    return render_template('register.html') 


@app.route('/register', methods = ['GET','POST'])
def register_post():
    """Grabs the information from registration form"""
    
    #required information for new user to input
    email = request.form.get('email') 
    password = request.form.get('password')
    name = request.form.get('name')
    current_location = request.form.get('current_location')
    dob = request.form.get('dob')
    place_of_birth = request.form.get('place_of_birth')
    isAdmin = request.form.get('isAdmin') == 'on'
    
    
    #adds new user information to session
    session['email'] = email
    session['password'] = password 
    session['name'] = name
    session['current_location'] = current_location
    session['dob'] = dob
    session['place_of_birth'] = place_of_birth
    session['isAdmin'] = isAdmin 
    print("*"*20, "about to call crud")
    
    #Check to make sure user doesn't already exist
    verify_user = crud.get_user_by_email(email)
    
    if verify_user:
        print("*"*20, "about to redirect")
        flash('A user with that email already exist', 'error')
        return redirect('/register')
    else:
        #creates a new user and adds the new user to the database
        print("*"*20, "sign in fail, about to redirect")
        crud.create_user(email, password, name, current_location, dob, place_of_birth, isAdmin)
        flash('Registration is successful. Please sign in.', 'success')
        return redirect('/')
         
    


    
   

################################### DASHBOARD, PROFILE AND CALENDAR PAGES############################

@app.route('/dashboard')
def dashboard():
    """Displays the user dashboard"""
    
    #redirects user if they are not signed in
    # if not session:
    #     return redirect('/')
    # else:
    #     return redirect('/dashboard')
    return render_template('dashboard.html')



@app.route('/user_profile')
def profile():
    """Displays user profile information"""
    
    return render_template('user_profile.html')


@app.route('/calendar')
def calendar():
    """Displays calendar of events"""
    
    return render_template('calendar.html')


           

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")

 
# {'email': 'ortegaeric@gmail.com', 'password': '_9Bp@KlG_5', 'name': 'Angela Avila', 'current_location': 'Florida', 
#  'dob': datetime.date(1921, 11, 9), 'place_of_birth': 'South Carolina', 'isAdmin': False}

 # #Testing that the user object 'user id' is not None
    # def test_user_id(self):
    #     self.assertIsNotNone(self.user.user_id, 'success')
