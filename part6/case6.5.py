rivers = {
    "nile":"Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China",
}
for river, country in rivers.items():
    print(f"The {river} runs throught {country}")
print()

for river in rivers.values():
    print(river)
print()

for country in rivers.keys():
    print(country)