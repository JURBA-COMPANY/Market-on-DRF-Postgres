import * from DBclasses
from service_parent import service


engine = create_engine("postgresql+psycopg2://postgres:123@localhost/Mivla")
session = Session(bind=engine)

class sofa_service(service):
    def get(self, idles):
        getid = session.query(Sofa.id, Sofa.num_seats, Sofa.expand, Sofa.corner).filter_by(id=idles).one()
        return getid

    def getall(self):
        getidall = session.query(Sofa.id, Sofa.num_seats, Sofa.expand, Sofa.corner).all()
        return getidall
