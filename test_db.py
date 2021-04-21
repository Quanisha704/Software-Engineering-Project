"""Testing database"""

import unittest

from faker import Faker

from model import User, UserEvent, Event


class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.fake = Faker()
        self.user = User(
            email = self.fake.email(),
            password = self.fake.password(),
            name = self.fake.name(),
            current_location = self.fake.state(),
            dob = self.fake.date_of_birth(),
            place_of_birth = self.fake.state(),
            isAdmin = self.fake.boolean()
           
        )

    #Testing to make sure that the user object has been created is an instance of the User class
    def test_user_creation(self):
        self.assertIsInstance(self.user, User)

    #Testing that the user object 'email' has been constructed properly 
    def test_email(self):
        expected_email = self.user.email
        self.assertEqual(expected_email, self.user.email)
        
    #Testing that the user object 'password' has been constructed properly 
    def test_pw(self):
        expected_pw = self.user.password
        self.assertEqual(expected_pw, self.user.password)
   
    #Testing that the user object 'name' has been constructed properly 
    def test_name(self):
        expected_name = self.user.name
        self.assertEqual(expected_name, self.user.name)
    
    #Testing that the user object 'current location' has been constructed properly 
    def test_current_location(self):
        expected_CL= self.user.current_location
        self.assertEqual(expected_CL, self.user.current_location)
    
    #Testing that the user object 'dob' has been constructed properly 
    def test_dob(self):
        expected_dob= self.user.dob
        self.assertEqual(expected_dob, self.user.dob)
    
    #Testing that the user object 'place of birth' has been constructed properly 
    def test_pob(self):
        expected_pob= self.user.place_of_birth
        self.assertEqual(expected_pob, self.user.place_of_birth)
    
    #Testing that the user object 'isAdmin' has been constructed properly 
    def test_admin(self):
        expected_admin= self.user.isAdmin
        self.assertEqual(expected_admin, self.user.isAdmin)
        
   
   
   
   
   
   
        
    