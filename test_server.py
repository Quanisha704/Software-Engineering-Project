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

# class FlaskTestsLoggedIn(TestCase):
#     """Flask tests with user logged in to session."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         app.config['TESTING'] = True
#         app.config['SECRET_KEY'] = 'testingKey'
#         self.client = app.test_client()

#         with self.client as c:
#             with c.session_transaction() as sess:
#                 sess['email'] = "beasleyshelly@yahoo.com"

#     def test_profile_page(self):
#         """Test profile page."""

#         result = self.client.get("/user_profile")
#         self.assertIn(b"Your profile details are below:", result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()

