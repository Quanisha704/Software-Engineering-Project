# """Testing database"""

# #importing necessary libaries and files 
# from flask import Flask
# from model import *
# import unittest
# import sys
# import os
# import crud

# #creates and instance of flask 
# flask_app = Flask(__name__)


# #dropping and creating db called testdb
# os.system('dropdb testdb')
# os.system('createdb testdb  ')


# #Testing the class User from model.py
# class TestUser(unittest.TestCase):
    
#     def setUp(self):
        
#         connect_to_db(flask_app, db_uri='postgresql:///testdb', echo=True)
#         db.create_all()
        
#         self.user = crud.create_user(email='shelly@time.com', password = 'rY742&1@', fname = 'Shelly', lname = 'Harris', job = 'RN',
#                                      current_location = 'Texas',  place_of_birth = 'South Carolina', dob ='2000-12-09', isAdmin =False)
       
       
#     #Testing to make sure that the user object has been created is an instance of the User class
#     def test_user_creation(self):
#         self.assertIsInstance(self.user, User)
        
#     #Testing that the user object 'email' has been constructed properly 
#     def test_email(self):
#         self.assertEqual('shelly@time.com', self.user.email)
        
#     #Testing that the user object 'password' has been constructed properly 
#     def test_pw(self):
#         self.assertEqual('rY742&1@', self.user.password)
   
#     #Testing that the user object 'name' has been constructed properly 
#     def test_fname(self):
#         self.assertEqual('Shelly', self.user.fname)
    
#     #Testing that the user object 'current location' has been constructed properly 
#     def test_current_location(self):
#         self.assertEqual('Texas', self.user.current_location)
    
#     #Testing that the user object 'dob' has been constructed properly 
#     def test_dob(self):
#         self.assertEqual('2000-12-09', self.user.dob)
    
#     #Testing that the user object 'place of birth' has been constructed properly 
#     def test_pob(self):
#         self.assertEqual('South Carolina', self.user.place_of_birth)
    
#     #Testing that the user object 'isAdmin' has been constructed properly 
#     def test_admin(self):
#         self.assertEqual(False, self.user.isAdmin)
    
    
#     def tearDown(self):
#         db.drop_all()
        
        
# if __name__ == " __main__":
#     unittest.main()
    
    
    
   
   
   
        
    