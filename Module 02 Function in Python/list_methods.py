numbers = [45, 56, 12, 89, 87, 32, 84, 59, 46, 93]

numbers.append(100)
print(numbers)
numbers.insert(5,55)
print(numbers)
numbers.remove(100)
print(numbers)
if 98 in numbers:
    numbers.remove(98)
else:
    print(numbers) 
last = numbers.pop()
print(last, numbers)

if 589 in numbers:
    val= numbers.index(598)
    print(val)
else:
    print("list e nai") 
numbers.reverse()
print(numbers)