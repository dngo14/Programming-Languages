#include <iostream>
#include <vector>
#include <list>
#include <string>
using namespace std;

int car(vector<int> x) {
    int first = x.front();
    return first;
}

vector<int> cddr(vector<int> x) {
    vector<int> returnvector;
    returnvector.assign(x.begin(), x.end());
    returnvector.erase(returnvector.begin());
    return returnvector;
}

vector<int> cons(vector<int> x, vector<int> y) {
    vector<int> combinedlist;
    combinedlist.reserve(x.size()+y.size());
    combinedlist.insert(combinedlist.end(), x.begin(), x.end());
    combinedlist.insert(combinedlist.end(), y.begin(), y.end());
    return combinedlist;
}

int carlist(list<int> x) {
    int first = x.front();
    return first;
}

list<int> cddrlist(list<int> x) {
    list<int> returnlist;
    returnlist.assign(x.begin(), x.end());
    returnlist.erase(returnlist.begin());
    return returnlist;
}

list<int> conslist(list<int> x, list<int> y) {
    list<int> combinedlist;
    combinedlist.insert(combinedlist.end(), x.begin(), x.end());
    combinedlist.insert(combinedlist.end(), y.begin(), y.end());
    return combinedlist;
}

int main() {
    vector<int> vector1{1,2,3,4};
    cout << car(vector1) << "\n";

    vector<int> vector2;
    vector2 = cddr(vector1);
    for (int i: vector2) {
        cout << i << ' ';
    }

    cout << "\n";

    vector<int> vector3;
    vector3 = cons(vector1, vector2);
    for (int i: vector3) {
        cout << i << ' ';
    }

    cout << "\n";

    int y = car(cddr(vector1));
    cout << y << "\n";

    int z = car(cddr(cddr(vector1)));
    cout << z << "\n";

    list<int> list1{1,2,3,4};
    cout << carlist(list1) << "\n";

    list<int> list2;
    list2 = cddrlist(list1);
    for (int i: list2) {
        cout << i << ' ';
    }

    cout << "\n";

    list<int> list3;
    list3 = conslist(list1, list2);
    for (int i: list3) {
        cout << i << ' ';
    }

    cout << "\n";

    int k = carlist(cddrlist(list1));
    cout << k << "\n";

    return 0;
}