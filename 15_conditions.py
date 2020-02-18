'''
if expression:
    pass

if condition:
    pass
else:
    pass

'''
number = int(input("Input number: "))
if (number >30):
    print("Number is more than 30")
else:
    print("Something else!")    

numbers = [1,2,3,4,5,6,7,8,9,10]
number = int(input("Input number: "))

if(number in numbers):
    print("present")
else:
    print("absent")

friends1 = ["ola", "uber", "didi", "mave", "ride"]
friends2 = ["ride", "jia", "didi", "zoom"]    

for f in friends1:
    if f in friends2:
        print("Common friend: ",  f)