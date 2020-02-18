# {}.format(parameter)
# print("format this string")
print("{}".format("format this string"))

fname = "prafful"
lname = "daga"
print("{}....{}".format(fname, lname))

#use format to align and give width to the output
print(format(fname, ">50s"))
print(format(fname, "<50s"))
#fill empty space with any character
print(format(fname, "$>50s"))
print(format(fname, "@<50s"))
print(format(fname, "$>50s"))
print(format(fname, "@^50s"))

#use integers with format strings
print("Score is {}". format(8))
print("Score is {}". format(88888))
print("Score is {:,}". format(88888))
print("Score is {:,}". format(888888888))
print("Score is {:15,} only". format(888888888))
print("Score is {:<15,} only". format(888888888))
print("Score is {:->15,} only". format(888888888))
print("Score is {:-<15,} only". format(888888888))
print("Score is {:-^15,} only". format(888888888))

#integer to binary
number = 0
print("Binary of 1 is {0:b}".format(number))
while(number <= 32):
    print("Binary for {0}: {1:b} Octal: {2:o} Hexadecimal: {3:x}".format(number, number, number, number))
    number+=1

#use format to access list and dictionary items!
language = ['python', 'django', 'java', 'node']
print("I love to work with ", language[0])
print("I love to work with {0[0]}". format(language))
print("Secure language is  {0[2]}". format(language))

friends= {"mohan": "chennai", "yuko": "japan"}
print("Mohan is from {0[mohan]} \nYuko is from {0[yuko]}". format(friends) )


