from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_menu = Menu()
my_money_machine = MoneyMachine()

while True:
    user_input = input(f"What would you like to order? {my_menu.get_items()}: ")
    if user_input == "report":
        my_coffee_maker.report()
        my_money_machine.report()
        continue
    elif user_input == "off":
        print("Device shutting down. Bye :)")
        exit()

    order = my_menu.find_drink(user_input)
    if not isinstance(order, MenuItem):
        continue

    if my_coffee_maker.is_resource_sufficient(order):
        is_payment_successful = my_money_machine.make_payment(order.cost)
        if is_payment_successful:
            my_coffee_maker.make_coffee(order)
        else:
            continue
    else:
        continue

