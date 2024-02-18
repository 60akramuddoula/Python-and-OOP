
name = 'akrmuddoula'
name2= 'rafat fahim'
name3= """
shakib khan
biplop hossain

"""

print(name)
# string is a sequence of characters
for char in name2:
    print(char)

print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])
print(name)

#  mutable means changeable
# immutable means not changeable
#  name2[0]= H => this not possible 
if 'fahim' in name2:
    print('exsit') 
else:
    print('not exists')

print(name.upper())
print(name.lower())
if name == name2:
    print('same to same')
else:
    print('not same')




name = 'Sakib\'s Khan' #escape 
name2 = "sakib khan"
# multiline string
name3 = """
    Sakib khan
    number one
"""

print(name)
# string is a sequence of characters
for char in name2:
    print(char)

print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])

# mutable means changeable 
# immutable means you can not change it
# name2[0] = 'R'
print(name2)
if 'khan' in name2:
    print('exists')

print(name2.upper())