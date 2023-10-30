from data import MENU
from data import resources
import math


def user_prompt():
    """Ask the user for a coffee choice. and returns True if user
    inputs 'report' to print a report.
    Returns False, if user inputs 'off' to turn off the machine. Finally,
    if not of previous choice were made,
    returns the user's coffee selection

    Returns:
        bool: True if user inputs 'report'
        bool False if user inputs 'off'
        str: 'espresso' or 'latte' or 'cappuccino'
    """
    user_input = input("What would you like? (espresso, latte, cappuccino): ")
    if user_input == "report":
        return True
    elif user_input not in ["espresso", "latte", "cappuccino"]:
        return False
    else:
        return user_input


def print_report(stock):
    """Prints the report of the stored ingresdients and money in the machine.

    Args:
        stock (dict): Contains the values of money and
        ingredientes stored in the machine.

    Returns:
        None
    """
    print(f"Water {stock['water']}ml")
    print(f"Milk {stock['milk']}ml")
    print(f"Coffee {stock['coffee']}gr")
    print(f"Money: ${stock['money']}")


def check_ingredients(coffee_info, usr_choice, stock):
    """Checks the availibility of ingredients in the machine.
    If doesn't have enough ingredients for a coffe, prints a message
    with missing engidient.

    Args:
        coffee_info (dict): Contains the information of all types of
        coffe, like how much water it needs, price, etc.
        usr_choice (str): Contains the coffee selection made by the user.
        stock (dict): COntains the amount of ingredients and money stored
        in the machine.

    Returns:
        bool: True if there are enough ingredients
        bool: False if there arent enough ingredients
    """
    for ingredient in coffee_info[usr_choice]['ingredients']:
        if stock[ingredient] < coffee_info[usr_choice]['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
        return True


def coins_input():
    """Asks the user to insert a number of coins of every
    type: quarters, dimes, nickels, pennies. Then returns the total
    amount of coins inserted

    Returns:
        float: Total amount of coins inserted by the user.
    """
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    t_quarters = 0.25 * quarters
    t_dimes = 0.10 * dimes
    t_nickels = 0.05 * nickles
    t_pennies = 0.01 * pennies
    total_money = t_quarters + t_dimes + t_nickels + t_pennies
    return round(total_money, 2)


def prepare_coffee(old_stock, coffee_info, usr_choice):
    """For all the ingredients, removes the amount needed to prepare
    the coffee selected by the user.

    Args:
        old_stock (dict): Contains the actual stock of the machine in a given
        time coffee_info (dict): Contains the information of all types of
        coffe, like how much water it needs, price, etc.
        usr_choice ([type]): Contains the coffee selection made by the user.

    Returns:
        dict: Updated value of ingredients in the machine after preparatiob of
        coffee.
    """
    for ingredient in coffee_info[usr_choice]['ingredients']:
        old_stock[ingredient] = old_stock[ingredient] - coffee_info[usr_choice]['ingredients'][ingredient]
    old_stock['money'] += coffee_info[usr_choice]['cost']
    return old_stock


def check_price(coffee_info, usr_choice, t_coins):
    """Checks if the coins inserted by the user are enough to buy the coffee.
    if not enough, prints "Sorry that's not enough money. Money refunded." and
    returns False
    else, return True, print and calculates change

    Args:
        coffee_info (dict): Dictionary with all coffees' information.
        usr_choice (str): Coffe selected by user.
        t_coins (float): Change returned to user if inserted more coins than

    Returns:
        bool: Return True if user inserted enough coins, else return False.
    """
    if coffee_info[usr_choice]['cost'] > t_coins:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif coffee_info[usr_choice]['cost'] == t_coins:
        return True
    else:
        change = round(t_coins - coffee_info[usr_choice]['cost'], 2)
        print(f"Here is your {usr_choice} \N{hot beverage}. Enjoy")
        print(f"Here is ${change} dollars in change.")
        return True


menu_info = MENU
reserves = resources


while True:
    coffee_selection = user_prompt()
    if isinstance(coffee_selection, bool)  and not coffee_selection:
        break
    elif isinstance(coffee_selection, bool) and coffee_selection:
        print_report(reserves)
        continue
    else:
        if not check_ingredients(menu_info, coffee_selection, reserves):
            continue
        else:
            usr_money = coins_input()
            if check_price(menu_info, coffee_selection, usr_money):
                reserves = prepare_coffee(reserves, menu_info, coffee_selection)
