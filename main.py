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
def check_resources(ingredients: dict) -> bool:
    is_sufficient = True
    for item in ingredients:
        if ingredients.get(item) > resources.get(item):
            print(f"Sorry, there is not enough {item}.")
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
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_inserted < drink_value:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    if money_inserted >= drink_value:
        print("Transaction successful")
        if money_inserted > drink_value:
            print("Here is your exchange: ${:.2f}".format(money_inserted-drink_value))
        return True


# TODO: 7. Make Coffee
def deduct_from_resources(ingredients: dict):
    for item in ingredients:
        resources[item] -= ingredients.get(item)
    return


def make_coffee(choice: str):
    ingredients = MENU.get(choice).get("ingredients")
    deduct_from_resources(ingredients)
    print(f"Here is your {choice}!")
    return


while True:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    choice = input("What would you like? (espresso/latte/cappuccino):")
    match choice:
        case "espresso" | "latte" | "cappuccino":
            is_sufficient_resources = check_resources(MENU.get(choice).get("ingredients"))
            if is_sufficient_resources:
                coins_inserted = process_coins()
                is_sufficient_money = check_transaction(coins_inserted, MENU.get(choice).get("cost"))
                if is_sufficient_money:
                    make_coffee(choice)
                    resources["money"] += MENU.get(choice).get("cost")

        # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
        case "off":
            print("Shutting down the machine")
            break
        # TODO: 3. Print report.
        case "report":
            print(f'Water: {resources.get("water")}ml')
            print(f'Milk: {resources.get("milk")}ml')
            print(f'Coffee: {resources.get("coffee")}g')
            print('Money: ${:.2f}'.format(resources.get("money")))
        case _:
            print("Wrong option or typing error")
