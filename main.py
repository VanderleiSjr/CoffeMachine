MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}


# TODO: 4. Check resources sufficient?
def check_resources(ingredients:dict) -> bool:
    is_sufficient = True
    if ingredients.get("water") > resources.get("water"):
        print("Sorry, there is not enough water.")
        is_sufficient = False
    if ingredients.get("milk") and ingredients.get("milk") > resources.get("milk"):
        print("Sorry, there is not enough milk.")
        is_sufficient = False
    if ingredients.get("coffee") > resources.get("coffee"):
        print("Sorry, there is not enough coffee.")
        is_sufficient = False
    return is_sufficient


# TODO: 5. Process coins
def process_coins() -> float:
    print("Insert coins:")
    pennies = float(input("How many pennies?:"))
    nickles = float(input("How many nickles?:"))
    dimes = float(input("How many dimes?:"))
    quarters = float(input("How many quarters?:"))
    total = (pennies*0.01) + (nickles*0.05) + (dimes*0.10) + (quarters*0.25)

    return total


# TODO: 6. Check transaction successful?
def check_transaction(money_inserted, drink_value) -> bool:
    if money_inserted < drink_value:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    if money_inserted >= drink_value:
        print("Transaction successful")
        resources["money"] += drink_value
        if money_inserted > drink_value:
            print(f"Here is your exchange: ${float(round(money_inserted-drink_value, 2))}")
        return True


# TODO: 7. Make Coffee
def deduct_from_resources(water=0, milk=0, coffee=0):

    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee

    return


while True:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    choice = input("What would you like? (espresso/latte/cappuccino):")
    match choice:
        case "espresso":
            is_sufficient_resources = check_resources(MENU.get("espresso").get("ingredients"))
            if is_sufficient_resources:
                coins_inserted = process_coins()
                is_sufficient_money = check_transaction(coins_inserted, MENU.get("espresso").get("cost"))
                if is_sufficient_money:
                    ingredients = MENU.get("espresso").get("ingredients")
                    deduct_from_resources(ingredients.get("water"),
                                          ingredients.get("milk"),
                                          ingredients.get("coffee"))
                    print("Here is your espresso!")

        case "latte":
            is_sufficient_resources = check_resources(MENU.get("latte").get("ingredients"))
            if is_sufficient_resources:
                coins_inserted = process_coins()
                is_sufficient_money = check_transaction(coins_inserted, MENU.get("latte").get("cost"))
                if is_sufficient_money:
                    ingredients = MENU.get("latte").get("ingredients")
                    deduct_from_resources(ingredients.get("water"),
                                          ingredients.get("milk"),
                                          ingredients.get("coffee"))
                    print("Here is your latte!")
        case "cappuccino":
            is_sufficient_resources = check_resources(MENU.get("cappuccino").get("ingredients"))
            if is_sufficient_resources:
                coins_inserted = process_coins()
                is_sufficient_money = check_transaction(coins_inserted, MENU.get("latte").get("cost"))
                if is_sufficient_money:
                    ingredients = MENU.get("cappuccino").get("ingredients")
                    deduct_from_resources(ingredients.get("water"),
                                          ingredients.get("milk"),
                                          ingredients.get("coffee"))
                    print("Here is your cappuccino!")

        # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
        case "off":
            print("Shutting down the machine")
            break
        # TODO: 3. Print report.
        case "report":
            print(f'Water: {resources.get("water")}ml')
            print(f'Milk: {resources.get("milk")}ml')
            print(f'Coffee: {resources.get("coffee")}g')
            print(f'Money: ${resources.get("money")}')
        case _:
            print("Wrong option or typing error")
