from case11_1_2 import cities_countries

def test_cities_countries():
    city_country = cities_countries("Tashkent", "Uzbekistan")
    assert city_country == "Tashkent, Uzbekistan"
    
def test_cities_countries_population():
    city_country = cities_countries("Tashkent", "Uzbekistan", 5_000_000)
    assert city_country == "Tashkent, Uzbekistan - 5000000"