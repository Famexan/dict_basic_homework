def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """

    city = {}
    cities = set(cities)
    cities = list(cities)

    for i in  range(len(cities)):
        city[i] = cities[i-1]


    return city

sity = ['andijon','samarqand','toshkent']

print(cities_dict(sity))