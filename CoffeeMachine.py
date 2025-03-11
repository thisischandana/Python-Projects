MENU ={
    "espresso" : {
        "ingredints":{
            "water": 50,
            "coffee": 18
    },
    "cost": 1.5

    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
      },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

resouces = {
    "water": 300,
    "milk" : 200,
    "coffee": 100,
}
"""
1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):” -- done
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.

"""
is_on = True


""" 2. Turn off the Coffee Machine by entering “off” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens."""
def resource_sufficient(order_ingredients):
    is_true = True
    for item in order_ingredients:
        if order_ingredients[item]>= resouces[item]:
            is_true = False
    return is_true

def process_coins():


while is_on:
    user_choice = input("“What would you like? (espresso/latte/cappuccino):")
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print("Water: 100ml")
        print("Milk: 50ml")
        print("Coffee: 76g")
        print("Money: $2.5")
    else:
        drink = MENU[user_choice]
        if resource_sufficient[drink["ingredients"]]:


"""3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5"""


