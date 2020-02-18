"""
File IO

1. Open the  file in specific mode.
2. It will return filehandle.
3. Use the filehandle to do file operations (read, write, change, delete, change attributes)
4. Close the filehandle
"""

fh = open("01.py", "r")
print(fh.name)
print(fh.mode)
print(fh.closed)
fh.close()
print(fh.closed)

print("-----------------------------------------------------")


with open("01.py", "r") as fh:
    print(fh.name)
    print(fh.mode)
    print(fh.closed)
print(fh.closed)

#open the file in write mode and write data to the same

with open("python.txt", "w") as fh:
    fh.write("Hello from python! \n")
    fh.write("In a new line! \n")
    fh.write("-------------------------------------- \n")
fh = None
#print(fh.name)
#fh.write("tryto write!")    

#open file in append mode and append data to the same

with open("python.txt", 'a') as fh:
    fh.write("Hello again from Python \n")    
    fh.write("Next is fun!")

#open file in read mode and write to the console    
with open("python.txt", "r") as fh:
    content = fh.readlines()
    print(content)
    for eachline in content:
        print(eachline)

#read data from file in chunk size
with open("python.txt", "r") as fh:
    content1 = fh.read(10)
    content2 = fh.read(10)
    content3 = fh.read(10)
    print(content1)
    print(content2)
    print(content3)
    print(fh.tell())
    #seek(how much do I want to seek, from where)
    #possible values of from where
    # 0 -> pointer shift will start from beginning of file!
    # 1 -> pointer shift will start from current offset!
    # 2 -> EOF will be the current offset!

    fh.seek(11, 0)
    print(fh.tell())
    print(fh.read(7))
    print(fh.tell())
    #fh.seek(11, 1)
    #print(fh.read(7))

#copy data from one file to another
with open("python.txt", "r") as fh:
    content = fh.readlines()
    tempfh = open("python1.txt", "w")
    for eachline in content:
        tempfh.write(eachline)
    tempfh.close()    

#copy data from one image to another
with open("eclipse.png", "rb") as fh:
    content = fh.readlines()
    tempfh = open("ec.png", "wb")
    for eachline in content:
        tempfh.write(eachline)
    tempfh.close()        


