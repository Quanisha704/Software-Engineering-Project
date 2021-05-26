"""Testing flask routes and database in server.py"""

from unittest import TestCase
from flask import session 
from server import app 
from model import *
import crud
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
        self.assertIn(b"Welcome to Family Ties! A place to connect with family both near and far", result.data)
        self.assertEqual(result.status_code, 200)
    
    def test_signIn(self):
        """Test sign in page."""

        result = self.client.post("/sign_in",
                                  data={"email": "jeffrey62@alexander.net", "password": "4aVD2fKd*2"}, follow_redirects=True)
        self.assertIn(b"See Calendar", result.data)
        
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
                sess['email'] = "jeffrey62@alexander.net"

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

    def test_dashboard_page(self):
        """Test that user can't see dashboard page when logged out."""

        result = self.client.get("/dashboard", follow_redirects = True)
        self.assertNotIn(b"Family Ties - Dashboard", result.data)

    
class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///test_db")

        # Create tables and add sample data
        db.create_all()
        
        self.user = crud.create_user(email='maryc123@yahoo.com', password = 'K9#n*Hs73', fname = 'Mary', lname = 'Crews', job = 'Night Auditor',
                                     current_location = 'Florida',  place_of_birth = 'Iowa', dob ='1977-11-03', isAdmin =False)

    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()
        
        
    def test_user_creation(self):
        """Test user profile page and to make sure user object 
        has been created successfully"""
        
        self.assertIsInstance(self.user, User)
        
    def test_email(self):
        """Testing that the user object 'email' 
        has been constructed properly"""
        
        self.assertEqual('maryc123@yahoo.com', self.user.email)
    
    def test_admin(self):
        """Testing that the user object 'isAdmin' has 
        been constructed properly"""
        
        self.assertEqual(False, self.user.isAdmin)
        
        
        
if __name__ == "__main__":
    
    connect_to_db(app)
    
    import unittest

    unittest.main()
