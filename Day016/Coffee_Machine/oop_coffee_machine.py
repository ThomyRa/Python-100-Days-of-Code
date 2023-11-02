from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()
coffee_maker = CoffeeMaker()
machine_menu = Menu()
money_transaction = MoneyMachine()

is_on = True
while is_on:
    user_choice = input(f"What would you like? ({coffee_menu.get_items()}): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()  
        money_transaction.report() 
    else:
        user_order = machine_menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(user_order) and \
            money_transaction.make_payment(user_order.cost):
            coffee_maker.make_coffee(user_order)
