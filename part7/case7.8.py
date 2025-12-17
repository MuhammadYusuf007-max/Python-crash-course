sandwich_orders = ["mali", "tuna", "shiba", "tuba", "rupa"]
finished_sandwichs = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}")
    finished_sandwichs.append(sandwich)

for sandwich in finished_sandwichs:
    print(sandwich)
    