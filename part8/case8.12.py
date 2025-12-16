def make_sandwichs(*items):
    print("your sandwich are ordered With:")
    for i in items:
        print(f"\t- {i}")

make_sandwichs("mushroom", "sausage", "extra cheese")