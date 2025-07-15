## ☕ Coffee Machine Simulation – Python CLI Project
# 📌 Overview
This project is a command-line based coffee machine simulation built in Python. It allows users to order drinks like Espresso, Latte, and Cappuccino by checking available resources, handling coin transactions, and dispensing coffee with real-time updates to inventory.

# 🎯 Features
✅ Interactive CLI for ordering drinks

✅ Resource check before making a beverage

✅ Coin-based payment simulation (quarters, dimes, nickels, pennies)

✅ Handles change and refunds

✅ Displays live inventory report (water, milk, coffee)

✅ Supports "off" command to turn off the machine

# 🧃 Menu & Pricing
Drink	Ingredients (ml/g)	Cost ($)
Espresso	50 water, 18 coffee	1.5
Latte	200 water, 150 milk, 24 coffee	2.5
Cappuccino	250 water, 100 milk, 24 coffee	3.0

# 🛠️ Code Highlights
1. is_resources_sufficient()
Checks if there are enough resources (water, milk, coffee) to make the selected drink.

2. process_coins()
Simulates inserting coins. Asks user for number of:

Quarters (0.25)

Dimes (0.10)

Nickels (0.05)

Pennies (0.01)

3. is_transaction_successful()
Validates if enough money was inserted. Returns change or refunds money if insufficient.

4. make_coffee()
Deducts resources from inventory and confirms drink is ready.

5. Main Loop
Handles user input (espresso, latte, cappuccino, report, or off) and calls appropriate functions.

# 📋 Example Interaction
What would you like to have? Espresso/Latte/Cappuccino: latte
Please insert coins
Enter no of quarters: 10
Enter no of dimes: 0
Enter no of nickels: 0
Enter no of pennies: 0
Your transaction is successful. Please collect your change 0.0$
Here is your latte ☕️
