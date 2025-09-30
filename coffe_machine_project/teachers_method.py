MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, returns False if ingredients are not enough."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there isn't enough {item}")
            return False
    return True

def process_coins():
    print("Please insert coins:")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

def is_transaction_succesfull(money_received, drink_cost):
    """Return True when the payment is accepted, False if the money is not enough"""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is the ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Money is not enough. Money refunded.")
        return False
    

def make_coffee(drink_name, order_ingredients):
    """Deduc the required ingredients form the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")



power_on = True


while power_on:
    order = input("What would you like? (espresso/latte/cappuccino):")

    if order == "off":
        power_on = False
    elif order == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money $: {profit}")
    
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesfull(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"]) 


# profit is immutable because its int everytime there is a update we "change it"
# resources is mutable because it is dic and mutable i cry