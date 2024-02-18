# list --> []
# tuple --> ()
# set --> {}
# set: unique items collection. No duplicate

numbers = [12, 56 , 98, 78, 56 , 12 , 6, 98]
print(numbers)
numbers_set= set(numbers)
print('set')
print(numbers_set)

numbers_set.add(100)
numbers_set.add(500)
numbers_set.add(155)
numbers_set.add(158)
print(numbers_set)
print('remove korbo')
numbers_set.remove(100)
print(numbers_set)

for item in numbers_set:
    print(item)

if 98 in numbers_set:
    print('exist')
elif 100 in numbers_set:
    print('155 milgaye')
else:
    print('na pelam na')
numbers.reverse()
print(numbers)

A= {20,30,50,80}
B={1,30,50}
print(A & B)
print(A | B)
