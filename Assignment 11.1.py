# DSC510-T301 Assignment 11.1
# Zachary Hill
# 18FEB2019
# Cash Register
#
# This program creates a CashRegister class for shopping at my hair care shop. It tracks number of items
# in the cart as well as total cost of the cart. With more time I think adding a cart contents method
# would be nice.

import locale

# Sets currency locale
locale.setlocale( locale.LC_ALL, 'en_US' )

# Lists available items and associated cost
items = {'hair gel': 4.50, 'shampoo': 3.00, 'conditioner': 3.50, 'hair spray': 4.00, 'purple hair dye': 18.00}

print('Welcome to Zach\'s Hair Care emporium!')

# Creates class for manipulating the shopping cart of the customer
class CashRegister:

    numItems = 0
    totalPrice = 0

    def __init__(self, item, cost):
        self.item = item
        self.cost = cost
        self.addItem(cost)

    # Adds items to cart, increments total number of items and total cost of cart with each item added
    def addItem(self, price):
        CashRegister.numItems += 1
        CashRegister.totalPrice = CashRegister.totalPrice + price
        pass

    # Gets total cost variable that was incremented by addItem
    def getTotal(self):
        return CashRegister.totalPrice
        pass

    # Gets total number of items added by addItem
    def getCount(self):
        return CashRegister.numItems
        pass

# Allows user to select product to add
def productSelect():
    itemsCount = {1: 'hair gel', 2: 'shampoo', 3: 'conditioner', 4: 'hair spray', 5: 'purple hair dye'}
    print('What products do you desire?')
    for key in itemsCount:
        print('{:<4s}{:<20s}{:>6s}'.format(repr(key), itemsCount[key], locale.currency(items[itemsCount[key]])))
    userSelect = input('Enter your selection: ')
    try:
        product = itemsCount[int(userSelect)]
        if product in items:
            return product
    except:
        print('Invalid Selection, please try again!')
        return productSelect()

# Requests whether user would like to add another item
def keepShopping(total, count):
    yes = ('yes', 'y', 'ya', 'si', 'ja', 'hai', 'ye')
    restart = input('Would you like to add another item?').lower()
    if restart in yes:
        main()
    else:
        print('-' * 30)
        print('You have', count, 'items in your cart.')
        print('Your cart will cost', locale.currency(total))
        print('Please proceed to checkout.')
        print('Thank you for shopping at Zach\'s Hair Care Emporium!')

        exit()


def main():
    choice = productSelect()
    shoppingCart = CashRegister(choice, items[choice])
    print('You have', shoppingCart.getCount(), 'items in your cart.')
    print('Your cart will cost', locale.currency(shoppingCart.getTotal()))
    keepShopping(shoppingCart.getTotal(), shoppingCart.getCount())


main()
