import parse_daft
import inputFilters

userFilters = inputFilters.getInput()
parse_daft.parse_html(userFilters)

