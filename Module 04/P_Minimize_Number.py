n = int(input())
arr= list(map(int, input().split()))
# print(arr)

flag= False
for i in arr:
    if i%2!=0:
        flag=True

if(flag):
    print(0)
else:
    cnt =0 
    while(True):
        arr= [nums //2 for nums in arr]
        flag= False
        for i in arr:
            if i%2!=0:
                flag= True
            
        cnt+= 1
        if(flag):
            break

    print(cnt)