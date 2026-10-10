#include <algorithm>
#include <cstdio>
#include <vector>

enum { NEW, PATH, GOOD };

static bool consistent(const std::vector<int> &names) {
    int n = (int)names.size();
    if (std::count(names.begin(), names.end(), 0) != 1) {
        return false;
    }
    std::vector<int> state(n + 1, NEW), path;
    for (int start = 1; start <= n; start++) {
        // follow the accusations until a confessor or a child already known
        // to lead to one; meeting the current path again means a ring
        path.clear();
        int v = start;
        while (v != 0 && state[v] == NEW) {
            state[v] = PATH;
            path.push_back(v);
            v = names[v - 1];
        }
        if (v != 0 && state[v] == PATH) {
            return false;
        }
        for (int u : path) {
            state[u] = GOOD;
        }
    }
    return true;
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        std::vector<int> names(n);
        for (int &k : names) {
            scanf("%d", &k);
        }
        puts(consistent(names) ? "YES" : "NO");
    }
}
