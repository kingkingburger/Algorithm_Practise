l = [int(input()) for _ in range(10)]
l = [(l[i]%42) for i in range(10)]
# for i in range(10):
#     l[i] = (l[i]%42)
print(len(set(l)))