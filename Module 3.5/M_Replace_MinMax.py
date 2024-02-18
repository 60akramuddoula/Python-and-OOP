n = int(input())
arr= [int(i) for i in input().split()]
# print(arr)

mx_index= arr.index(max(arr))
mn_index= arr.index(min(arr))

temp= arr[mx_index]
arr[mx_index]= arr[mn_index]
arr[mn_index]= temp 
print(*arr)