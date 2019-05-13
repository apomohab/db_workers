from db_workers import Base, Factory, Worker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import Flask, render_template

app = Flask(__name__)

engine = create_engine('sqlite:///paintfactory.db')

Base.metadata.bind  = engine

DBsession = sessionmaker(bind = engine)

session = DBsession()


@app.route('/')
@app.route('/factories/<int:factory_id>/')
def factory(factory_id):

    factory = session.query( Factory ).filter_by(id=factory_id).first()
    workers  = session.query(Worker).filter_by(factory_id = Factory.id)

    return render_template('menu.html',factory=factory,workers=workers)



if __name__ == '__main__' :

    app.debug= True

    app.run(host ='0.0.0.0', port=5000, threaded=False)
