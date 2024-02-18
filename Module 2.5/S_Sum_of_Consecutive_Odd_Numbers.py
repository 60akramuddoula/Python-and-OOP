t = int(input())
while t > 0:
    x, y = map(int, input().split())

    # takes input as a list 
    # for example if i take input like 10 20 , it will take 
    # this "10","20"
    
    start = min(x, y) + 1
    end = max(x, y)
    total_sum = 0
    
    for i in range(start, end):
        if i % 2 != 0:
            total_sum += i
    
    print(total_sum)
    t -= 1
