import json
import socket
import ssl
import urllib.request
import urllib.error
import Config.config as config

# Yahoo Geocoding


def yahoogeocode(address):
    ssl._create_default_https_context = ssl._create_unverified_context
    socket.setdefaulttimeout(5)
    u_agent = urllib.request.build_opener()
    u_agent.addheaders = [('User-Agent', 'python-urllib-test')]
    api_end_point = config.yahoo_endpoint
    params = {
        'appid': config.yahoo_client_id,
        'output': 'json',
        'ei': 'UTF-8',
        'al': 4,
        'recursive': 'true',
        'query': address
    }

    encoded_params = urllib.parse.urlencode(params)
    req_url = api_end_point + '?' + encoded_params
    try:
        response = u_agent.open(req_url)
    except Exception as e:
        return 1, e
    else:
        pass

    res_all_json = response.read()
    res_all = json.loads(res_all_json)
    try:
        res_geocodes = res_all['Feature']
        tmp = res_geocodes[0]
        geocode = tmp['Geometry']['Coordinates']
        return 0, geocode
    except Exception as e:
        return 1, e
