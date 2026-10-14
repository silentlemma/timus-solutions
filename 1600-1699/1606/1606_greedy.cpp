#include <algorithm>
#include <cstdio>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<tuple<int, int, int>> flags(n); // (y, x, number)
    for (int i = 0; i < n; i++) {
        int x, y;
        if (scanf("%d %d", &x, &y) != 2)
            return 0;
        flags[i] = {y, x, i + 1};
    }
    sort(flags.rbegin(), flags.rend());
    // down the slope the x coordinates must zigzag; the longest zigzag keeps
    // the first flag, the last one of every run in one direction, and the end
    vector<int> path = {get<2>(flags[0])};
    for (int i = 1; i < n; i++) {
        bool last = i == n - 1;
        bool turns = !last && (get<1>(flags[i]) > get<1>(flags[i - 1])) !=
                                  (get<1>(flags[i + 1]) > get<1>(flags[i]));
        if (last || turns)
            path.push_back(get<2>(flags[i]));
    }
    string out = to_string(path.size()) + "\n";
    for (size_t i = 0; i < path.size(); i++)
        out += to_string(path[i]) + (i + 1 < path.size() ? " " : "\n");
    fputs(out.c_str(), stdout);
}
