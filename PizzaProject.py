"""
Pizza Topping & Price List
Shelley Wilson
1-31-22

Project working with lists, inserting, removing, and sorting
"""

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
#sorts pizza in ascending order based on price
pizza_and_prices.sort()
#prints cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
#prints most expensive pizza
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
#removes most expensive pizza
pizza_and_prices.pop(-1)
#adds a new topping and price in correct order
pizza_and_prices.insert(3, [2.5, "peppers"]) 
print(pizza_and_prices)
#slices the lowest 3 pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)

