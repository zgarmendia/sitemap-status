import requests

def check_status_code(url):
    try:
        response = requests.get(url)
        return url, response.status_code
    except requests.exceptions.RequestException as e:
        print (f'Error fetching {url}: {e}')
        return url, None