#Для работы требуется импортировать DBclasses.
#engine = create_engine("postgresql+psycopg2://postgres:shaman482003@localhost/test14")
#session = Session(bind=engine)

from service_parent import service


class stol_service(service):
    def get(self, idles):
        getid = session.query(Stol.id, Stol.expand).filter_by(id=idles).all()
        return getid
    
    def getall(self):
        getidall = session.query(Stol.id, Stol.expand).all()
        return getidall
