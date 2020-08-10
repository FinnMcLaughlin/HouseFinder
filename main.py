from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# Specified property website URL: Daft.ie
property_url = "https://www.daft.ie/dublin-city/apartments-for-rent/?pt_id=1&cc_id=ct1&ignored_agents%5B0%5D=1551&s" \
               "%5Bignored_agents%5D%5B0%5D=1551&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d "

# Connects to URL and grabs HTML
uClient = uReq(property_url)
page_html = uClient.read()
uClient.close()

# Parses HTML
page_soup = soup(page_html, "html.parser")

# Stores all property item containers
prop_containers = page_soup.findAll("div", {"class": "PropertyCardContainer__container"})

# Extracts the relevant information (link to property URL, property address, price attributes etc.)
# Prints them to the console
for container in prop_containers:
    prop_link = "https://www.daft.ie/" + container.a["href"]
    prop_address = container.findAll("div", {"class": "PropertyInformationCommonStyles__addressCopy calculate-truncation-plugin"})[0].text.strip()
    prop_price = container.findAll("div", {"class": "PropertyInformationCommonStyles__propertyPrice"})[0].text.strip()
    prop_attributes = container.findAll("div", {"class": "QuickPropertyDetails__iconContainer"})

    print(prop_link)
    print(prop_address)
    print(prop_price)
    for attr in prop_attributes:
        print(attr.img["alt"])

    print("\n")
