def make_car(manufacturer, car_model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['car_model'] = car_model
    return kwargs

car = make_car("GM", "lacetti", color='blue', seats=4)
print(car) 