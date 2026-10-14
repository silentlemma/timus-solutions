#include <iostream>
#include <string>
#include <vector>
using namespace std;

string join(const vector<int> &order) {
    string s;
    for (size_t i = 0; i < order.size(); i++)
        s += (i ? " " : "") + to_string(order[i]);
    return s + "\n";
}

int main() {
    int n;
    cin >> n;
    // the cheapest round trip, as a cycle through n: one side of n goes
    // 2, n - 2, 4, n - 4, ..., the other 1, n - 1, 3, n - 3, ...; step k
    // takes the pair k, k + 1 for odd k and n - k, n - k + 1 for even k
    vector<bool> used(n + 1, false);
    used[n] = true;
    vector<int> oneSide, otherSide;
    for (int k = 1;; k++) {
        int a = k % 2 == 1 ? k + 1 : n - k, b = k % 2 == 1 ? k : n - k + 1;
        if (a < 1 || used[a] || used[b])
            break;
        oneSide.push_back(a);
        otherSide.push_back(b);
        used[a] = used[b] = true;
    }
    // the cycle: n, one side, the city left where the two sides meet if
    // any, and the other side back to n; it ends with city 1
    vector<int> cycle = {n};
    cycle.insert(cycle.end(), oneSide.begin(), oneSide.end());
    for (int v = 1; v < n; v++)
        if (!used[v])
            cycle.push_back(v);
    cycle.insert(cycle.end(), otherSide.rbegin(), otherSide.rend());
    vector<int> cheap = {cycle.back()};
    cheap.insert(cheap.end(), cycle.begin(), cycle.end() - 1);
    // the dearest: odd numbers up, then even numbers down, so that every
    // city is next to the two closest in size
    vector<int> dear;
    for (int v = 1; v <= n; v += 2)
        dear.push_back(v);
    for (int v = n - n % 2; v >= 2; v -= 2)
        dear.push_back(v);
    cout << join(cheap) << join(dear);
}
