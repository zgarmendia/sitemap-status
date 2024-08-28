import requests
import xml.etree.ElementTree as ET

def fetch_sitemap_index(index_sitemap_url):
    try:
        response = requests.get(index_sitemap_url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            sitemap_urls = [sitemap.find('ns:loc', namespaces).text for sitemap in root.findall('ns:sitemap', namespaces)]
            return [url for url in sitemap_urls if url.endswith('.xml')]
        else:
            print(f'Failed to fetch: {index_sitemap_url} - Status code: {response.status_code}')
            return []
    except ET.ParseError as e:
        print(f'Failed to parse XML: {e}')
        return []
    except requests.exceptions.RequestException as e:
        print(f'Error fetching sitemap: {e}')
        return []
