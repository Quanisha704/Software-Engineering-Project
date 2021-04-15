"""Server for Family Ties Flask app."""

from flask import (Flask, request, render_template, redirect, session, flash)
from model import connect_to_db
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import crud

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


@app.route('/sign_in', methods= ['POST'])
def sign_in_post():
    """Grabs the information from sign form"""
    
    email = request.form.get('email')
    session['email'] = email
    
    password = request.form.get('password')
    session['password'] = password
    
    # user = crud.get_user_by_email(email)
    # if email == user.email:
    #     session['user_id'] = user_id
    #     session['email'] = email
    #     session['password'] = password
   
        
    return render_template('dashboard.html', email=email, password=password)

@app.route('/sign_out')
def sign_out():
    """Prompts the user to sign out"""   
    
    return render_template('sign_out.html')



# @app.route('/register')
# def register_form():
#     """Prompts the user to register for new account."""
    
#     return render_template('register.html') 


# @app.route('/register', methods = ['POST'])
# def register_post():
#     """Prompts the user to register."""
    
#     email = request.form.get('email')
#     password = request.form.get('password')
#     name = request.form.get('name')

#     user = crud.get_user_by_email(email)
#     if user:
#         flash('An account with the email address already exist. Please try again.')
#     else:
#         crud.create_user(email, password, name, dob, isAdmin)
#         flash('Account created! Please sign in.')

#     return redirect('/')

################################### PROFILE , CALENDAR
@app.route('/user_profile')
def profile():
    """Displays user profile information"""
    
    
    
    return render_template("user_profile.html")


@app.route('/calendar')
def calendar():
    """Displays calendar of events and important info"""
    
    return render_template("calendar.html")


           






if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
