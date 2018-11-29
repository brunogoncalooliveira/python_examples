from clint.textui import progress
import requests
import os

def downloadfile_with_progress_bar(url, destination):
    http_proxy = ''
    https_proxy = ''
    ftp_proxy = ''
    if 'http_proxy' in os.environ:
        http_proxy = os.environ['http_proxy']
    if 'https_proxy' in os.environ:
        https_proxy = os.environ['https_proxy']
    if 'ftp_proxy' in os.environ:
        ftp_proxy = os.environ['ftp_proxy']
    downloadfile_with_progress_bar_with_proxies(url, destination, http_proxy=http_proxy, https_proxy=https_proxy, ftp_proxy=ftp_proxy)

def downloadfile_with_progress_bar_with_proxies(url, destination, http_proxy='', https_proxy='',ftp_proxy='', verify=False):
    proxyDict = {}
    if http_proxy != '':
        proxyDict['http'] = http_proxy
    if https_proxy != '':
        proxyDict['https'] = https_proxy
    if ftp_proxy != '':
        proxyDict['ftp'] = ftp_proxy
    r = requests.get(url, proxies=proxyDict, stream=True, verify=verify)
    with open(destination, 'wb') as f:
        total_length = int(r.headers.get('Content-Length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()
