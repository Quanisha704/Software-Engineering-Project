"""Models for Family Ties App"""


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def connect_to_db(flask_app, db_uri='postgresql:///users', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')
    

class User(db.Model):
    """A user"""
    
    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key= True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    profile_id = db.Column(db.Integer,
                        autoincrement= True)
    full_name = db.Column(db.String)
    DOB = db.Column(db.DateTime)
    current_locationd= db.Column(db.String)
    place_of_birth = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'
    
    
    
    
    
    # if __name__ == '__main__':
    #     #from server import app
    #     connect_to_db(app)