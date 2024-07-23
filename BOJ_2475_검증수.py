num_list = map(int,input().split())
res = 0
for n in num_list:
    res += n**2
print(res%10)