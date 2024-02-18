

x, n = input().split()
x= int(x)
n= int(n)

def eqution(x,n):
    sum =0
    for i in range(2,n+1,2):
        # print(i)
        sum = sum + x**i 
    return sum

ans= eqution(x,n)
print(ans)
