from model import *
import os 
import server

os.system('dropdb family') 
os.system('createdb family')

connect_to_db(server.app)
db.create_all()

Rose = User(
            name='Rose Harris',
            email='rose@gmail.com',
            password='pass',

            )



db.session.add_all()([rose])) 
# some users are implicitly added by relationship to questions
db.session.commit()