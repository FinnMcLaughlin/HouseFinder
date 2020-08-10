from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


def parseHTML(property_url):
    # Connects to URL and grabs HTML
    uClient = uReq(property_url)
    page_html = uClient.read()
    uClient.close()

    return soup(page_html, "html.parser")
