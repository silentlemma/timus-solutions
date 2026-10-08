#include <cstdio>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<int> w(n);
    int total = 0;
    for (int &x : w) {
        if (scanf("%d", &x) != 1)
            return 0;
        total += x;
    }
    // reach[s]: some stones weigh exactly s; the lighter pile is at most total/2
    int half = total / 2;
    std::vector<char> reach(half + 1, 0);
    reach[0] = 1;
    for (int x : w)
        for (int s = half; s >= x; s--)
            reach[s] |= reach[s - x];
    int s = half;
    while (!reach[s])
        s--;
    printf("%d\n", total - 2 * s);
    return 0;
}
