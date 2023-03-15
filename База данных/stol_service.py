#Для работы требуется импортировать DBclasses.

from service_parent import service

class stol_service(service):
    def get(self, idles):
        getid = session.query(Stol.id, Stol.expand).filter_by(id=idles).all()
        return getid
