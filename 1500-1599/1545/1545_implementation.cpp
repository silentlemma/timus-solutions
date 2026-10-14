#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> words(n);
    for (auto &w : words)
        cin >> w;
    string letter;
    cin >> letter;
    // the dictionary order is kept, repeated entries are printed every time
    for (const auto &w : words)
        if (w[0] == letter[0])
            cout << w << "\n";
}
