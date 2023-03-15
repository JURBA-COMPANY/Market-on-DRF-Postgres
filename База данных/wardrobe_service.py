#Для работы требуется импортировать DBclasses.

from service_parent import service


class wardrobe_service(service):
    def get(self, idles):
        getid = session.query(Wardrobe.id, Wardrobe.num_shelfs).filter_by(id=idles).all()
        return getid

    def getall(self):
        getidall = session.query(Wardrobe.id, Wardrobe.num_shelfs).all()
        return getidall
