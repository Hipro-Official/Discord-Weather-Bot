import requests

base_url = 'http://geoapi.heartrails.com/api/json?method=searchByGeoLocation&'


def heartrails(coordinate):
    split_coordinate = coordinate.split(',')
    complete_url = base_url + 'x=' + \
        str(split_coordinate[0]) + '&y=' + str(split_coordinate[1])
    response = requests.get(complete_url)
    coordinateinfo = response.json()
    return coordinateinfo['response']['location'][0]
