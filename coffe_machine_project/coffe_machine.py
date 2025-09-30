from data_list import MENU
from data_list import resources

COFFEE_MENU = MENU
power_on = True
conversion_rate = [0.25, 0.10, 0.05, 0.01]


# TODO recipes can stay global-fix but resources should be local and should change without reseting


# TODO take the request


def required_ingredients(drink):
    required_drink = MENU[drink]
    required_water = float(required_drink["ingredients"]["water"])
    required_coffee = float(required_drink["ingredients"]["coffee"])
    required_price = float(required_drink["cost"])
    if required_drink == "espresso":
        required_milk = float(0)
    else:
        required_milk = float(required_drink["ingredients"]["milk"])
    return required_water, required_milk, required_coffee, required_price, required_drink

def coin_conversion(coins, rated):
    a = coins["quarters"] * rated[0]
    b = coins["dimes"] * rated[1]
    c = coins["nickels"] * rated[2]
    d = coins["pennies"] * rated[3]
    return a + b + c + d


# def price_check ():
#     if coin_conversion(conversion_rate) > required_price:
#         return True


def coffe_machine():

    while power_on:

        order = str(input("What would you like? (espresso/latte/cappuccino):").lower())
        required_ingredients(order)
        required_water, required_milk, required_coffee, required_price, required_drink = required_ingredients(order)

        coins = {}
        coin_types = ["quarters", "dimes", "nickels", "pennies"]

        for coin in coin_types:
            coins[coin] = int(input(f"How many {coin}"))

        sum_of_purse = coin_conversion(coins, conversion_rate)

        if required_water <= resources["water"]:
            if required_coffee <= resources["coffee"]:
                if required_milk <= resources["milk"]:
                    if required_price <= sum_of_purse:
                        print(f"Your coffee is being prepared. Here is the change{sum_of_purse - required_price}")
                        resources["water"] - required_water
                        resources["coffee"] - required_coffee
                        resources["milk"] - required_milk
                    else:
                        print(f"Insufficient funds. Here is the refund: {sum_of_purse}")
                else:
                    print("Not enough Milk!")
            else:
                print("Not enough coffe!")
        else:
            print("Not enough water!")

    # TODO machine should have a "off" button
    # TODO "report" should print out resources
    # TODO Make a coin system. quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    # TODO When the user chooses a drink, the program should check if there are enough resources to make that drink
    # TODO After the user chooses a drink, let them put in coins. Then check if there are enough coins
    """May be a in transaction window where the return is True it follows through with the procedure if not 'refunds' """
    # TODO If the transaction is True, then remove resources and add the money

while input("Do you want coffe? 'y' or 'n'") == 'y':
    coffe_machine()
else: power_on = False

