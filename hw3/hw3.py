x = [1,22,3,4]
print(x)
x.append(3)
print(x)
x.insert(2, "hi")
print(x)
x.pop(2)
print(x)
print(x.count(3))
y = x.copy()
print(y)
print(y.pop())

from collections import deque
q = deque([1,2,3,4,5,6,7])
q.append(8)
print(q.popleft())
print(q)

squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]

vector = [-2,3,4,1]
y = [x*2 for x in vector]
print(y)

k= [abs(x) for x in y]
print(k)

print([(x, x**2) for x in range(6)])

matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]]

print([[row[i] for row in matrix] for i in range(4)])

del y[0]
print(y)

t = 12345, 54321, 'hello!'
u = t, (1, 2, 3, 4, 5)
print(u)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  
print("pineapple" in basket)
b = set('alacazam')
t = list("yoooll")
u = set("yellow")
print(t)
print(b | u)

tel = {'jack': 4098, 'sape': 4139}
print(tel["jack"])

print({x: x**2 for x in (2, 4, 6)})

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
j = "danniel"
print("hello my name is {0}".format(j))

for i in reversed(range(1, 10, 2)):
    print(i)

print(sorted(basket))