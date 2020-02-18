'''
nonname or anonymous functions
'''
def addNum(n1, n2):
    return n1 + n2

sum = addNum(4, 4)
print(sum)

#lambda way
message = lambda m: print(m)
print(message("Hello Lambda!"))

#lambda way
sum = lambda n1, n2: n1 + n2
print(sum(3,5))

squared = lambda n: n*n
print(squared(5))

#list of lambda functions (functions in collection)
lambdaList = [ lambda a: a**2, lambda a,b: a*b, lambda a,b: a+b]
print(lambdaList[0](8))
print(lambdaList[1](8, 5))
print(lambdaList[2](7,1))

#lambda with no parameters -> there has to be something to return 
noparacheck = lambda: True
print(noparacheck())