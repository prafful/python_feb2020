"""
Reduce -> Aggregator functions!
1. It works with iterable
2. It will return single value!

"""
from functools import reduce

numbers = [1,2,3,4,5]
#         [3    ,3,4,5]
# #       [6    ,4,5]  
#         [10    ,5]
#         [15]    
total = reduce( lambda n1, n2: n1+n2, numbers)
print(total)


numbers = [ 55, 45, 65, 85, 22, 13, 5, 88, 78]
largest = reduce(lambda a, b: a if a>b else b, numbers)
print(largest)

numbers = [ 5, 15, 10, 8, 2, 3, 6, 18, 7]
#numbers = [5, 6, 11]
# 25 + 36
# 61
#Assignment 1: 
#Find the sum of square of all numbers less than 10
#Assignment 2: 
#Find the sum of square of all even numbers 

#Assignment 1

def function1(a, b):
    return a+b

def function2(c):
    return c*c

def function3(d):
    if d<10:
        return True
    else:
        return False 

#non-lambda way           
sum = reduce(function1, map(function2, filter(function3, numbers)))
print(sum)
#lambda way
sum =  reduce( lambda a, b: a+b  , map( lambda a: a*a , filter(lambda n1: n1<10, numbers)))
print(sum)
