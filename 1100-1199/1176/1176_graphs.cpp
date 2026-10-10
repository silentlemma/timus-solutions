#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int n, a;
    scanf("%d %d", &n, &a);
    // the channels still to lay are the missing ones; every planet has as
    // many of them going out as coming in, so they form one Euler circuit
    std::vector<std::vector<int>> todo(n + 1);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            int t;
            scanf("%d", &t);
            if (t == 0 && i != j) {
                todo[i].push_back(j);
            }
        }
    }
    // Hierholzer: walk until stuck, then back up and splice in side loops
    std::vector<size_t> next(n + 1, 0);
    std::vector<int> stack = {a}, circuit;
    while (!stack.empty()) {
        int v = stack.back();
        if (next[v] < todo[v].size()) {
            stack.push_back(todo[v][next[v]++]);
        } else {
            circuit.push_back(v);
            stack.pop_back();
        }
    }
    std::reverse(circuit.begin(), circuit.end());
    for (size_t k = 0; k + 1 < circuit.size(); k++) {
        printf("%d %d\n", circuit[k], circuit[k + 1]);
    }
}
