with open("test.txt", 'r') as reader:
    listofLines = reader.readlines()
    reversed(listofLines)
    with open("test.txt",'w') as writer:
        for revline in reversed(listofLines):
            writer.write(revline)

#reader & writer are object here.
