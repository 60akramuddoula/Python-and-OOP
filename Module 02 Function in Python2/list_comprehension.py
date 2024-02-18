# numbers= [10,2,30,40,8,50,100,65]

# odds= []
# for num in numbers:
#     if num%2==0 and num%5==0:
#         odds.append(num) 

# print(odds)

# odd_nums= ( num for num in numbers if num%2==0) 
#  not readable for everyone
# print(odd_nums)

players= ['sakib', 'mushfik', 'liton']
ages=[10,20,30]

combination_of=[]
for player in players:
    for age in ages:
        # print('player: ', player, 'age :', age)
        combination_of.append([player, age]) 
print(combination_of)

com_of=([player, age ]for player in players for age in ages )
print(com_of)
