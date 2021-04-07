from model import *
from faker import Faker
import os 
import server

os.system('dropdb family') 
os.system('createdb family')

connect_to_db(server.app)
db.create_all()





# db.session.add_all()() 
# # some users are implicitly added by relationship to questions
# db.session.commit()