first = "This i my first string"
second = 'This is my second string'
third = 'This is my "third" string'
# delimiters

# bad = "this has a "double quotes" in it"
better = "This one also has a \"double quote\" in it\n"
best = 'This is the best way to "double quote" something in python'

print(best)
best_upper = best.upper()
print(best_upper)
print(best)

paragraph = first + second + third
print(paragraph)

pretty_para = first + ".  " + second + ".  " + third + "."
print(pretty_para)

name = "fluffy"
age= 7
color = "white"

# concatenation
mycat = "My cat is named " + name + " and is the color " + color + " and is " + str(age) + " years old."
print(mycat)

# f-string
yourcat = f"Your cat is named {name} and is the color {color} and is {age} years old. "
print(yourcat)

bdaycat = f"YOur cat is named {name} ans is the color {color} and just turned {age + 1} years old."
print(bdaycat)

# format method
hiscat = "His cat is name {} ans is the color {} ans is {} years old.".format(name, color, age)
print(hiscat)

cats = ["fluffy", "snowball", "garfield"]
kitty = "My cats are: {}, {}, and {}".format(*cats)
print(kitty)

diff_order = "My cats are: {2}, {2}, and {0}".format(*cats)
print(diff_order)



# doc string

"""
This 'is'
a "multiline"
comment.
"""

movie = "   Bladerunner the movie wins   "
print(movie)
print(movie[4:12])
print(movie[0])
print(movie[::2])
print(movie[-1::-1])

# remove whitespace
print(movie.strip(), end="***\n")

print(movie.split('e'))

# remove whitespace and split into a list based on str
split_movie = movie.strip().split('e')
print(split_movie)

print('E'.join(split_movie))