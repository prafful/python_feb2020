# Map will work only on iterables!
# It will return the list created by lambda/named function 
# Lambda function works on parameter (one of the item in iterables) of map 

messages = ['Help', 'Run', 'Fight', 'Request']

for m in messages:
    print("Current message is : ", m)

def printMessage(msg):
    #print("message from function is "+ msg)
    return "message from function is "+ msg


mapcheck = map(printMessage, messages)    
print(list(mapcheck))

#working with map and lambda!
mapcheck = map(lambda m: "lambda map " + m , messages)  
print(id(mapcheck))
newlist = list(mapcheck)  
print(type(list(mapcheck)))
print(id(mapcheck))
print(newlist)
print(list(mapcheck))

#mapcheck is becoming empty list after type check as list constructor is being used!!!!

scores1 = [25, 35, 45]
scores2 = [10, 15, 20]
scores3 = [2, 3, 4]

#scores3 = sum of each respective item at respective index position in 
# scores1 and scores2  

scores3 = map(lambda n1, n2, n3: (n1+n2)*n3 , scores1, scores2, scores3)
print(list(scores3))

# consider a scenario with list of different length!
scores1 = [20, 30, 40, 50, 60]
scores2 = [10, 20, 30, 40]
scores3 = [2, 3, 4]

#scores3 = sum of each respective item at respective index position in 
# scores1 and scores2  

scores3 = map(lambda n1, n2, n3: (n1+n2)*n3 , scores1, scores2, scores3)
print(list(scores3))


messages = ['Help', 'Run', 'Fight', 'Request']
# create a 2 d list of characters in messages
#[['H','e','l','p'], ['R','u','n']....]

print(list(map(list, messages)))