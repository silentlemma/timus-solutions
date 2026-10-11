#include <algorithm>
#include <cstdio>
#include <vector>

// a brick and everything it carries: its ends, the total weight (lengths)
// and twice its moment about 0, R^2 - L^2 per brick
struct Brick {
    long long left, right, weight, moment;
};

int main() {
    int layers = 0;
    if (scanf("%d", &layers) != 1)
        return 0;
    std::vector<Brick> above, bricks;
    for (int layer = 0; layer < layers; layer++) {
        int k = 0;
        if (scanf("%d", &k) != 1)
            return 0;
        bricks.assign(k, Brick());
        for (Brick &b : bricks) {
            if (scanf("%lld %lld", &b.left, &b.right) != 2)
                return 0;
            b.weight = b.right - b.left;
            b.moment = b.right * b.right - b.left * b.left;
        }
        // each brick above rests on the one brick below that it overlaps, and
        // the centre of all it carries must lie strictly inside the overlap, a test
        // that the doubled moment keeps in whole numbers
        size_t j = 0;
        for (const Brick &a : above) {
            while (j < bricks.size() && bricks[j].right <= a.left)
                j++;
            if (j == bricks.size() || bricks[j].left >= a.right) {
                puts("No");
                return 0;
            }
            long long lo = std::max(a.left, bricks[j].left),
                      hi = std::min(a.right, bricks[j].right);
            if (!(2 * lo * a.weight < a.moment && a.moment < 2 * hi * a.weight)) {
                puts("No");
                return 0;
            }
            bricks[j].weight += a.weight;
            bricks[j].moment += a.moment;
        }
        above.swap(bricks);
    }
    puts("Yes");
    return 0;
}
