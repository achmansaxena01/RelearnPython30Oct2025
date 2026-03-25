def myfun(x,*args,**kwargs):
    print(x)
    print(args)
    for each in args:
        print(each)
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)
myfun(10,20,30,40,name = "Achman", sal = 1000000)
