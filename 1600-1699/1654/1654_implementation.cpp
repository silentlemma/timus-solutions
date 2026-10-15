#include <iostream>
#include <string>
using namespace std;

int main() {
    string text, stack;
    cin >> text;
    // a letter equal to the one before it cancels that one: removing the
    // inserted pairs in any order leaves the same text
    for (char c : text) {
        if (!stack.empty() && stack.back() == c)
            stack.pop_back();
        else
            stack.push_back(c);
    }
    cout << stack << '\n';
}
