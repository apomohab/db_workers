from db_workers import Base, Factory, Worker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///paintfactory.db')

Base.metadata.bind  = engine

DBsession = sessionmaker(bind = engine)

session = DBsession()


paint = Factory(name = 'Paint Factory')

session.add(paint)
session.commit()

employ1 = Worker(name='hamada',age = '25',special='paint helper', factory = paint)

session.add(employ1)
session.commit()

employ2 = Worker(name='yamin',age = '25',special='cleaning', factory = paint)
session.add(employ2)
session.commit()

employ3 = Worker(name='hasan',age = '26',special='store', factory = paint)
session.add(employ3)
session.commit()


employ4 = Worker(name='alaa',age = '25',special='paint line', factory = paint)
session.add(employ4)
session.commit()


employ5 = Worker(name='mostafa',age = '28',special='cleaning line help', factory = paint)
session.add(employ5)
session.commit()


employ6 = Worker(name='salah',age = '40',special='cl systems', factory = paint)
session.add(employ6)
session.commit()


employ7 = Worker(name='nabil',age = '29',special='driver', factory = paint)
session.add(employ7)
session.commit()


employ8 = Worker(name='nagib',age = '35',special='paint room', factory = paint)
session.add(employ8)
session.commit()


employ9 = Worker(name='abbas',age = '23',special='paint room', factory = paint)
session.add(employ9)
session.commit()

employ10 = Worker(name='habib',age = '20',special='coils connect', factory = paint)
session.add(employ10)
session.commit()









