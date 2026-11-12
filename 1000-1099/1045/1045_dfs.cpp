#include <cstdio>
#include <vector>

using Flights = std::vector<std::vector<int>>;

bool winning(const Flights &flights, int airport, int previous) {
    // In a tree, the previous airport is the only destroyed neighbor.
    for (int next : flights[airport])
        if (next != previous && !winning(flights, next, airport))
            return true;
    return false;
}

int main() {
    int n, start;
    if (std::scanf("%d %d", &n, &start) != 2)
        return 0;
    Flights flights(n + 1);
    for (int i = 1; i < n; ++i) {
        int a, b;
        if (std::scanf("%d %d", &a, &b) != 2)
            return 0;
        flights[a].push_back(b);
        flights[b].push_back(a);
    }
    int best = n + 1;
    for (int next : flights[start])
        if (next < best && !winning(flights, next, start))
            best = next;
    if (best <= n)
        std::printf("First player wins flying to airport %d\n", best);
    else
        std::puts("First player loses");
}
