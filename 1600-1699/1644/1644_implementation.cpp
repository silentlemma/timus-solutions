#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

const int KNOWN_HUNGRY = 2, KNOWN_FULL = 10; // given in the statement

int main() {
    int n;
    if (!(cin >> n))
        return 0;
    int hungry = KNOWN_HUNGRY, full = KNOWN_FULL;
    for (int i = 0; i < n; i++) {
        int count;
        string verdict;
        cin >> count >> verdict;
        if (verdict == "hungry")
            hungry = max(hungry, count);
        else
            full = min(full, count);
    }
    // the smallest satisfying amount must exceed the largest hungry one
    if (full > hungry)
        cout << full << '\n';
    else
        cout << "Inconsistent\n";
}
