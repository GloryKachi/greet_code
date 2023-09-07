travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },

    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]


def add_new_items(country, visits, cities):
    new_country = {"country": country, "visits": visits, "cities": cities}
    travel_log.append(new_country)


add_new_items(country="Nigeria", visits=7, cities=["Lagos", "Abuja", "Aba"])
print(travel_log)
