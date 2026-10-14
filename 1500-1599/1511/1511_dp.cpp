#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int BASE = 10;
const int INF = 1 << 30;

int main() {
    string a, b, c;
    cin >> a >> b >> c;
    int width = c.size();
    if ((int)max(a.size(), b.size()) > width) {
        cout << -1 << "\n"; // the sum would be longer than C
        return 0;
    }
    // digit i from the lowest, zero past the number's length
    auto digit = [](const string &s, int i) {
        return i < (int)s.size() ? s[s.size() - 1 - i] - '0' : 0;
    };
    // the lowest digit position i may take: the first digit may not become zero
    auto least = [](const string &s, int i) { return i == (int)s.size() - 1 ? 1 : 0; };
    // the highest: past its own length a number has only the digit 0
    auto most = [](const string &s, int i) { return i < (int)s.size() ? BASE - 1 : 0; };
    // cost[carry]: the cheapest fix of the lower positions that carries this
    vector<int> cost = {0, INF};
    for (int i = 0; i < width; i++) {
        vector<int> next = {INF, INF};
        for (int carry = 0; carry < 2; carry++) {
            if (cost[carry] == INF)
                continue;
            for (int x = least(a, i); x <= most(a, i); x++)
                for (int y = least(b, i); y <= most(b, i); y++) {
                    int total = x + y + carry, z = total % BASE;
                    if (z < least(c, i))
                        continue;
                    int v = cost[carry] + abs(x - digit(a, i)) + abs(y - digit(b, i)) +
                            abs(z - digit(c, i));
                    next[total / BASE] = min(next[total / BASE], v);
                }
        }
        cost = next;
    }
    cout << (cost[0] < INF ? cost[0] : -1) << "\n";
}
