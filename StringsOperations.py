#Some operations using strings

val1 = "TheBigBilion"
val2 = "Dollar"

print(val1[0:6]) #to print sub-string
print(val1 + val2) #concatenate
print("TheBig" in val1)
print(val1.split('B')) #split takes a character as input and breaks the original string into list, whereever the character is present.

val3 = " String with spaces "
print(val3.strip()) #strip will omit the whitespaces present at the start/end of any string.
print(val3.lstrip()) #lstrip will omit the whitespaces present at the start of any string.
print(val3.rstrip()) #rstrip will omit the whitespaces present at the end of any string.


