from function import double_it

#  here import is used to import somthing from another file 
#  or another function. syntax is just like english translation
val= double_it(100)
print(f'from the function.py theke ', val)

from function import double_it as ans
f_ans= ans(250)
print(f_ans , f'name change kore dewa hoyeshe') 

#  if we want import all the function from 
#  any file then i need to use 'from file_name
#  import * 