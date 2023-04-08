from itertools import chain
from .filtre_universale import filtre_universale


def get_all():
    fur_list = ['Sofa', 'Stol', 'Wardrobe']
    list_of_all_obj = [eval(f"{i}.objects.all()") for i in fur_list]
    return list_of_all_obj


def get(class_name, parameter_dict=None):
    if not parameter_dict:
        ans = get_all()
        return ans

    get_value = eval(f"{class_name}.objects.filter({filtre_universale(parameter_dict)})")
    return get_value
