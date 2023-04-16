from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

off = False
menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
while not off:
    choice = input(f"What would you link to drink? ({menu.get_items()}): ")
    if choice == "off":
        off = True
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink_requested = menu.find_drink(choice)
        if drink_requested is not None:
            if coffee_machine.is_resource_sufficient(drink_requested):
                if money_machine.make_payment(drink_requested.cost):
                    coffee_machine.make_coffee(drink_requested)
print("Turning off.")
