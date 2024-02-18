n = int(input())
# arr = list(map(int, input()))
arr = [int(i) for i in input()]
# print(arr)

sum =0 
for i in range(n):
    sum= sum + arr[i]

print(sum)