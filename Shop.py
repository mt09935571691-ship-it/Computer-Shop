product = {'mouse' : 25,
           "keyboard": 40,
            "headset": 35,
            "mousepad": 15,
            "webcam": 50,
            "flash": 12,
            "gamepad": 45,
            "microphone": 60
            }

def take_order(product):
    total = 0
    print('\n======= COMPUTER SHOP =======')

    name = input('Enter you name:\n')
    print(f'Wellcome to our shop {name}')

    print('\n======= ORDER MENU =======')

    for item,price in product.items():
        print(f'{item.title():<10} {price}')

    order = input('Enter your order:').lower().split()

    quantities = input('Enter quantities:').split()

    if len(order) != len(quantities):
        print('\nPlease enter one quantity for each item')
        return -1

    orders = {}

    for i in range(len(order)):
        item = order[i]

        if item in product:
            total += product[item] * int(quantities[i])
            orders[item] = int(quantities[i])

        else:
            print(f'Error"{item}"is not available in the menu')
            return -1

    print('\n====== RECEIPT ======')
    for item,quantity in orders.items():
        price = product[item]
        subtotal = quantity * price

        print(f'{item.title():<6} x{quantity} ${price}')
    print('-------------------------')
    print(f'Total: ${total}')
    return total


if take_order(product) != -1:
    print('\nYour order has been successfully placed')
else:
    print('\nYour order was not placed')