from attrs import *
import sys


def has_attr(attrs, x):
    if x in attrs:
        return True
    else:
        return False

def remove_attr(attrs, x):
    dict1 = dict(attrs)
    for key in list(dict1.keys()):
        if key == x:
            dict1.pop(key)
    print(dict1)

def update_attr(attrs, x):
    dict1 = dict(attrs)
    for key in list(dict1.keys()):
        if key == x[0] and x[1] > 0:
            dict1[key] = x[1]
            print(dict1)
            return
        elif key == x[0] and x[1] < 0:
            dict1.pop(key)
            print(dict1)
            return
    dict1[x[0]] = x[1]
    print(dict1)

def update_multi_attr(attrs, x):
    y = x[1]
    x = x[0]
    xstate = True
    ystate = True

    dict1 = dict(attrs)
    while xstate == True:
        if x[1] < 0:
            xstate = False
        for key in list(dict1.keys()):
            if key == x[0] and x[1] >= 0:
                dict1[key] = x[1]
                xstate = False
            elif key == x[0] and x[1] < 0:
                dict1.pop(key)
                xstate = False

    while ystate == True:
        if y[1] < 0:
            ystate = False
        for key in list(dict1.keys()):
            if key == y[0] and y[1] >= 0:
                dict1[key] = y[1]
                ystate = False
            elif key == y[0] and y[1] < 0:
                dict1.pop(key)
                ystate = False

    print(dict1)

non_attr_val = -sys.maxsize

def attrs_from_string(x):
    dict1 = {}
    x = x.split(" ")
    for i in range(0,len(x),2):
        dict1[x[i]] = int(x[i+1])
    print(dict1)
    
            

def main():
    attrs = {'a': 3, 'b': 4}
    has_attr(attrs, "b")
    remove_attr(attrs, 'a')
    update_attr(attrs, ['a', 17])
    update_attr(attrs, ['c', 17])
    print(non_attr_val)
    update_attr(attrs, ['a', non_attr_val])
    update_multi_attr(attrs, [['b', 5], ['a', non_attr_val]])
    attrs_from_string("d 3 e 4")


if __name__ == "__main__":
    main()