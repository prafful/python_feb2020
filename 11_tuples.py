sample = ()
print(type(sample))
#sample = (25, 65, 45)
sample = 25, 65, 45
print(sample)
sample = (25, 65, 45, [90, "check", 5.5])
print(sample)
sample = ((3,4,5,), (7,8,9), (1,9,0))
print(sample)
#((3, 4, 5), (7, 8, 9), (1, 9, 0))
print(sample[1][1])

#creating tuples from list and sets
scores = [25, 35, 45]
sample = tuple(scores)
print(sample)

scores = {25, 35, 45}
sample = tuple(scores)
print(sample)

onlyOne = 'omg'
# checkOne = tuple(onlyOne)
checkOne = (onlyOne,)
print(checkOne)
print(type(checkOne))

sample = (25, 65, 45, [90, "check", 5.5], 88, 'a', 'check', 55.5, 78)

#(65, 45, [90, 'check', 5.5])
print(sample[1:])
#(65, 45, [90, 'check', 5.5], 88, 'a', 'check', 55.5, 78)
print(sample[:5])
#(25, 45, 88)
print(sample[:5:2])

#tuple is immutable -> you cannot modify elements in the tuple
#                       but can assign a new tuple to same variable         

sample = (25, 65, 45)
print(sample[0])
#TypeError: 'tuple' object does not support item assignment
#sample[0] = 33
sample = (44, 85, 45)
print(sample)
vowel1 = ('a','e','i')
vowel2 = ('o','u')
vowel = vowel1 + vowel2
print(vovel)

#TypeError: 'tuple' object doesn't support item deletion
#del sample[0]
#print(sample)
#delete the given tuple
#del sample

for item in sample:
    print(item)