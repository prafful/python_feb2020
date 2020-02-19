'''

try:
    pass
except expression as identifier:
    pass
else:
    pass

'''
try:
    fh = open('myfile.txt', 'wb')
    fh.write(b"File operation binary!")
except BaseException as exception:
    print("Error while working with file!", exception)
else:
    fh.close()
    print("File operation is success!")
