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
    

################################ CRUD Functions for UserEvent table ############################

################################ CRUD Functions for Event table ############################



if __name__ == '__main__':
    from server import app
    connect_to_db(app)







