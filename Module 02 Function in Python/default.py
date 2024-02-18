# def sum(num1, num2,num3=0):
#     result= num1 + num2+num3
#     print(result) 
    
# sum(10,20,23)


# args
def all_args(num1,num2, *numbers):
    # print(numbers)
    sum=0
    for i in numbers:
        # print(i)
        sum+=i 

    return sum 

joss= all_args(10,20,30,40,50,60)
print(joss)

def do_a_lot(*args):
    print(args)