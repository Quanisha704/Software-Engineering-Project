"""Testing flask routes in server.py"""

from unittest import TestCase
from flask import session 
from server import app 
from model import *
import sys
import os
import crud



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
    
    def test_signIn(self):
        """Test sign in page."""

        result = self.client.post("/sign_in",
                                  data={"email": "ilucero@soto.org", "password": "J&8YDTtDtk"})
        self.assertIn(b"Sign in successful!", result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()

