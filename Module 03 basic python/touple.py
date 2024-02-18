things= 'akram', 'bappi', 'bag', 'bottle', 'charger'
print(type(things)) # 3->>> touple ->contains first bracket

print(things[0])
print(things[3])
print(things[2])
print(things[-4])
print(f'slice ',things[2:4])

for item in things:
    print(item)
mega= ([10,20,30],[40,50,70])
print("original touple")
print(type(mega))
print(mega)
print("changed touple")
mega[0][0]=500
print(mega)