x = 2
if x > 0:
    print("i love coding")

print("choose a number")
y = input()

if y.isnumeric() == True:
    if int(y) > 0:
        print(y+" is greater than 0")
    elif int(y) < 10:
        print(y+" is less than 10")
else:
    print(y+" is not a number")


words = ["hi", "hello", "hey", "yo"]
for i in words:
    print(i)

for i in range(10):
    print(i)

list(range(5,10,2))

sum(range(10))

j = input()

def square(x):
    print("type a number")
    if x.isnumeric() == False:
        print("not a number")
    else:
        print("the square is ", int(x)*int(x), "\n")
        a, b = 0, 1
        print("fibo \n")
        while a < int(x):
            print(a, end=' ')
            a, b = b, a+b
    print() 

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


