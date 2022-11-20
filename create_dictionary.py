def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    dic = {}

    for i in range(len(key)):
        #dic[key(i)] = value[i]
        dic.update({ke[i] : val[i]})

    return dic

