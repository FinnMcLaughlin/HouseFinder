import html_parser


def parse_html(url_parameters):

    foundResult = False

    # Specified property website URL: Rent.ie
    property_url = "https://www.rent.ie/"

    for parameter in url_parameters:
        property_url += parameter

    page_soup = html_parser.parseHTML(property_url)

    prop_containers = page_soup.findAll("div", {"class": "search_result"})

    # Array to store dictionaries containing information on each property
    allProperties = []

    for container in prop_containers:

        prop_link = container.findAll("div", {"class": "sresult_address"})[0].h2.a["href"]

        prop_address = container.findAll("div", {"class": "sresult_address"})[0].h2.a.text.strip()

        prop_price = container.findAll("div", {"class": "sresult_description"})[0].h4.text.strip()

        prop_attributes_string = container.findAll("div", {"class": "sresult_description"})[0].h3.text.strip()

        prop_attr_split = prop_attributes_string.split(",")
        prop_attributes = []

        for index in range(0, len(prop_attr_split)):
            prop_attributes.append(prop_attr_split[index].strip())

        propertyInfo = {
            "link": prop_link,
            "address": prop_address,
            "price": prop_price,
            "attr": prop_attributes
        }

        allProperties.append(propertyInfo)

    return allProperties


'''
Rent.ie does not have a minimum / maximum number of bedrooms
Update code to do a web crawl as many times needed within the 
range of min / max bedrooms for rent.ie 
'''

def inputFilters(parameters):
    # Update to allow for choices of letting options
    # Update to allow for location changing
    url_params = ["houses-to-let/", "renting_dubllin/"]

    if parameters["min_beds"] != "None":
        url_params.append(parameters["min_beds"] + "_beds/")

    if parameters["min_price"] != "None":
        url_params.append("rent_" + parameters["min_price"])

    if parameters["max_price"] != "None":
        if parameters["min_price"] != "None":
            url_params.append("-" + parameters["max_price"] + "/")
        else:
            url_params.append(url_params + "rent_0-" + parameters["max_price"] + "/")
    else:
        url_params.append("/")

    return url_params
