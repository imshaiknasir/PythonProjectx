#How to read all lines present in text file.
filex = open("test.txt")

#sample1
line = filex.readline()
while line != "":
    print(line)
    line = filex.readline()

#sample2
for line in filex.readlines():
    print(line)

lines = filex.readlines()
print(lines)