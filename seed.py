from model import *
from faker import Faker
from datetime import datetime

import random
import os 
import server
import crud
import json


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
    password = fake.password( special_chars=True, digits=True, upper_case=True, lower_case=True)
    fname = fake.first_name()
    lname = fake.last_name()
    job = fake.job()
    current_location = fake.state()
    dob = fake.date_of_birth(minimum_age=13)
    place_of_birth = fake.state()
    isAdmin = fake.boolean(chance_of_getting_true=10)
   

    db_user = crud.create_user(email, password, fname, lname, job, current_location, place_of_birth, dob, isAdmin)
    users.append(db_user)

#Create user event from the user event table
user_event=[]
for i in range(10):
    userevent_id = fake.random_number() #generating a random number for right now 
    db_userevent = crud.create_user_event(userevent_id)
    user_event.append(db_userevent)
    
# Load events data from JSON file
with open('data/events.json') as f:
    event_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings
events_in_db = []

for event in event_data:
    event_name, event_location = (event['event_name'], event['event_location'])
    event_date = datetime.strptime(event['event_date'], '%Y-%m-%d')
    start_at = event['start_at']
    end_at = event['end_at']
    
    
    db_event = crud.create_event(event_name, event_date, event_location, start_at, end_at)
    events_in_db.append(db_event)
# #Create event from the event table
# events = []
# for i in range(5):
#     event_name = fake.name() #checking to see if there is a provider to generate fake event names if not try to see how to possilbly create my own provider 
#     event_date = fake.date()

    # db_event = crud.create_event(event_name, event_date)
    # events.append(db_event)
