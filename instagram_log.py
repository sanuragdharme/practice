from bs4 import BeautifulSoup
import requests

# instagram URL
URL = "https://www.instagram.com/{}/"


def parse_data(content):
    data = {}
    content = content.split('-')[0]
    content = content.split(' ')
    data['Followers'] = content[0]
    data['Following'] = content[2]
    data['Posts'] = content[4]

    return data


def scrap_data(username):
    request = requests.get(URL.format(username))
    response = BeautifulSoup(request.text, 'html.parser')
    meta = response.find('meta', property='og:description')
    return parse_data(meta.attrs['content'])


if __name__ == '__main__':
    data = scrap_data(username='')
    print(data)
