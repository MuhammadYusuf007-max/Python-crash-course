pizzas = ["Pepperonni", "Mushroom", "Spagetti"]
friend_pizza = pizzas[:]
pizzas.append("italian")
friend_pizza.append("americano")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print()

print("my friends' favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)