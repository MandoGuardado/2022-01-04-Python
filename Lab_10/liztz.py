cats = ["fluffy", "snowball", "garfield"]
# index    0          1           2
# reverse
# index   -3         -2          -1

# Note: with lists you can access indexes in reverse direction

print(cats)
print(0, cats[0], -3, cats[-3])  # fluffy
print(1, cats[1], -2, cats[-2])  # snowball
print(2, cats[2], -1, cats[-1])  # garfield

# list slicing
print("/n", cats)
print(cats[0:2])  # ["fluffy", "snowball"]
print(cats[1:])  # ["snowball", "garfield"]
print(cats[0::2])  # ["fluffy", "garfield"]
print(cats[-1::-1])  # ["garfield" ,"snowball", "fluffy"]

tigers = ["tony", "tiger king", "hobbes", "Sher Khan", "tigger"];

cats.append(tigers);

print(cats)  # ["fluffy", "snowball", "garfield" ,["tony", "tiger king", "hobbes", "Sher Khan", "tigger"] ]
# index           0         1            2                                3

print(cats[3])  # ["tony", "tiger king", "hobbes", "Sher Khan", "tigger"]
print(cats[3][1])  # 'tiger king'

lions = ["simba", "mufasa", "nala", "scar", "ghost", "darkness"]

big_cats = tigers.copy()
big_cats.extend(lions)
print(big_cats)

print(tigers)
fluffy_cats = tigers + lions
print(fluffy_cats)
