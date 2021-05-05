from model import db, User, UserEvent, Event, connect_to_db
from flask_sqlalchemy import SQLAlchemy
from faker import Faker

################################ CRUD Functions for User table ############################

def create_user(email, password, fname, lname, job, current_location, place_of_birth, dob, profile_url, isAdmin):
    """Create and return a new user"""
    
    user = User(email=email, password = password, fname=fname, lname=lname, job=job, 
                current_location = current_location, place_of_birth = place_of_birth, dob = dob, profile_url = profile_url, isAdmin = isAdmin )
    
    db.session.add(user)
    db.session.commit()
    
    return user

def all_users():
    """Returns all users"""
    
    return User.query.all()

def get_user_by_id(user_id):
    """Gets user by id"""
    
    return User.query.filter(User.user_id == user_id).one()

def get_user_by_email(email):
    """Checks if user email exists"""
    
    return User.query.filter(User.email==email).first()


def get_is_admin(isAdmin):  
    """Checks to see if user is an admin"""
    
    return User.query.filter(User.isAdmin == True).first()
    
    
    
################################ CRUD Functions for UserEvent table ############################
def create_user_event(userevent_id):
    """Create and return a new user event"""
    
    userevent = UserEvent(userevent_id = userevent_id)

    db.session.add(userevent)
    db.session.commit()
    
    return userevent

################################ CRUD Functions for Event table ############################

def create_event(title, start, url):
    """Create and return a new event"""
    
    event = Event(title = title, start = start, url = url)
    
    db.session.add(event)
    db.session.commit()
    
    return event

def all_events():
    """Returns all events"""
    
    return Event.query.all()

def get_event_by_id(id):
    """Gets event by id"""
    
    return Event.query.get(id)

def get_event_by_name(title):
    """Checks if event exists"""
    
    return Event.query.filter(Event.title==title).first()

def get_event_by_start_date(start):
    """Gets event by date"""
    
    return User.query.get(start)

 

   
if __name__ == '__main__':
    from server import app
    connect_to_db(app)







