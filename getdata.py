#how to print the data from db

from db_workers import Base, Factory, Worker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///paintfactory.db')

Base.metadata.bind  = engine

DBsession = sessionmaker(bind = engine)

session = DBsession()


#data = session.query(Worker).all()

#for info in data :

    #print info.special #we can change at wanted mission.
    

hamada = session.query(Worker).filter_by(name='hamada')

for info in hamada:
    print 'Hamada Details'
    print info.name
    print info.age
    print info.special
    print info.id


alaa = session.query(Worker).filter_by(name = 'alaa')

for info2 in alaa:
    print 'Alla Details'
    print info2.name
    print info2.age
    print info2.special


#change the age for worker

hamada_edit_age = session.query(Worker).filter_by(id = 1).one()
print "now edit the age for hamada worker"
#print hamada_edit_age.age #for test

hamada_edit_age.age = '27'
session.add(hamada_edit_age)
session.commit()

print hamada_edit_age.age