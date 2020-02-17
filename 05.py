#integer
n1 = 5
print(str(n1) + " is of type " + str(type(n1)))

#floats
n2 = 5.5
print(str(n2) + " is of type " + str(type(n2)))

#lists
mixed = []
print(type(mixed))
mixed = [2, 5.5, 'a', 'B', "uber"]
print(type(mixed))
print(mixed)
print(mixed[0])
print("Length of list is: " + str(len(mixed)))
mixed[0]=4
print(mixed)


#tuple
nochange = ()
print(type(nochange))
nochange = (2, 5.5, 'a', 'B', "uber")
print(nochange)
print(nochange[0])
# below statement is illegal for tuple
#nochange[0] = 4

#strings
location = "chennai"

multiline = '''
            "hello " + " how "+
            " are " + " you?"
            '''
print(type(location))
print(len(location))
print(location[0])
print(multiline)


#sets
noorder  = {25, 35, 45, 80, 90}
print(type(noorder))
print(noorder)
#subscription is not possible in set!
#print(noorder[0])

#dictionary
keyvalue = {}
print(type(keyvalue))
keyvalue = { 1:"prafful", "tech":"python", 4:8, 9:"ML" }
print(keyvalue[1])
print(keyvalue["tech"])
print(keyvalue[4])
print(keyvalue[9])


#type conversion
n2 = 5
print(type(n2))
n3 =  float(n2)
print(type(n3))
n4 = str(n3)
print(type(n4))

#input - everything is string in input
score1 = input("Input score 1: ")
score2  = input("Input score 2: ")
print("Score is : " + score1 + score2)
print("####################################")
score1 = int(input("Input score 1: "))
score2  = int(input("Input score 2: "))


print("Score is : " + str(score1+score2))
print("Score is ", score1 )

