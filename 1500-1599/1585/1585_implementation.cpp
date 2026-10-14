#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    // every record is two words, the kind and "Penguin"
    map<string, int> seen;
    string kind, penguin;
    for (int i = 0; i < n; i++) {
        cin >> kind >> penguin;
        seen[kind]++;
    }
    string best;
    for (auto &[k, count] : seen)
        if (best.empty() || count > seen[best])
            best = k;
    cout << best << " Penguin" << endl;
}
