#include <cstdio>
#include <vector>

const int FRESH = 0, WALKING = 1, DONE = 2;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<int> to(n + 1), incoming(n + 1, 0);
    for (int v = 1; v <= n; v++) {
        scanf("%d", &to[v]);
        incoming[to[v]]++;
    }
    // follow the arrows from every new programmer to find the cycles
    std::vector<int> state(n + 1, FRESH), path;
    int cycles = 0, onCycles = 0, bare = 0;
    for (int start = 1; start <= n; start++) {
        path.clear();
        int v = start;
        while (state[v] == FRESH) {
            state[v] = WALKING;
            path.push_back(v);
            v = to[v];
        }
        if (state[v] == WALKING) {
            cycles++;
            // a cycle nobody else points into needs a group of its own
            bool alone = true;
            int u = v;
            do {
                onCycles++;
                if (incoming[u] != 1) alone = false;
                u = to[u];
            } while (u != v);
            if (alone) bare++;
        }
        for (int u : path) state[u] = DONE;
    }
    // fewest: every programmer nobody names starts a group, and so does
    // every bare cycle; most: a cycle goes into one group as soon as a
    // group enters it, and everyone else can stand alone
    int starts = 0;
    for (int v = 1; v <= n; v++) {
        if (incoming[v] == 0) starts++;
    }
    printf("%d %d\n", starts + bare, n - onCycles + cycles);
}
