cities = {
    "Bukhara":{
        "location": "Uzbekistan",
        "population": 1.9,
        "fact": "it ishomeland of Imam Bukhary"
    },
    "Istanbul":{
        "location": "Turkey",
        "population": 32,
        "fact": "city is conqured by Muhammad Fotih"
        },
    "Madina":{
        "location": "Saudia Arabia",
        "population": 7,
        "fact": "Muhammad Sollallohu alayhi va sallam lived there"
    }
}
for city, information in cities.items():
    print(f"\n{city} is located {information['location']} with {information['population']} million people \nand the interesting thing about it is {information['fact']}")
    
    