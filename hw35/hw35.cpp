#include <iostream>
#include <vector>
#include <list>
#include <string>
using namespace std;

template <class Iterator, class Function>
void find_if (Iterator first, Iterator last, Function predicate)
{
   for (Iterator i = first, i != last; ++i)
   {
      if (predicate(*i)) // found!
      {
         return i;
      }
   }

   return i; // returns last if not found
}

template <typename T>
class is_greater_than
{
public:
   is_greater_than (const T & n)
      : value(n)
   {}

   bool operator() (const T & element) const
   {
      return element > value;
   }

private:
   T value;
};

class to_lower
{
public:
    char operator() (char c) const        // notice the return type
    {
        return tolower(c);
    }
};

string lower (const string & str)
{
    string lcase = str;
    //transform (str.begin(), str.end(), lcase.begin(), to_lower());

    return lcase;
}

int main() {

    list<int> values{1,2,3,4};
    int search_value;

    //if (find_if (values.begin(), values.end(),
    //         is_greater_than<int> (5)) != values.end())

    // vector<string> words;
    // ifstream file ("words.txt");
    // if (file)
    // {
    //     copy (istream_iterator<string> (file), istream_iterator<string>(),
    //         back_inserter (words));
    //}

    return 0;
}