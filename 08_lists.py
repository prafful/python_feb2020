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

#newlist = [iter for item in range(0, 5)]
#print(newlist)

providers = ["uber", "ola", "zoom", "riderz", "didi"]
firstProviders = [provider[0] for provider in providers]
print(firstProviders)
lengthOfEachItem  = [len(provider) for provider in providers]
print(lengthOfEachItem)
#in operator
print("uberz" in providers)
print('z' in "prafful")

#add items in two list
getx = [x+y for x in 'abc' for y in 'def']
print(getx)

#creating 2 dimensional list
print("adi " *4)
clone = [4]*3
# [4, 4 ,4]
print(clone)
'''
[
    [4,4,4],
    [4,4,4],
    [4,4,4]
]
'''
clone2 = [[4]*3]*3
print(clone2)

#list additions!

friends1 = ["Oma", "Oka", "Chia"]
friends2 = ["Pic", "Din", "Bek"]
friends3 = friends1 + friends2
print(friends3)

#OR

friends3 = friends1.extend(friends2)
print(friends3)

print(mixed)
print(mixed[0: 7: 3 ])

mixed.insert(0, 55)
print(mixed)
check = mixed.pop(0)
print(str(check)  + " popped from " + str(mixed))
print(mixed)

del mixed[0]
print(mixed)

del mixed
#print(mixed)

#create 2 d list using for
'''
[4]*3  -> range(0,2)
'''
#[[4, 4, 4], [4, 4, 4], [4, 4, 4]]
twoDimension = [ [4]*3 for a in range(0,3)]
print(twoDimension)
#[[0, 0, 0], [1, 1, 1], [2, 2, 2]]
#[[0, 0, 0], [1, 1, 1], [4, 4, 4]]
#[[0, 0, 0], [1, 1, 1], [8, 8, 8]]
twoDimension = [ [a]*3 for a in range(0,3)]
print(twoDimension)

twoDimension = [ [a**a]*3 for a in range(0,3)]
print(twoDimension)
 
twoDimension = [ [a**(a+1)]*3 for a in range(0,3)]
print(twoDimension)
