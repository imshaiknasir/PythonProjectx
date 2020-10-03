values = [1, 2, "test", 3, 7]

values.append(7)
values.insert(0, "one")
values[-1] = 'seven'
del values[3]
values.pop(3)

print(values)