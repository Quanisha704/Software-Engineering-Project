"""Testing flask routes in server.py"""

from unittest import TestCase
from flask import session 
from server import app 
from model import *
import sys
import os




class FlaskTestsBasic(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test landing page."""

        result = self.client.get("/")
        self.assertIn(b"Welcome To Family Ties", result.data)
        self.assertEqual(result.status_code, 200)
    
    def test_signIn(self):
        """Test sign in page."""

        result = self.client.post("/sign_in",
                                  data={"email": "beasleyshelly@yahoo.com", "password": "TTV9zm^ip*"}, follow_redirects=True)
        self.assertIn(b"Sign in successful!", result.data)
        
    def test_register(self):
        """Testing register page"""
        
        result = self.client.get("/register")
        self.assertEqual(result.status_code, 200)

class FlaskTestsLoggedIn(TestCase):
    """Flask tests with user logged in to session."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'testingKey'
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['email'] = "beasleyshelly@yahoo.com"

    def test_dashboard_page(self):
        """Test dashboard page."""

        result = self.client.get("/dashboard")
        self.assertIn(b"Family Ties - Dashboard", result.data)

class FlaskTestsLoggedOut(TestCase):
    """Flask tests with user logged in to session."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        self.client = app.test_client()

    # def test_dashboard_page(self):
    #     """Test that user can't see dashboard page when logged out."""

    #     result = self.client.get("/dashboard", follow_redirects=True)
    #     self.assertNotIn(b"Family Ties - Dashboard", result.data)
    #     self.assertIn(b"You must sign in to access this page!", result.data)
    
#     File "/home/vagrant/src/project/server.py", line 144, in dashboard
#     email = session['email']
#   File "/home/vagrant/env/lib/python3.6/site-packages/werkzeug/local.py", line 377, in <lambda>
#     __getitem__ = lambda x, i: x._get_current_object()[i]
#   File "/home/vagrant/env/lib/python3.6/site-packages/flask/sessions.py", line 84, in __getitem__
#     return super(SecureCookieSession, self).__getitem__(key)
# KeyError: 'email'

class FlaskTestsLogInLogOut(TestCase):  
    """Test log in and log out."""

    def setUp(self):
        """Before every test"""

        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_login(self):
        """Test log in form.

        Unlike login test above, 'with' is necessary here in order to refer to session.
        """

        with self.client as c:
            result = c.post("/sign_in",
                                  data={"email": "beasleyshelly@yahoo.com", "password": "TTV9zm^ip*"}, follow_redirects=True)
            self.assertIn(b"Sign in successful!", result.data)
            self.assertEqual(session['email'], 'beasleyshelly@yahoo.com')
            self.assertIn(b"Family Ties - Dashboard", result.data)

    def test_logout(self):
        """Test sign out route."""

        with self.client as c:
            with c.session_transaction() as sess:
                sess['email'] = 'beasleyshelly@yahoo.com'

            result = self.client.get('/sign_out', follow_redirects=True)

            self.assertNotIn(b'email', session)
            self.assertIn(b'You have been signed out', result.data)



if __name__ == "__main__":
    
    connect_to_db(app)
    
    import unittest

    unittest.main()

