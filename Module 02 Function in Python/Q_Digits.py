t = int(input())

while(t > 0):
    n = input()
     # works like a space
    name = n[:: -1] # reverse a string with slice 
    for char in name:
        print(char, end=' ')
    print() # it works like a new line
    t -= 1


# name ='akramddoula'
# for char in name:
#     print(char, end=' ')