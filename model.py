"""Models for Family Ties App"""

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from datetime import *


db = SQLAlchemy()



class User(db.Model): 
    """A user"""
    
    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    email = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    fname = db.Column(db.String, nullable = False) 
    lname = db.Column(db.String, nullable = False)
    job = db.Column(db.String)
    current_location = db.Column(db.String)
    place_of_birth = db.Column(db.String)
    dob = db.Column(db.Date)
    profile_url =  db.Column(db.String)
    isAdmin = db.Column(db.Boolean, nullable = False)
    

   
    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email} password={self.password} fname={self.fname} lname={self.lname} job={self.job}  current_location = {self.current_location } place_of_birth = {self.place_of_birth} dob = {self.dob} profile_url = {self.profile_url} isAdmin = {self.isAdmin}>'


class UserEvent(db.Model):
    """A user event"""
    
    #Association table between users and events
    __tablename__ = 'userevents' 

    userevent_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key= True)
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.user_id')) 
    id = db.Column(db.Integer, 
                         db.ForeignKey('events.id'))
    
    event = db.relationship('Event', backref='userevents')
    user = db.relationship('User', backref='userevents')
    
    

    def __repr__(self):
        return f'<User userevent_id={self.userevent_id}>'
    

class Event(db.Model):
    """An event"""
    
    __tablename__ = 'events'

    id = db.Column(db.Integer,
                        primary_key= True)
    title = db.Column(db.String, nullable = False)
    start = db.Column(db.DateTime, nullable = False)
    url =  db.Column(db.String)
    
    
    def __repr__(self):
        return f'<Event id={self.id} title={self.title} start={self.start} url={self.url}>'

    

    
def connect_to_db(flask_app, db_uri='postgresql:///family', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    
    
    print('Connected to the db!')
    
    
if __name__ == '__main__':
    from server import app
  
    connect_to_db(app)
    
    
    