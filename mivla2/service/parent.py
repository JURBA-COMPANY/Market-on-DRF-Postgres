from .filtre_universale import filtre_universale
from .models import *


class Service:
    def get_all(self, *args):
        list_of_all_obj = [i.objects.all() for i in args]
        return list_of_all_obj

    def get(self, class_name, parameter_dict=None):
        get_value = eval(f"{class_name}.objects.filter({filtre_universale(parameter_dict)})")
        return get_value
