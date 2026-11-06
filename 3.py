f1,f2=0,1
print(f1,f2,end=" ")
for i in range(3,21):
    f=f1+f2
    f1=f2
    f2=f
    print(f,end=" ")