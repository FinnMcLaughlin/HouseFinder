from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq, Request


def parseHTML(property_url):
    # Connects to URL and grabs HTML
    request = Request(property_url, headers={'User-Agent': 'Mozilla/5.0'})
    uClient = uReq(request)
    page_html = uClient.read()
    uClient.close()

    return soup(page_html, "html.parser")
