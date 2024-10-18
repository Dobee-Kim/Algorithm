N = int(input())

guild = list(map(int,input().split()))

guild.sort(reverse=True)

num_group = 0
first_idx = 0
next_idx = 0
while True:
    next_idx = guild[first_idx]
    num_group += 1
    if first_idx+next_idx >= N:
        break
    first_idx = next_idx
print(num_group)
# 6 
# 1 1 2 4 4 4 -> 3