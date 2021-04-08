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





if __name__ == '__main__':
    from server import app
    connect_to_db(app)







################################ CRUD Functions for UserEvent table ############################

################################ CRUD Functions for Event table ############################