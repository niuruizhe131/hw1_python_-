import random
i=int(input("行数："))
with open("test.txt","w") as f:
    for _ in range(i):
        s=''.join(chr(random.randint(0,127)) for _ in range(20))
        f.write(s+"\n")
with open("test.txt","r") as f1,open("copy_test.txt","w") as f2:
    f2.write(f1.read())