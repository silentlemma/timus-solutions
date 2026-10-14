#include <algorithm>
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    map<string, int> count;
    int largest = 0;
    for (int i = 0; i < 1 << n; i++) {
        string name, prefecture;
        cin >> name >> prefecture;
        largest = max(largest, ++count[prefecture]);
    }
    // c wrestlers of one prefecture can avoid each other in all rounds but
    // ceil(log2 c) of them, and dealing the wrestlers sorted by prefecture
    // round-robin into that many top-level groups achieves it for all at once
    int unsafe = 0;
    while (1 << unsafe < largest)
        unsafe++;
    cout << n - unsafe << "\n";
}
