import random
if __name__=="__main__":
    with open("data.txt","w") as f:
        for _ in range(100000):
            num=random.randint(1,100)
            f.write(f"{num}\n")