from model import *
from faker import Faker
import os 
import server

os.system('dropdb family') 
os.system('createdb family')

connect_to_db(server.app)
db.create_all()

fake = Faker()
users = []

for i in range(10):
    u = User(email = fake.email(), password = fake.password(),
                    name = fake.name())
    users.append(u)
print(users)
    


db.session.add_all(users) 
# # some users are implicitly added by relationship to questions
db.session.commit()