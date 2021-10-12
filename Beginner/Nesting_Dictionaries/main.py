travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(new_country, times_visited, new_city ):
    new_dict = { "country": new_country, "visits": times_visited, "cities": new_city}
    travel_log.append(new_dict)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
