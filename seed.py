from model import *
from faker import Faker
import random
import os 
import server
import crud

#dropping and creating database called family 
os.system('dropdb family') 
os.system('createdb family')

#connecting to server.py and creating all databases
connect_to_db(server.app)
db.create_all()

#Creating an instance(obj) of Faker 
fake = Faker()

#Create users from user table by generating fake data
#and store them in a list so we can use them 
#to create user accounts and profiles 
users = []

for i in range(10):
    email = fake.email()
    password = fake.password()
    name = fake.name()
    dob = fake.date_of_birth()
    isAdmin = fake.boolean()
   

    db_user = crud.create_user(email, password, name, dob, isAdmin)
    users.append(db_user)

#Create user event from the user event table
user_event=[]
for i in range(10):
    userevent_id = fake.random_number() #generating a random number for right now 
    db_userevent = crud.create_user_event(userevent_id)
    user_event.append(db_userevent)
    

#Create event from the event table
events = []
for i in range(5):
    event_name = fake.name() #checking to see if there is a provider to generate fake event names if not try to see how to possilbly create my own provider 
    event_date = fake.date()

    db_event = crud.create_event(event_name, event_date)
    events.append(db_event)
