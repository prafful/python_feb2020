'''for loops'''
vowels = "aeiou"
for v in vowels:
    print(v)


numbers = [1,2,3,4,5,6,7,8,9,10]
total = 0
for n in numbers:
    total += n
print("Sum of all in list of 1 to 10: ", total)

#using form loop with range!
for n in range(1,5):
    print(n, end =" ")
    #print(n,)
    #print(n),
print()    
for n in range(1,10, 2):
    print(n, end =" ")

#for else loop
# else will execute only if loop is finished with all iterations
for n in numbers:
    print(n**n )
else:
    print("Exponent for all numbers is done!")

# in below case else will not execute as loop is breaking in between!
for n in numbers:
    print(n**n )
    if(n == 7):
        break
else:
    print("Exponent for all numbers is done!")    
    