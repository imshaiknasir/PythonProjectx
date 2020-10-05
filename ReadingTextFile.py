file1 = open('test.txt') #open() used to open any file; and takes the location of the file as argument.

print(file1.read()) #read() function reads all the content from the text file.
print(file1.read(4)) #argument inside sting function will display the number of character from the text file.
print(file1.readline()) #This wil read first-line from the text file.

file1.close()