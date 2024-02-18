
def doubled(num):
    return num*2

doubled= lambda num: num*2
# do same thing using lambda function technique 
# syntax : function name = lambda keyword varriable name : operation 
squared= lambda num: num*num
result= doubled(10)
ans = squared(10)
print(ans)
print(result)


add = lambda x,y : x+y
do = add(10,15)
print(do)

# Map: when i have to deal with single single value 
# value of a list then i should use Map function 




numbers= [10,20,30,40]
double_map= map(lambda x : x*2, numbers)
print(numbers)
print(list(double_map))

actors= [
    {'name': 'akramuddoula', 'age': 25},
    {'name': 'habib', 'age': 50},
    {'name': 'asif', 'age': 100},
    {'name': 'polash', 'age': 85},
    {'name': 'dhusor', 'age': 25},
]
# filter works only a particular element of the array 
# it works with condition
juniors= filter(lambda actor : actor['age']<85, actors)
print(list(juniors))