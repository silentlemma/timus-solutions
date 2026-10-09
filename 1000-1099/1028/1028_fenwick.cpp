#include <cstdio>
#include <string>
#include <vector>

const int MAX_COORD = 32000;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 1;
    // stars come by y, then x: the level of a star is the number of stars
    // already seen with x not greater than its own; a Fenwick tree counts them
    std::vector<int> tree(MAX_COORD + 2, 0), count(n, 0);
    for (int i = 0; i < n; i++) {
        int x, y;
        if (scanf("%d %d", &x, &y) != 2)
            return 1;
        int level = 0;
        for (int j = x + 1; j > 0; j -= j & -j)
            level += tree[j];
        count[level]++;
        for (int j = x + 1; j <= MAX_COORD + 1; j += j & -j)
            tree[j]++;
    }
    std::string out;
    for (int c : count)
        out += std::to_string(c) + "\n";
    fputs(out.c_str(), stdout);
}
