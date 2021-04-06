"""Models for Family Ties App"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """A user"""
    
    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    email = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False) 
    profile_id = db.Column(db.Integer,
                        autoincrement = True)
    full_name = db.Column(db.String)
    DOB = db.Column(db.DateTime)
    current_location = db.Column(db.String)
    place_of_birth = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class UserEvent(db.Model):
    """A user event"""
    
    #Association table between users and events
    __tablename__ = 'userevents' 

    userevent_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key= True)
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.user_id')) 
    event_id = db.Column(db.Integer, 
                         db.ForeignKey('events.event_id'))
    
    event = db.relationship('Event', backref='userevents')
    user = db.relationship('User', backref='userevents')

    def __repr__(self):
        return f'<User userevent_id={self.userevent_id}>'
    

class Event(db.Model):
    """An event"""
    
    __tablename__ = 'events'

    event_id = db.Column(db.Integer,
                        primary_key= True)
    event_name = db.Column(db.String)
    event_date = db.Column(db.DateTime)
    admin_id = db.Column(db.Integer, 
                         db.ForeignKey('admin.admin_id'))

    admin = db.relationship('Admin', backref='events')
    
    def __repr__(self):
        return f'<Event event_id={self.event_id} event_name={self.event_name}>'


class Admin(db.Model):
    """A admin"""
    
    __tablename__ = 'admin'

    admin_id = db.Column(db.Integer,
                        primary_key= True)
    profile_id = db.Column(db.Integer,
                           db.ForeignKey('users.profile_id'))
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.user_id'))
    
    user = db.relationship('User', backref='admin')
    profile = db.relationship('User', backref='admin')

    def __repr__(self):
        return f'<Admin admin_id={self.admin_id}>'
    
    
def connect_to_db(flask_app, db_uri='postgresql:///users', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')
    
    
    if __name__ == '__main__':
        from server import app
        
        connect_to_db(app)