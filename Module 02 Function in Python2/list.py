#  in generel list , array is same 

numbers = [45, 56, 12, 89, 87, 32, 84, 59, 46, 93]

print(numbers[3], numbers[-3])
#  list numbers[start : end ]
print(numbers[1:len(numbers):2])
print(numbers[2: 6])
# print(numbers[7: 2])
print(numbers[3:])
print(numbers[:5])
print(numbers[7: 2: -1])

print(numbers[:])  # shortcut to copy a list 
print(numbers[:: -1]) # reverse an array totally


# list numbers[start : end : step] -> here we can jump the index
# for number in numbers:
#     print(number)
# print(numbers)


# list, array, collection is same (simple terms)

# index =   0   1   2   3   4  5   6   7   8   9  
numbers = [45, 56, 12, 89, 87, 32, 84, 59, 46, 93]
# index = -10  -9  -8  -7  -6  -5  -4  -3  -2  -1  

print(numbers[3], numbers[-3]) 

# list( start : end ) # start from the start index and stops before the end index
print(numbers[2:6])
print(numbers[1:7])

# list(start : end : step)
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[2:7:-1])
print(numbers[7:2:-1])
print(numbers[7:2:-2])
print(numbers[4:])
print(numbers[:5])
print(numbers[:]) # shortcut to copy a list
print(numbers[::-1]) #shortcut to reverse a list

""" 
The list data type has some more methods. Here are all of the methods of list objects:

list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].
 """