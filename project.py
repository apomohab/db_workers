#add all data in project for make website

from db_workers import Base, Factory, Worker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import Flask

app = Flask(__name__)

engine = create_engine('sqlite:///paintfactory.db')

Base.metadata.bind  = engine

DBsession = sessionmaker(bind = engine)

session = DBsession()

@app.route('/')
@app.route('/factory')

def factorypaint():

    factory = session.query(Factory).filter_by(id=10).all()
    items = session.query(Worker).filter_by(factory_id=factory.id)

    output = ''

    for i in items :

        output += i.name
        output += '</br>'
        output += i.age
        output += '</br>'
        output += i.special
        output += '</br>'

    return output

if __name__ == '__main__' :

    app.debug= True

    app.run(host ='0.0.0.0', port=5000, threaded=False)
