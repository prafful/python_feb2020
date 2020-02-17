#lists
mixed = [2, 4, 8, "prafful", 88.88, 44, 71, "daga", 'a']
print(mixed[4])
print(id(mixed))
# : operator
#slice from 3rd index position to (7-1)th position
newslice  = mixed[3:7]
print(newslice)
print(type(newslice))
#slice from negative direction
backslice = mixed[-4:-1]
print(backslice)
backslice1 = mixed[-5:]
backslice2 = mixed[-5::1]
print(backslice1)
print(backslice2)

#iterating through the list!
for item in mixed:
    print(item)
