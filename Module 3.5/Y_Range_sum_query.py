n, q = map(int, input().split())

# n, q= map(int , input().split())

# arr= [for int(i) in input()]
arr = [int(i) for i in input().split()]


while q > 0:
    x, y = map(int, input().split())
    summation = 0 
    for i in range(x, y):  
        summation += arr[i]  
        
    print(summation)  
    q -= 1
