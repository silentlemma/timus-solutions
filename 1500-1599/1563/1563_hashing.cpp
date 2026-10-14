#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int main() {
    int n;
    string line;
    cin >> n;
    getline(cin, line);
    unordered_set<string> seen;
    int repeats = 0;
    for (int i = 0; i < n && getline(cin, line); i++) {
        // a name is the whole line, spaces included; only the line end goes
        if (!line.empty() && line.back() == '\r')
            line.pop_back();
        if (!seen.insert(line).second)
            repeats++;
    }
    cout << repeats << endl;
}
