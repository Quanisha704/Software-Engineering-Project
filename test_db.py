"""Testing database"""

#importing necessary libaries and files 
from flask import Flask
from model import *
import unittest
import sys
import os
import crud

#creates and instance of flask 
flask_app = Flask(__name__)


#dropping and creating db called testdb
os.system('dropdb testdb')
os.system('createdb testdb  ')


#Testing the class User from model.py
class TestUser(unittest.TestCase):
    
    def setUp(self):
        
        connect_to_db(flask_app, db_uri='postgresql:///testdb', echo=True)
        db.create_all()
        
        self.user = crud.create_user(email='shelly@time.com', password = 'rY742&1@', name = 'Shelly Green',
                                     current_location = 'Texas', dob ='2000-12-09', place_of_birth = 'South Carolina', isAdmin =False)
       
       

    #Testing to make sure that the user object has been created is an instance of the User class
    def test_user_creation(self):
        self.assertIsInstance(self.user, User)

    #Testing that the user object 'email' has been constructed properly 
    def test_email(self):
        self.assertEqual('shelly@time.com', self.user.email)
        
    # #Testing that the user object 'password' has been constructed properly 
    # def test_pw(self):
    #     expected_pw = self.user.password
    #     self.assertEqual(expected_pw, self.user.password)
   
    # #Testing that the user object 'name' has been constructed properly 
    # def test_name(self):
    #     expected_name = self.user.name
    #     self.assertEqual(expected_name, self.user.name)
    
    # #Testing that the user object 'current location' has been constructed properly 
    # def test_current_location(self):
    #     expected_CL= self.user.current_location
    #     self.assertEqual(expected_CL, self.user.current_location)
    
    # #Testing that the user object 'dob' has been constructed properly 
    # def test_dob(self):
    #     expected_dob= self.user.dob
    #     self.assertEqual(expected_dob, self.user.dob)
    
    # #Testing that the user object 'place of birth' has been constructed properly 
    # def test_pob(self):
    #     expected_pob= self.user.place_of_birth
    #     self.assertEqual(expected_pob, self.user.place_of_birth)
    
    # #Testing that the user object 'isAdmin' has been constructed properly 
    # def test_admin(self):
    #     expected_admin= self.user.isAdmin
    #     self.assertEqual(expected_admin, self.user.isAdmin)
    
    def tearDown(self):
        db.drop_all()
         
    
  
   
   
   
   
   
        
    