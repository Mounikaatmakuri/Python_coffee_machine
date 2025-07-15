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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit =0
def is_resources_sufficient(choice_ingredients):
    for a in choice_ingredients:
        if choice_ingredients[a] >= resources[a]:
            print(choice_ingredients[a])
            print(resources[a])
            print('Sorry not enough resources to make the order')
            return False
    return True

def process_coins():
    print('Pleas insert coins')
    total = int(input('enter no of quarters'))*0.25
    total += int(input('enter no of dimes')) * 0.10
    total += int(input('enter no of nickles')) * 0.05
    total += int(input('enter no of pennies')) * 0.01
    return total

def is_transaction_successfull(money_received,order_cost):
    if money_received >= order_cost:
        change = round((money_received - order_cost),2)
        global profit
        profit += money_received
        #print(f'Here is the change {change}$')
        print(f'Your transaction is successful. Please collect your change {change}$')
        return True
    else:
        print('Sorry not enough coins to buy a beverage.Money refunded')
        print(f'Your transaction is successful. Please collect your {choice}')
        return False

def make_coffee(choice_ingredients,drink_name):
    for b in choice_ingredients:
        resources[b] -= choice_ingredients[b]
    print(f'Here is your {choice}☕️')

is_game = True
while is_game:
    choice = input("What would you like to have? Espresso/Latte/Cappuccino").lower()
    if choice == "off":
        is_game = False
    elif choice == "report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}ml")
    else:
        drink=MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successfull(payment,drink['cost']):
                make_coffee(drink['ingredients'],choice)


