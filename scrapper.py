import argparse
import logging
import re
import requests
from bs4 import BeautifulSoup
from ConfigParser import SafeConfigParser
try:
    # Python 3.x
    from urllib.request import urlopen, urlretrieve, quote
    from urllib.parse import urljoin
except ImportError:
    # Python 2.x
    from urllib import urlopen, urlretrieve, quote
    from urlparse import urljoin




logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL_PREFIX = "http://cdm.unfccc.int/Projects/Validation/DB/"
URL_POSTFIX = "/view.html"

# TODO
# Batch processing read from config file
# Concatenate the id to entire url

def read_unfcc_config_file():
    ids = []
    config = SafeConfigParser()
    config.read('unfcc_ids_config.ini')
    for (key, val) in config.items('main'):
        ids.append(val)

    return ids

def extract_downloadable_link(url):
    u = urlopen(url)
    try:
        html = u.read().decode('ISO-8859-1')
    finally:
        u.close()

    soup = BeautifulSoup(html, "html5lib")
    ahref_links = soup.findAll('a', attrs={'href': re.compile("^http://")})
    return ahref_links


def download_pdf(url):
    logger.info('Extracting the html')
    ahref_links = extract_downloadable_link(url)
    for ahref in ahref_links:
        if "FileStorage" in ahref.attrs['href']:
            link = (ahref.attrs['href'])
            file_name = ahref.getText() + '-' +ahref.attrs['href'].split('/')[-1]+'.pdf'
            try:
                r = requests.get(link, allow_redirects=True)
                open('downloads/'+file_name, 'wb').write(r.content)
                print("File is downloaded successfully. Please check di downloads/")
                return 1
            except:
                print('failed to download')
                return -1

    return 0

def get_args():
    '''This function parses and return arguments passed in'''
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description='UNFCC web scrapper')
    # Add arguments
    parser.add_argument(
        '-c', '--config', type=str, help='read from config file', default=True)
    parser.add_argument(
        '-u', '--url', type=str, help='unfcc url', required=False, nargs='+', default=None)
    parser.add_argument(
        '-i', '--id', type=str, help='unfcc ID', required=False, default=None)
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    config = args.config
    try:
        _url = args.url[0].split(",")
    except:
        _url = None

    id = args.id
    # Return all variable values
    return config, _url, id

def main(*args):
    config, _url, id = get_args()

    if str.lower(config) == "true":
        logger.info('Start reading unfcc id from unfcc_ids_config.ini')
        ids = read_unfcc_config_file()
        for _id in ids:
            target_url = URL_PREFIX+_id+URL_POSTFIX
            logger.info('Downloading %s' % target_url)
            status = download_pdf(target_url)
            if status:
                logger.info('Success')
            else:
                logger.info('Could not download the file')
    elif _url:
        pass
    else:
        pass

if __name__ == '__main__':
    main()