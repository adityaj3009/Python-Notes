# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia': 'Moscow',
            }

print(capitals['India'])    #here we dont use index number like 0,1,2...
print(capitals.get('Germany'))   #To check if a key word exist
print(capitals.keys())
print(capitals.values())
print(capitals.items())       #To print whole dictionary

#update method
capitals.update({'Germany': 'Berlin'})
capitals.update({'USA':'Las Vegas'})

for key, value in capitals.items():    #Also to print whole dictionary
    print(key, value)

capitals.pop('China')      #To remove a particular key
capitals.clear()            #To clear everthing