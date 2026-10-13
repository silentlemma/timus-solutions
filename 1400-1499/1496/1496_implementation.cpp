#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    // a team that submitted more than once is the spammer; the teams are
    // printed in the order of their first submission
    map<string, int> count;
    vector<string> order;
    for (int i = 0; i < n; i++) {
        string team;
        cin >> team;
        if (count[team]++ == 0)
            order.push_back(team);
    }
    for (auto &team : order)
        if (count[team] > 1)
            cout << team << "\n";
}
