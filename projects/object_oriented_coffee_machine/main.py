from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()

menu = Menu()
list = menu.get_items()

coffee_maker = CoffeeMaker()








power_on = True

while power_on:

    pre_order = str(input(f"Please choose your coffee: {list}").lower())
 
    

    if pre_order == "off":
        power_on = False
    elif pre_order == "report":
        coffee_maker.report()
        money_machine.report()
    else: 
        order = pre_order

        object_order = menu.find_drink(order)
        check_resources = coffee_maker.is_resource_sufficient(object_order)
        check_payment = money_machine.make_payment(object_order.cost)
        


        if check_resources == True:
            if check_payment == True:
                coffee_maker.make_coffee(object_order)

                print("it fukn works")
