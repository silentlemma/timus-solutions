#include <cstdio>
#include <functional>
#include <queue>
#include <string>
#include <utility>
#include <vector>

const int BLOCKS = 30000, LIFETIME = 600;

int main() {
    // expiry[b]: when block b becomes free, unless it is accessed again
    std::vector<int> expiry(BLOCKS + 1, 0);
    std::vector<bool> busy(BLOCKS + 1, false);
    // times never decrease, so the expiries are queued in order; an entry is
    // stale when the block was accessed again later
    std::queue<std::pair<int, int>> expiries;
    std::priority_queue<int, std::vector<int>, std::greater<int>> freed;
    int fresh = 1;
    std::string out;
    int t;
    char op[2];
    while (scanf("%d %1s", &t, op) == 2) {
        while (!expiries.empty() && expiries.front().first <= t) {
            auto [e, b] = expiries.front();
            expiries.pop();
            if (busy[b] && expiry[b] == e) {
                busy[b] = false;
                freed.push(b);
            }
        }
        int b;
        if (op[0] == '+') {
            // freed blocks are all smaller than the never used ones
            if (!freed.empty()) {
                b = freed.top();
                freed.pop();
            } else {
                b = fresh++;
            }
            out += std::to_string(b);
        } else {
            if (scanf("%d", &b) != 1)
                break;
            if (!busy[b]) {
                out += "-\n";
                continue;
            }
            out += "+";
        }
        out += "\n";
        busy[b] = true;
        expiry[b] = t + LIFETIME;
        expiries.push({expiry[b], b});
    }
    fputs(out.c_str(), stdout);
}
