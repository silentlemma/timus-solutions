#include <iostream>
#include <set>
#include <string>

using namespace std;

const int LIMIT = 20;

int main() {
    ios::sync_with_stdio(false);
    set<string> names = {"sun"}; // the base starts with this one name
    string line, out;
    while (cin >> line) {
        string arg = line.substr(1);
        if (line[0] == '+') {
            names.insert(arg);
            continue;
        }
        out += arg + "\n";
        // names with this prefix form a run starting where the prefix would go
        int shown = 0;
        for (auto it = names.lower_bound(arg); it != names.end() && shown < LIMIT; ++it, ++shown) {
            if (it->compare(0, arg.size(), arg) != 0)
                break;
            out += "  " + *it + "\n";
        }
    }
    cout << out;
}
