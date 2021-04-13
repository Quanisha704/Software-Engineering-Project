from model import db, User, UserEvent, Event, connect_to_db
from flask_sqlalchemy import SQLAlchemy
from faker import Faker

################################ CRUD Functions for User table ############################

def create_user(email, password, name, dob):
    """Create and return a new user"""
    
    user = User(email=email, password = password, name=name, dob = dob)
    
    db.session.add(user)
    db.session.commit()
    
    return user

def all_users():
    """Returns all users"""
    
    return User.query.all()

def get_user_by_id(user_id):
    """Gets user by id"""
    
    return User.query.get(user_id)

def get_user_by_email(email):
    """Checks if user email exists"""
    
    return User.query.filter(User.email==email).first()

def get_user_by_name(name):
    """Checks if user name exists"""
    
    return User.query.filter(User.name==name).first()

def is_user_admin(isAdmin):
    """Checks to see if user isAdmin"""
    
    return User.query.filter(User.isAdmin == isAdmin).first()   #ask if this is the correct way to query for admin 
    

################################ CRUD Functions for UserEvent table ############################
def create_user_event(userevent_id):
    """Create and return a new user event"""
    
    userevent = UserEvent(userevent_id = userevent_id)



################################ CRUD Functions for Event table ############################

def create_event(event_name, event_date):
    """Create and return a new event"""
    
    event = Event(event_name=event_name, event_date=event_date)
    
    db.session.add(event)
    db.session.commit()
    
    return event

def all_events():
    """Returns all events"""
    
    return Event.query.all()

def get_event_by_id(event_id):
    """Gets event by id"""
    
    return Event.query.get(event_id)

def get_event_by_name(event_name):
    """Checks if event exists"""
    
    return Event.query.filter(Event.event_name==event_name).first()

def get_event_by_date(event_date):
    """Gets event by date"""
    
    return User.query.get(event_date)

 

   
if __name__ == '__main__':
    from server import app
    connect_to_db(app)







