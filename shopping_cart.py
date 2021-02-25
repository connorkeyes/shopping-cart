# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

import datetime
from datetime import date
import time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from dotenv import load_dotenv

load_dotenv()

for product in products:
    product["price_per"] = "item"

products.append({"id":21, "name": "Organic Bananas", "department": "fruits and vegetables", "aisle": "fruits", "price": 0.79, "price_per": "pound"})

taxRate = float(os.getenv("TAX_RATE", default = 0.0875))

motherProductIDList = []
for product in products:
    motherProductIDList.append(str(product["id"]))

lbsProductList = []
productIDList = []
productID = ""

print("Below, you are asked to enter a product ID. When you are finished, enter 'done'.")

while(str.casefold(productID) != str.casefold("Done")):
    productID = input("Please enter a product identifier:")
    if productID not in motherProductIDList and productID != str.casefold("Done"):
        print("Invalid entry. Please enter a valid product ID.")
        continue
    elif productID != str.casefold("Done"):
        productIDList.append(productID)
    for product in products:
        if product["price_per"] == "pound" and str(product["id"]) == productID:
            while(True):
                try:
                    numLbs = float(input("Please enter the number of pounds of " + product["name"] + ":"))
                    lbsProductList.append({"id": productID, "numLbs": numLbs})
                    break
                except:
                    print("Invalid entry. Enter an integer or float.")
                    continue

userProductList = []

for productID in productIDList:
    for product in products:
        if str(product["id"]) == productID:
            userProductList.append(product)

for product in userProductList:
    for lbsProduct in lbsProductList:
        if str(product["id"]) == lbsProduct["id"]:
            product["price"] = product["price"] * lbsProduct["numLbs"]

subtotal = 0

for product in userProductList:
    subtotal = subtotal + product["price"]

tax = float(subtotal) * taxRate

total = subtotal + tax

e = datetime.datetime.now() # helpful website to put time in attractive format: https://phoenixnap.com/kb/get-current-date-time-python

print("---------------------------------")
print("PADDY'S PUB GROCERIES")
print("WWW.PADDYSPUB.COM")
print("---------------------------------")
print("CHECKOUT AT:", date.today(), e.strftime("%I:%M:%S %p")) # used again: https://phoenixnap.com/kb/get-current-date-time-python
print("---------------------------------")
print("SELECTED PRODUCTS:")
for product in userProductList:
    print(" ...", product["name"], to_usd(product["price"]))
print("---------------------------------")
print("SUBTOTAL:", to_usd(subtotal))
print("TAX:", to_usd(tax))
print("TOTAL:", to_usd(total))
print("---------------------------------")
print("THANK YOU FOR SHOPPING AT PADDY'S PUB!")
print("---------------------------------")

fileName = time.strftime("%Y-%m-%d-%H-%M-%S") + ".txt"
rootDir = os.path.dirname(os.path.abspath("top_level_file.txt")) # I had to dig for this: https://www.kite.com/python/answers/how-to-get-the-path-of-the-root-project-structure-in-python#:~:text=dirname()%20to%20get%20the,top%20level%20of%20the%20project.
completeName = os.path.join(rootDir + "/receipts", fileName) # https://stackoverflow.com/questions/8024248/telling-python-to-save-a-txt-file-to-a-certain-directory-on-windows-and-mac/8024254
with open(completeName, "w") as file:
    file.write("---------------------------------\n")
    file.write("PADDY'S PUB GROCERIES\n")
    file.write("WWW.PADDYSPUB.COM\n")
    file.write("---------------------------------\n")
    file.write("CHECKOUT AT: " + str(date.today()) + e.strftime(" %I:%M:%S %p\n"))
    file.write("---------------------------------\n")
    file.write("SELECTED PRODUCTS:\n")
    for product in userProductList:
        file.write(" ... " + product["name"] + " " + to_usd(product["price"]) + "\n")
    file.write("---------------------------------\n")
    file.write("SUBTOTAL: " + to_usd(subtotal) + "\n")
    file.write("TAX: " + to_usd(tax) + "\n")
    file.write("TOTAL: " + to_usd(total) + "\n")
    file.write("---------------------------------\n")
    file.write("THANK YOU FOR SHOPPING AT PADDY'S PUB!\n")
    file.write("---------------------------------\n")

emailQuestion = input("Would you like to receive the receipt in your email? Yes/No: ")
if emailQuestion != str.casefold("yes"):
    print("Have a nice day!")
    exit()

userEmail = input("Please enter your email address: ")

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
client = SendGridAPIClient(SENDGRID_API_KEY)
subject = "Your Receipt from Paddy's Pub Groceries"

with open(completeName, "r") as file:
    contents = file.read()
    lines = contents.split("\n")

htmlListItems = ""

for line in lines:
    line = "<p>" + str(line) + "</p>"
    htmlListItems += line

html_content = f"""
<h3>Hello! Here is your receipt:</h3>
<ol>
    {htmlListItems}
</ol>
"""

message = Mail(from_email=SENDER_ADDRESS, to_emails=userEmail, subject=subject, html_content=html_content)

try:
    response = client.send(message)
    print("Your email receipt has been sent. Thanks again for shopping at Paddy's Pub!")

except:
    print("Unfortunately, something went wrong. Your receipt email could not be sent.")
    print("However, a copy of your receipt was still saved in the receipts folder.")
    print("Thanks again for shopping at Paddys Pub!")
