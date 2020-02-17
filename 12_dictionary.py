newDict = {}
print(type(newDict))

score = {1:"monday", "bigday":"tuesday", 'a':"wednesday", "friends":["ama", "chia", "pia"]}
print(score["bigday"])
print(score["a"])
print(score["friends"])

#create dictionary from list of tuples
friends = dict([("chennai",8), ("mumbai",7), ("ahmedabad", 2)])
#{'chennai': 8, 'mumbai': 7, 'ahmedabad': 2}
print(friends)

print(friends["chennai"])
print(friends.get("mumbai"))

friends.update({'mumbai':18})
print(friends)

#iterate through dictionary
for key, value in friends.items():
    print(key,  ": ", value)

# create a dictionary where key is string 
# and value is length of string from the 
# list strings!

friends = ['amar', 'akbar', 'antony', 'tiger', 'lion']
# somedict = { 'amar': 4, 'akbar':5, 'antony':6, 'tiger':5, 'lion':4}

somedict = {value:len(value)  for value in friends}
print(somedict)















