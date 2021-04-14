"""Family Ties Flask app."""

from flask import Flask, request, render_template, redirect, request, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True
app.secret_key = "FAMILY"


@app.route('/')
def homepage():
    """Homepage for app to ask the user to sign in or register"""
    
    return render_template("welcomepage.html")


@app.route('/register')
def register():
    """Prompts the user to register. If name or email already stored, redirect."""
    
    # if 'name' or 'email' in session:
    #     return redirect('/sign_in')
    
    return render_template("register.html")
  

@app.route('/sign_in')
def login():
    """Prompts the user to sign in"""
    
    email = request.args.get('email')
    session['email'] = email 
    password = request.args.get('password')
    session['password'] = password     
    
    return render_template("sign_in.html")


@app.route('/profile')
def profile():
    """Displays user profile information"""
    
    return render_template("profile.html")


@app.route('/calendar')
def calendar():
    """Displays calendar of events and important info"""
    
    return render_template("calendar.html")


           






if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
