from user_agents import parse
import requests

COUNTRY_DICT = {
    'IN': 'India',
    'AE': 'United Arab Emirates',
    'BH': 'Bahrain',
    'IQ': 'Iraq',
    'IL': 'Israel',
    'JO': 'Jordan',
    'KW': 'Kuwait',
    'LB': 'Lebanon',
    'OM': 'Oman',
    'QA': 'Qatar',
    'SA': 'Saudi Arabia',
    'SY': 'Syria',
    'YE': 'Yemen',
}

def get_request_data(request):
    result ={
        "ip": "Not Available",
        "city": "Not Available",
        "state": "Not Available",
        "country": "Not Available",
        "isp": "Not Available",
        "user-agent": "Not Available",
    }

    try:
        result['ip'] = request.META.get('REMOTE_ADDR')
    except:
        pass

    def get_location():
        # ip_address = '103.147.208.177'
        ip_address = request.META.get('REMOTE_ADDR')
        response = requests.get(f'https://ipinfo.io/{ip_address}/json').json()

        country = response.get('country')
        if COUNTRY_DICT.get(country) is not None:
            country = COUNTRY_DICT[country]

        return {
            "isp":response.get('org'),
            "city":response.get('city'),
            "state":response.get('region'),
            "country": country,
        }
    
    try:
        result.update(get_location())
    except:
        pass
    
    try:
        result['user-agent']=str(parse(request.META.get('HTTP_USER_AGENT')))
    except:
        pass
    return result