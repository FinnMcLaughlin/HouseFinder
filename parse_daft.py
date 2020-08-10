import html_parser


def parse_html(filters):
    # Specified property website URL: Daft.ie
    property_url = "https://www.daft.ie/dublin-city/" + filters[0] + "/?s%5Bignored_agents%5D%5B0%5D=1551&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d"

    filters.pop(0)

    for uFilter in filters:
        property_url = property_url + uFilter

    page_soup = html_parser.parseHTML(property_url)

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
