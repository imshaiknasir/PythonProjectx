import json

with open("jsonFile1.json", 'r') as file1:
    jsondata1 = json.load(file1)
    print(jsondata1["object"]['a'])

with open('jsonFile2.json') as file2:
    jsondata2 = json.load(file2)

print(jsondata1 == jsondata2)   #or use assert
assert jsondata1 == jsondata2