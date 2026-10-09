#include <cstdio>
#include <string>
#include <vector>

const int MAX_COORD = 32000;

int size = 1;
std::vector<int> tree;

// stars at x in [lo, hi): a bottom-up segment tree over the coordinates
int countBelow(int lo, int hi) {
    int sum = 0;
    for (lo += size, hi += size; lo < hi; lo /= 2, hi /= 2) {
        if (lo & 1)
            sum += tree[lo++];
        if (hi & 1)
            sum += tree[--hi];
    }
    return sum;
}

void add(int x) {
    for (x += size; x > 0; x /= 2)
        tree[x]++;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 1;
    while (size <= MAX_COORD)
        size *= 2;
    tree.assign(2 * size, 0);
    // stars come by y, then x: the level of a star is the number of stars
    // already seen with x not greater than its own
    std::vector<int> count(n, 0);
    for (int i = 0; i < n; i++) {
        int x, y;
        if (scanf("%d %d", &x, &y) != 2)
            return 1;
        count[countBelow(0, x + 1)]++;
        add(x);
    }
    std::string out;
    for (int c : count)
        out += std::to_string(c) + "\n";
    fputs(out.c_str(), stdout);
}
