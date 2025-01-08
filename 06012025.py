def Rev_number():
    num=12345
    Rev_num=str(num)[::-1]
    print(Rev_num)
Rev_number()

def Largetinlist():
    mylist=[12,52,63,85,94,523]
    Largest=mylist[0]
    for num in mylist:
        if num>Largest:
          Largest=num
    print(Largest)
Largetinlist()

def Missing_number():
    my_List=[1,2,3,4,6,8,9,11,13,15,17]
    start=my_List[0]
    end=my_List[-1]
    result=sorted(set(range(start,end+1))-set(my_List))
    print(result)
Missing_number()

def duplicate():
    test_list=[4,8,5,2,5,6,8,9,7,10,12,15,6,4]
    seen=set()
    duplicates=set()
    for num in test_list:
      if num in seen:
          duplicates.add(num)
      else:
          seen.add(num)
    print(sorted(duplicates))
duplicate()

def factorial_num():
    num=5
    if num<0:
        print("Number should be positive")
    elif num==1:
        print(1)
    else:
        result=1
        for i in range(2,num+1):
            result*=i
        print(result)
factorial_num()



