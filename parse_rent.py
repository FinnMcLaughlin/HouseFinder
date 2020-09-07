import html_parser


def parse_html(filters):
    # Specified property website URL: Daft.ie
    property_url = "https://www.rent.ie/houses-to-let/renting_dublin/"

    filters.pop(0)

    for uFilter in filters:
        property_url = property_url + uFilter

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
