#Для работы требуется импортировать DBclasses.

from service_parent import service


class sofa_service(service):
    def get(self, idles):
        getid = session.query(Sofa.id, Sofa.num_seats, Sofa.expand, Sofa.corner).filter_by(id=idles).all()
        return getid

    def getall(self):
        getidall = session.query(Sofa.id, Sofa.num_seats, Sofa.expand, Sofa.corner).all()
        return getidall
