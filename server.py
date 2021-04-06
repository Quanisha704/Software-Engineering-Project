"""Greeting Flask app."""

#from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)


@app.route('/')
def homepage():
    """Prompts the user to sign up or sign in"""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Family Ties</title>
      </head>
      <body>
        <h3>Welome to FamilyTies</h3>
        <form>
          Please sign up or sign in!<br>
          Email:  <input type="text" name="email">
          Password:<input type="text" name="password">
          <input type="submit" value="Sign In">
          <input type="submit" value="Sign Up">
        </form>
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
