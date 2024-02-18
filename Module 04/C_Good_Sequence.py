
n = input()

# sequence_input = input().split(" ")
# sequence_input = list(map(int,))
# sequence_input = list(map(int, input().split()))
a= list(map(int,input().split()))


count_dict = {}


for num in a:
    if num not in count_dict:
        count_dict[num] = 0
    
    count_dict[num] += 1
    
total_removals = 0


for key, val in count_dict.items():
    if val > key:
        total_removals += val - key
    elif val < key:
        total_removals += val


print(total_removals)
