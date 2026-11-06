count=0
abc=[]
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b and b!=c and c!=a:
                    num=a*100+b*10+c
                    abc.append(num)
                    count+=1
print(count)
print(abc)
      