#!/usr/bin/env python
# encoding: utf-8

import argparse
import time
import gzip
import urllib.request
from bs4 import BeautifulSoup
from io import StringIO

URL_BASE = "http://axecop.com/comic/"

def get_page(url):
    """Download a page and return a BeautifulSoup object of the html"""
    response = urllib.request.urlopen(url)
    page_content = response.read()

    if response.info().get('Content-Encoding') == 'gzip':
        gzipFile = gzip.GzipFile(fileobj=response)
        page_content = gzipFile.read()

    soup_page = BeautifulSoup(page_content, "html.parser")

    return soup_page

def download_episode(episode, download_dir='./'):
    url = '{0}episode-{1}'.format(URL_BASE, episode)
    print(url)

    #get remote page
    soup = get_page(url)

    #get image
    img_tag =soup.find('img', {'title':"Episode " + episode})
    img_src = img_tag['src']

    while True:
        time.sleep(2)
        print('Saving ' + img_src)
        try:
            urllib.request.urlretrieve(img_src, download_dir + episode + '.png')
        except urllib.error.HTTPError as http_err:
            print ('HTTP error ', http_err.code, ": ", http_err.reason)
            if http_err.code == 404:
                break
        except urllib.error.ContentTooShortError:
            print ('The image has been retrieve only partially.')
        except Exception as e:
            print ('Error ', str(e))
        else:
            break

def main():
    parser = argparse.ArgumentParser(description='AxeCop Downloader.')

    parser.add_argument('--episode', '-e',
                        action='store',
                        required=True,
                        help='Episode to download')

    args = parser.parse_args()

    download_episode(args.episode)

if __name__ == "__main__":
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0')]
    urllib.request.install_opener(opener)
    main()
