4.3.1.10 LAB: Convirtiendo el consumo de combustible


def liters_100km_to_miles_gallon(liters):
    # mile2km = 1.609344
    # galon2liter = 3.785411784
    
    liter2gallon = 0.264172
    km2mile = 0.621371    
    
    consum = liters * liter2gallon
    distance = consum * (100 * km2mile)
    return distance

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))
