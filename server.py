"""Greeting Flask app."""

#from random import choice

from flask import Flask, request, render_template

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)


@app.route('/')
def homepage():
    """Homepage for app asks the user to sign in or register"""
    
    return render_template("welcomepage.html")
  

@app.route('/sign_in')
def login():
    """Prompts the user to login"""
    
    return render_template("sign_in.html")

@app.route('/register')
def register():
    """Prompts the user to register"""
    
    return render_template("register.html")
           






if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
