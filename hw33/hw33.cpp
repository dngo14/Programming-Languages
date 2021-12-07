#include <iostream>
#include <string>
using namespace std;

int globalint;

int doubleint (int x) 
{
    int x2 = x*2;
    return x2;
}

void printmessage ()
{
  cout << "I'm a function!";
}

void doublevalue (int& a) {
    a*=2;
}

string concatenate (const string& a, const string& b)
{
  return a+b;
}

int divide (int a, int b=2)
{
  int r;
  r=a/b;
  return (r);
}

long factorial (long a)
{
  if (a > 1)
   return (a * factorial (a-1));
  else
   return 1;
}

void printarray (int arg[], int length) {
  for (int n=0; n<length; ++n)
    cout << arg[n] << ' ';
  cout << '\n';
}

void increment_all (int* start, int* stop)
{
  int * current = start;
  while (current != stop) {
    ++(*current);  // increment value pointed
    ++current;     // increment pointer
  }
}

void print_all (const int* start, const int* stop)
{
  const int * current = start;
  while (current != stop) {
    cout << *current << '\n';
    ++current;     // increment pointer
  }
}

struct product {
  int weight;
  double price;
};

class Rectangle {
    int width, height;

    public:
        void set_values(int, int);
        int area () {
            return width*height;
        };
};

void Rectangle::set_values (int x, int y) {
    width = x;
    height = y;
}

class Circle {
    double radius;
  public:
    Circle(double r) { 
        radius = r; 
        }
    double circum() {
        return 2*radius*3.14159265;
        }
    double area() {
        return radius*radius*3.14159265;
        }
};

class Cylinder {
    Circle base;
    double height;
  public:
    Cylinder(double r, double h) : base (r), height(h) {}
    double volume() {return base.area() * height;}
};


int main() {
    int a, b, c;
    a = 3;
    b = 4;
    int result = b-a;
    cout << "Hello World!\n";
    cout << result;

    double r = 5.2;
    const double pi = 3.14;
    a+=2;
    b = b++;

    if (b == 100)
        cout << "x is 100";
    int n = 0;
    while (n < 5) {
        cout << n;
        n++;
    }
    for (int i = 0; i < 3; i++) {
        cout << i << "\n";
    }

    int value = doubleint(2);
    cout << value << "\n";

    doublevalue(value);
    cout << value << "\n";

    int foo [5] = {1,2,3,4,5};
    int foo2 [] = { 16, 2, 77, 40, 12071 };

    cout << foo[4] << "\n";

    char myword[] = { 'H', 'e', 'l', 'l', 'o', '\0' };
    char myword2[] = "Hello"; 

    int * address = &value;
    *address = 200;
    cout << *address << "\n" << value;

    int numbers[5];
    int *number;
    number = numbers;
    *number = 1;
    number++;
    *number = 2;
    number = &numbers[2];
    *number = 3;
    number = numbers + 3;
    *number = 4;
    number = numbers;
    *(numbers+4) = 5;
    for (int n=0; n<5; n++)
    cout << numbers[n] << ", ";

    int * foo3;
    foo3 = new int [5];

    delete[] foo3;

    product apple;
    apple.weight = 2;
    apple.price = 1.50;

    Rectangle rect;
    rect.set_values(3,4);
    int areaofrect = rect.area();

    return 0;
}