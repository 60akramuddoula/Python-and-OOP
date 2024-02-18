s= input()

string_list=[]
# print(type(string_list))
demo = ""
# print(type(demo))

cnt =0 
for i in range(0,len(s)):
    demo+=s[i]
    if(demo.count('L')== demo.count('R')):
        string_list.append(demo)
        cnt= cnt+1
        demo=""

print(cnt)
for strings in string_list:
    print(strings)
