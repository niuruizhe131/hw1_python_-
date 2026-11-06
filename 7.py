if __name__=="__main__":
    people=list(range(1,234))
    count=0
    index=0
    while len(people)>1:
        count+=1
        if count==3:
            people.pop(index)
            count=0
        else:
            index+=1
            if index>=len(people):
                index=0
print("最后剩下：",people[0])