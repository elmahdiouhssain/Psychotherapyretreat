from datetime import date

from database import User, RolesUsers, Role, User, Blog, Contact, db_session, init_db, Base, engine, db_session
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore, roles_required


# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = db_session()

user_datastore = SQLAlchemySessionUserDatastore(session,
										User, Role)

#user = User(email='aaa@aaa.aa', password='passpass')
user = User(username='ayman', email='sss@sss.ss', password='passpass')
user1 = User(username='anas',email='svv@sss.ss', password='passpass')

user2 = User(username='ahmad',email='sezs@sss.ss', password='passpass')
user3 = User(username='said',email='vvv@sss.dd', password='passpass')

session.add(user)
session.add(user1)
session.add(user2)
session.add(user3)

print("Users Done :)")

######################

cnt1 = Contact(name='wassim', mail='pspp@sss.ss', sub='I want to check in ..', msg='qsdjqksldqsdkqsdlkqsdqsd')
cnt2 = Contact(name='ayman', mail='ksss@sss.ss', sub='I want your help ..', msg='qsdjqksldqsdkqsdlkqsdqsd')
cnt3 = Contact(name='wassim', mail='b6hh@sss.ss', sub='can you help me ..', msg='qsdjqksldqsdkqsdlkqsdqsd')
cnt4 = Contact(name='asaad', mail='abidd@sss.ss', sub='best sales in surf', msg='qsdjqksldqsdkqsdlkqsdqsd')

session.add(cnt1)
session.add(cnt2)
session.add(cnt3)
session.add(cnt4)
print("Contacts Done :)")

##########################################################"""

post1 = Blog(title='Best day with surf hotel fammily', body='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', tags='qqskldqlksdjklqsdj', img_off='klqjdlkqjskdqsldk', categorie='Psycologue')
post2 = Blog(title='Surf time in imsouan', body='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', tags='qqskldqlksdjklqsdj', img_off='klqjdlkqjskdqsldk', categorie='Psycologue')
post3 = Blog(title='Tamraght summer vlog', body='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', tags='qqskldqlksdjklqsdj', img_off='klqjdlkqjskdqsldk', categorie='Psycologue')
post4 = Blog(title='Night party with surf hotel family', body='body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essenti', tags='qqskldqlksdjklqsdj', img_off='klqjdlkqjskdqsldk', categorie='Psycologue')



session.add(post1)
session.add(post2)
session.add(post3)
session.add(post4)

print("Posts Done :)")



##########################################################################################


session.commit()

session.close()

print("The Unitest Worky Seccussfly :)")

print("All Is Done ! :)")