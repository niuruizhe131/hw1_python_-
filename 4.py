s=input().strip()
wei=len(s)
print("位数",wei)
print("逆序各位",end=" ")
for i in s[::1]:
    print(i,end="　")