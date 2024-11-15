def cities_countries(city, country, population=None):
    if population:
        city_country = f"{city.title()}, {country.title()} - {population}"
    else:
        city_country = f"{city.title()}, {country.title()}"
    return city_country