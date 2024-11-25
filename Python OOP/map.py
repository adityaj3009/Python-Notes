# map() = applies a function to each item in an iterable (lists, tuple, etc..)
#
# map(function, iterable)

store = [("shirts", 20.00),
         ("pant", 25.00),
         ("jacket",50.00),
         ("socks", 10.00)]

# Conversion rates
usd_to_inr_rate = 83.44
inr_to_usd_rate = (1 /usd_to_inr_rate)

# Conversion lambdas
to_inr = lambda data: (data[0], data[1] * usd_to_inr_rate)
to_dollars = lambda data: (data[0], data[1] * inr_to_usd_rate)
to_euro = lambda data: (data[0], data[1]*0.82)


store_inr = list(map(to_inr, store))  # Here to_inr is a function, and store is iterables
print("Prices in INR:")
for i in store_inr:
    print(i)

print("------------------------------")

store_dollar = list(map(to_dollars,store_inr)) 
print("Prices back in USD:")
for i in store_dollar:
    print(i)

print("------------------------------")

to_euro = list(map(to_euro,store))
print("Prices in Euro: ")
for i in to_euro:
    print(i)