#include <cstdio>
#include <queue>
#include <string>
#include <utility>
using namespace std;

int main() {
    int k;
    if (scanf("%d", &k) != 1)
        return 0;
    priority_queue<pair<int, int>> heap; // (signs left, kind)
    for (int t = 1; t <= k; t++) {
        int c;
        if (scanf("%d", &c) != 1)
            return 0;
        heap.push({c, t});
    }
    string out;
    int prev = 0;
    while (!heap.empty()) {
        auto [count, t] = heap.top();
        heap.pop();
        if (t == prev && !heap.empty()) {
            // the most plentiful kind was just used: take the next one
            auto other = heap.top();
            heap.pop();
            heap.push({count, t});
            count = other.first;
            t = other.second;
        }
        out += to_string(t);
        out += ' ';
        prev = t;
        if (count > 1)
            heap.push({count - 1, t});
    }
    out.back() = '\n';
    fputs(out.c_str(), stdout);
}
