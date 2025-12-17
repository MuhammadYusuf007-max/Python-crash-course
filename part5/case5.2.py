car = 'AUDI'
print("Is car is bmw?")
print(car.lower() == 'bmw')

print("\nCar is not equal to honda")
print(car != 'honda')

age = 20
print(age == 32)
print(age != 24)
print(age > 22)
print(age<23)
print(age>=18)
print(age<=20)

gf_age = 18

if age >= 20 and gf_age > 18:
    print("We are ready for marriage")
else:
    print("We are not ready.")
    
if age > 18 or gf_age >18:
    print("okey")
else:
    print("No")