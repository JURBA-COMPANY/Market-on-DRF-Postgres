def filtre_universale(parameter_dict: dict):
    str_for_return = ''
    for key, value in parameter_dict.items():
        str_for_return += f"{key}={value},"
    return str_for_return[:len(str_for_return)-1]
