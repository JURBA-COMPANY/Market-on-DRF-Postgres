import * from DBclasses
from service_parent import service


engine = create_engine("postgresql+psycopg2://postgres:123@localhost/Mivla")
session = Session(bind=engine)

class wardrobe_service(service):
    def get(self, idles):
        getid = session.query(Wardrobe.id, Wardrobe.num_shelfs).filter_by(id=idles).all()
        return getid

    def getall(self):
        getidall = session.query(Wardrobe.id, Wardrobe.num_shelfs).all()
        return getidall
