class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    

    def add_trick(self, trick):
        self.tricks.append(trick)

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

class Warehouse:
    purpose = 'storage'
    region = 'west'

def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   

class MappingSubclass(Mapping):

    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

class Employee:
    pass

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def main():
    d = Dog("Jerry")
    w1 = Warehouse()
    w2 = Warehouse()
    w2.region = 'east'
    print(w2.purpose, w2.region)
    print(w1.purpose, w1.region)

    g = C()
    print(g.f(1,2))

    john = Employee() 
    john.name = 'John Doe'
    john.dept = 'computer lab'
    john.salary = 1000 
    rev = Reverse('spam')

if __name__ == "__main__":
    main()