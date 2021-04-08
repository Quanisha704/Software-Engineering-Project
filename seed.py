from model import *
from faker import Faker
import os 
import server

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
# users = []

# for i in range(10):
#     u = User(email = fake.email(), 
#             password = fake.password(),
#             name = fake.name(),
#             dob = fake.date_of_birth())
#     users.append(u)
# print(users)


#Create user event from the user event table
# user_event=[]
# for i in range(5):
#     ue = UserEvent(userevent_id = fake.random_number()) #generating a random number for right now 
#     user_event.append(ue)
# print(user_event)
    

#Create event from the event table
events = []
for i in range(5):
    e = Event(event_date = fake.date())
    events.append(e)
print(events)


db.session.add_all(events) 
db.session.commit()