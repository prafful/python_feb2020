
'''
def funcname(parameter_list):
    pass

'''
counter = 10

def customMessage(message):
    global counter
    if(counter > 0):
        print(message)
        counter -= 1
        customMessage(message)

customMessage("Hello ")

def addAll(n):
    if n!=0:
        return n + addAll(n-1)
    else:
        return 0     

# 10 ^^ 4
number = int(input("Input Number: "))
print(addAll(number))