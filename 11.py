import random,statistics
with open("data.csv","w") as f:
    for _ in range(10):
        r=[random.randint(1,99) for _ in range(3)]
        f.write(f"{r[0]},{r[1]},{r[2]}\n")
col2=[]
with open("data.csv") as f:
    for line in f:
        col2.append(int(line.strip().split(",")[1]))
print(max(col2),min(col2),sum(col2)/len(col2),statistics.median(col2))