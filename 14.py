with open("test.txt") as f1,open("copy_test.txt") as f2:
    for idx,(a,b) in enumerate(zip(f1,f2),start=1):
        if a!=b:
            print("不同行：",idx)