if __name__=="__main__":
   num_list=list(range(1000))
   for idx in range(len(num_list)-1,-1,-1):
      if num_list[idx]%2==1:
        num_list.pop(idx)
   print(num_list)