resources = {
    'Water': 300,
    'Milk': 200,
    'Coffee': 100,
    'Money': 0.0
}

MENU = {
    'espresso': {
        'Water': 50,
        'Milk': 0,
        'Coffee': 18,
        'Money': 1.5
    },
    'latte': {
        'Water': 200,
        'Milk': 150,
        'Coffee': 24,
        'Money': 2.5
    },
    'cappuccino': {
        'Water': 250,
        'Milk': 100,
        'Coffee': 24,
        'Money': 3.0
    },
}


def print_current_resources():
    print(f"\nCurrent resources:\nWater: {resources['Water']}ml\n"
          f"Milk: {resources['Milk']}ml\n"
          f"Coffee: {resources['Coffee']}g\n"
          f"Money: ${resources['Money']}\n")


def check_resources(_input):
    order = MENU[_input]
    enough_water = resources['Water'] >= order['Water']
    enough_milk = resources['Milk'] >= order['Milk']
    enough_coffee = resources['Coffee'] >= order['Coffee']

    resource_stat = ""

    if not enough_water:
        resource_stat += "/Water"
    if not enough_milk:
        resource_stat += "/Milk"
    if not enough_coffee:
        resource_stat += "/Coffee"

    if enough_water and enough_milk and enough_coffee:
        return True
    else:
        print(f"Sorry, there is not enough {resource_stat}.")
        return False


def process_coins():
    print("Please enter coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)


def consume_resources(_input):
    resources['Water'] -= MENU[_input]['Water']
    resources['Milk'] -= MENU[_input]['Milk']
    resources['Coffee'] -= MENU[_input]['Coffee']


def get_user_input():
    _input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if _input == 'report':
        print_current_resources()
    elif _input == 'off':
        print("Coffee maker shutting down...")
        exit()
    elif _input == 'espresso' or 'latte' or 'cappuccino':
        enough_resources = check_resources(_input)

        if enough_resources:
            total_inserted_coins = process_coins()

            if total_inserted_coins < MENU[_input]['Money']:
                print("Sorry, that is not enough money. Money refunded.")
            else:
                if total_inserted_coins > MENU[_input]['Money']:
                    print(f"Here is ${str(round(total_inserted_coins - MENU[_input]['Money'], 2))} in change.")
                resources['Money'] += MENU[_input]['Money']
                consume_resources(_input)
                print(f"Here is your {_input}. Enjoy!")
        else:
            return 0


while True:
    get_user_input()
