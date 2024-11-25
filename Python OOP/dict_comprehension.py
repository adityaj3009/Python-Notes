# dictionary comprehension = create dictionaries using an expression
#                             can replace for loops and certain lambda function
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if condition}
# dictionary = {key: (if/else) for (key,value) in iterables}
# dictionary = {key: function(value) for (key,value) in iterables}

cities_temp_F = {'new york': 32, 'boston':75, 'LA':100, 'chicago':50}

cities_temp_C = {key: round((value-32)*(5/9)) for(key,value) in cities_temp_F.items() }
print(cities_temp_C)

print("-------------------------------")

weather = {'new york': "sunny", 'boston': "sunny", 'LA': "cloudy", 'chicago':"moist"}
sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
print(sunny_weather)

print("--------------------------------")

cities = {'new york': 32, 'boston':75, 'LA':100, 'chicago':50}
desc_cities = {key: ("warm" if value >=40 else "cold") for (key,value) in cities.items()}
print(desc_cities)

print("--------------------------------")

def check_temp(value):
    if value >=70:
        return "warm"
    else:
        return "cold"

cities = {'new york': 32, 'boston':75, 'LA':100, 'chicago':50}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)





