def getInput():

    filters = []
    print("Filters\n-------------")

    prop_type = input("What type of property:\n(0)Any\n(1)Apartment\n(2)House\n--> ")
    if prop_type == "1":
        filters.append("apartments-for-rent")
    elif prop_type == "2":
        filters.append("houses-for-rent")
    else:
        filters.append("residential-property-for-rent")

    min_price = input("Enter minimum price: ")
    if len(min_price) > 0:
        filters.append("&s%5Bmnp%5D=" + min_price)

    max_price = input("Enter maximum price: ")
    if len(max_price) > 0:
        filters.append("&s%5Bmxp%5D=" + max_price)

    min_bed = input("Enter minimum beds: ")
    if len(min_bed) > 0:
        filters.append("&s%5Bmnb%5D=" + min_bed)

    max_bed = input("Enter maximum beds: ")
    if len(max_bed) > 0:
        filters.append("&s%5Bmxb%5D=" + max_bed)

    if len(filters) > 0:
        for uFilter in filters:
            print(uFilter)

    print("\n\n")
    return filters
