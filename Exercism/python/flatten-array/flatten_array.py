def flatten(iterable):
    flatten_list = list()

    for element in iterable:
        if isinstance(element, list):
            flatten_list = flatten_list + flatten(element)
        else:
            flatten_list.append(element)

    return sorted(flatten_list)
