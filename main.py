import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from sitemap_fetch import fetch_sitemap_index
from sitemap_check import check_status_code

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] - %(message)s", datefmt="%Y-%m-%d %H:%M:%S",filename='sitemap_status.log', filemode='w')

sitemap_index_urls = ['https://www.vegasinsider.com/sitemap_index.xml', 'https://www.us-bookies.com/sitemap_index.xml'] 

for index_url in sitemap_index_urls:
    sitemap_urls= fetch_sitemap_index(index_url)
    if sitemap_urls:
        logging.info(f'Total sitemaps found: {len(sitemap_urls)}')
        logging.info('Checking status codes of individual sitemaps:')

    with ThreadPoolExecutor(max_workers=8) as executor:
        future_to_url= {executor.submit(check_status_code, url): url for url in sitemap_urls}
        for future in as_completed(future_to_url):
            try:
                url, status_code = future.result()
                logging.info(f'{url} - Status code: {status_code}')
            except Exception as e:
                 logging.error(f'Error processing URL: {e}')
else:
    logging.warning(f'No sitemap found in {index_url}')
logging.info(f'Finished processing sitemap index: {index_url}\n')
