numbers = [12, 56 , 98, 78, 56, 12, 26, 98]
person1 = ['Kala Chan', 'kalipur', 23, 'student']
# key value pair
# dictionary
# object
# hash table
# overlap with set
# {key: value, key: value, key: value ->declearation

person = {'Name':'akrmuddoula', 'address':'khunla', 'roll':60}
print(person)
print(person.keys())
print(person.values())
print(f'roll holo bappir',person['roll'])

person['Name']= 'Md Habibur Rahman'
person['roll']=59
person['address']= 'chuadangga'
# del person['roll']  # delete something from the dictionary
print(person)

# special dictionary looping
for key, val in person.items():
    print(key, val)
    