from tkinter import *
from tkinter.ttk import *

window_h = 200
window_w = 350
max_price = 7500
max_bedrooms = 5


def run():
    def getValues():
        print(min_price_menu.get())
        print(max_price_menu.get())
        print(min_bedrooms_menu.get())
        print(max_bedrooms_menu.get())

    root = Tk()

    root.title("House Finder GUI")
    root.geometry("350x250")

    Label(root, text="House Finder").grid(row=0, column=0)
    Label(root, text="Minimum Price").grid(row=1, column=0)
    Label(root, text="Maximum Price").grid(row=3, column=0)
    Label(root, text="Min No. Bedrooms").grid(row=5, column=0)
    Label(root, text="Max No. Bedrooms").grid(row=7, column=0)

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

    min_price_menu.grid(row=2, column=1)
    max_price_menu.grid(row=4, column=1)
    min_bedrooms_menu.grid(row=6, column=1)
    max_bedrooms_menu.grid(row=8, column=1)

    Button(root, text="Run", command=getValues).grid(row=9, column=1)

    root.mainloop()
