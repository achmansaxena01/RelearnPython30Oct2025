def my_fun2(*args, **kwargs):
    print(args)
    print(kwargs)

def myfun(x, *pos_param, **key_param):
    print(x)
    print(pos_param)
    for each in pos_param:
        print(each)
    print(key_param)
    for key, value in key_param.items():
        print(key, value)
    modified_pos_param = pos_param + (50,)
    my_fun2(*modified_pos_param, **key_param)

myfun(10, 20, 30, 40,name="Achman", sal=1000000)


