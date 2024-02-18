from statistics import multimode


def fullName(first, second):
    name= f'full name is: {first} {second}'
    return name 

name= fullName('akramuddoula', 'bappi')
#  serial maintain korte hoy na python 
#  eta onk powerfull ekta kaj
# lets say fullname(last='bappi', first='akramuddoula')
print(name)


# def famous(**kargs)
def famous_name(first, last, **addition):
    name = f' {first} {last}'
    # print(addition['title'])
    print(addition['title'])
    # for key, value in addition.items():
    for key , val in addition.items():
        # eta mean kore addition theke ekta ekta kore value and key ber koro
        # and seta show koro, here tittle is key and hujur is keyvalue of the tittle
        print(key, val)
    return name

name = famous_name(first='Taher', last='Ali', 
                   title="Hujur", title2="Shayokh", 
                   last2='taheri')
print(name)

def all_sum(x,y):
    sum= x+y
    mult= x*y
    return sum, mult 

result = all_sum(10,20)
print(result)

def full_name(first, last):
    name = f'full name is: {first} {last}'
    return name

# take parameters in order(serial wise)
# name = full_name('Alu', 'kodu')
name = full_name(last='kodu', first='alu')
print(name)

# def famous(**kargs)
def famous_name(first, last, **addition):
    name = f' {first} {last}'
    # print(addition['title'])
    for key, value in addition.items():
        print(key, value)
    return name

name = famous_name(first='Taher', last='Ali', title="Hujur", title2="Shayokh", last2='taheri')
print(name)

# def function_name(num1, num2, *args, **kargs):


# return multiple things from an array
def a_lot(num1, num2):
    sum = num1 + num2
    mult = num1 * num2
    remain = num1 - num2
    # return [sum, mult, remain]
    return sum, mult, remain


everything = a_lot(55, 21)
print(everything)