# w means write
# r = read a file
# a = append a file



text = "hieee\n this is some text \n have good one!"

with open('test.txt', 'a') as file:     
    file.write(text)
