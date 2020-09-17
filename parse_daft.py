import html_parser


def parse_html(filters):
    # Specified property website URL: Daft.ie
    property_url = "https://www.daft.ie/"

    for uFilter in filters:
        property_url = property_url + uFilter

    page_soup = html_parser.parseHTML(property_url)

    # Stores all property item containers
    prop_containers = page_soup.findAll("div", {"class": "PropertyCardContainer__container"})

    # Array to store dictionaries containing information on each property
    allProperties = []

    # Extracts the relevant information (link to property URL, property address, price attributes etc.)
    # Prints them to the console
    for container in prop_containers:

        prop_link = "https://www.daft.ie/" + container.a["href"]
        # print(prop_link)

        prop_address = container.findAll("div", {"class": "PropertyInformationCommonStyles__addressCopy calculate-truncation-plugin"})[0].text.strip()
        # print(prop_address)

        prop_price = container.findAll("div", {"class": "PropertyInformationCommonStyles__propertyPrice"})[0].text.strip()
        # print(prop_price)

        prop_attr = container.findAll("div", {"class": "QuickPropertyDetails__iconContainer"})
        prop_attributes = []

        for attr in prop_attr:
            prop_attributes.append(attr.img["alt"])

        propertyInfo = {
            "link": prop_link,
            "address": prop_address,
            "price": prop_price,
            "attr": prop_attributes
        }

        allProperties.append(propertyInfo)

        # print("\n")

    return allProperties

def inputFilters(parameters):
    # Update to allow for choices of letting options
    # Update to allow for location changing
    # 3rd entry is necessary in the url to show newest results
    url_parameters = ["dublin-city/", "apartments-for-rent/", "?s%5Bignored_agents%5D%5B0%5D=1551&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d"]

    if parameters["min_price"] != "None":
        print("min_price: " + parameters["min_price"])
        url_parameters.append("&s%5Bmnp%5D=" + parameters["min_price"])

    if parameters["max_price"] != "None":
        print("max_price: " + parameters["max_price"])
        url_parameters.append("&s%5Bmxp%5D=" + parameters["max_price"])

    if parameters["min_beds"] != "None":
        print("min_beds: " + parameters["min_beds"])
        url_parameters.append("&s%5Bmnb%5D=" + parameters["min_beds"])

    if parameters["max_beds"] != "None":
        print("max_beds: " + parameters["max_beds"])
        url_parameters.append("&s%5Bmxb%5D=" + parameters["max_beds"])

    return url_parameters
