from itertools import chain
from .filtre_universale import filtre_universale
from .models import *



def get_all_from_table(*args):
    list_of_all_obj = [eval(f"{i}.objects.all()") for i in args]
    return list_of_all_obj


def get(class_name, parameter_dict=None):
    if not parameter_dict:
        ans = get_all()
        return ans

    get_value = eval(f"{class_name}.objects.filter({filtre_universale(parameter_dict)})")
    return get_value
