import requests


def get_weather(place, keys):
    """
    Get weather for given place, with given settings.
    """
    url_template = "https://wttr.in/{}"
    url = url_template.format(place)
    response = requests.get(url, params=keys)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    places = ("London", "SVO", "Череповец")
    settings = {'n': '', 'T': '', 'q': '', 'M': '', 'lang': 'ru'}
    for place in places:
        print(get_weather(place, settings))
