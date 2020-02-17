#sets will not have duplicated
number_set = {5, 10, 5, 15, 20, 5, 15}
print(number_set)
# error - TypeError: unhashable type: 'list'
#mixed_type = { 4,5,6,7, [55, 44, 77]}

mixed_type = { 4,5,6,7, (55, 44, 77)}
print(mixed_type)

number_list = [ 4 , 5 , 5 , 88 , 88 , 77]
number_set = set(number_list)
#{88, 77, 4, 5}
print(number_set)

#add item to set
number_set.add(12)
print(number_set)
number_set.add(77)
print(number_set)

#remove item from set
number_set.remove(12)
print(number_set)
# will throw key error as 100 is not present!
#number_set.remove(100)
#print(number_set)
number_set.discard(77)
print(number_set)

#pop item from set
print(number_set.pop())

#unions and intersections
score1 = {58,68,78,88}
score2 = {18,28,38,48}
print(score1.union(score2))

score1 = {18,68,48,88}
score2 = {18,28,38,48}
print(score1.intersection(score2))

# substration/difference
# those elements of score1 which are not in score2
print(score1)
print(score2)
print("score1 - score2: ", score1 - score2)
# those elements of score2 which are not in score1
print("score1 - score2: ", score2 - score1)

for s in score1:
    print(s in score1)

#print( 28 in score1)  

#number_set.clear()
print(number_set)
number_set.add(44)
print(number_set)


freeze = frozenset(number_set)
#cannot modify the frozen set
#freeze.add(33)