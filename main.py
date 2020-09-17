import parse_daft
import parse_rent
from tkinter import *
from tkinter.ttk import *

window_h = 200
window_w = 350
max_price = 7500
max_bedrooms = 5


def getValues():
    params = {
        "min_price": min_price_menu.get(),
        "max_price": max_price_menu.get(),
        "min_beds": min_bedrooms_menu.get(),
        "max_beds": max_bedrooms_menu.get()
    }

    results = parse_rent.parse_html(parse_rent.inputFilters(params))

    results += parse_daft.parse_html(parse_daft.inputFilters(params))

    for property in results:
        print(property["link"] + "\n" + property["address"] + "\n" + property["price"])

        for attr in property["attr"]:
            print(attr)

        print("\n")

    showResults(results)


def clearScreen():
    for lbl in labels:
        lbl.destroy()

    for wgt in widgets:
        wgt.destroy()


def showResults(results):
    root.geometry("500x500")

    clearScreen()

    Label(root, text="Result", font=30).grid(row=0, column=0)

    rowNo = 1

    for res_prop in results:
        Label(root, text=res_prop["link"], cursor="hand2").grid(row=rowNo, column=0)
        Label(root, text=res_prop["address"]).grid(row=rowNo+1, column=0)
        Label(root, text=res_prop["price"]).grid(row=rowNo+2, column=0)

        attrIndex = rowNo+4
        for attr in res_prop["attr"]:
            Label(root, text=attr).grid(row=attrIndex, column=0)
            attrIndex += 1

        rowNo = attrIndex


root = Tk()

root.title("House Finder GUI")
root.geometry("350x250")

title_lbl = Label(root, text="House Finder")
title_lbl.grid(row=0, column=0)

labels = [
    Label(root, text="Minimum Price"),
    Label(root, text="Maximum Price"),
    Label(root, text="Min No. Bedrooms"),
    Label(root, text="Max No. Bedrooms")
]

rowNo = 1
for label in labels:
    label.grid(row=rowNo, column=0)
    rowNo += 2

labels.append(title_lbl)

prices = []

for price in range(0, max_price, 500):
    prices.append(price)

prices[0] = "None"

min_price_menu = Combobox(root)
max_price_menu = Combobox(root)

min_price_menu["values"] = prices
min_price_menu.current(0)

max_price_menu["values"] = prices
max_price_menu.current(0)

min_bedrooms_menu = Combobox(root)
max_bedrooms_menu = Combobox(root)

bedrooms = []

for bed in range(0, max_bedrooms + 1):
    bedrooms.append(bed)

bedrooms[0] = "None"

min_bedrooms_menu["values"] = bedrooms
min_bedrooms_menu.current(0)

max_bedrooms_menu["values"] = bedrooms
max_bedrooms_menu.current(0)

runButton = Button(root, text="Run", command=getValues)

widgets = [
    min_price_menu,
    max_price_menu,
    min_bedrooms_menu,
    max_bedrooms_menu,
    runButton
]

rowNo = 2
colNo = 1

for widget in widgets:
    widget.grid(row=rowNo, column=colNo)
    rowNo += 2

root.mainloop()
