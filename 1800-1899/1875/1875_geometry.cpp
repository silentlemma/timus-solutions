#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

typedef long long ll;

const int MONKEYS = 5;
ll xs[MONKEYS], ys[MONKEYS];

// y / x = b - c x along a shot, so the slopes y / x of points on one shot
// lie on a line in x; compared with all fractions cleared
bool one_shot(int i, int j, int k) {
    ll left = (ys[k] * xs[i] - ys[i] * xs[k]) * xs[j] * (xs[j] - xs[i]);
    ll right = (ys[j] * xs[i] - ys[i] * xs[j]) * xs[k] * (xs[k] - xs[i]);
    return left == right;
}

int main() {
    for (int i = 0; i < MONKEYS; i++)
        if (scanf("%lld %lld", &xs[i], &ys[i]) != 2) return 0;
    int full = (1 << MONKEYS) - 1;
    vector<int> shots;
    for (int i = 0; i < MONKEYS; i++) shots.push_back(1 << i);
    for (int i = 0; i < MONKEYS; i++) {
        for (int j = 0; j < MONKEYS; j++) {
            // gravity bends the path down: the slope y / x must fall as x grows
            if (xs[i] < xs[j] && ys[i] * xs[j] > ys[j] * xs[i]) {
                int mask = 0;
                for (int k = 0; k < MONKEYS; k++)
                    if (one_shot(i, j, k)) mask |= 1 << k;
                shots.push_back(mask);
            }
        }
    }
    vector<int> need(full + 1, MONKEYS);
    need[0] = 0;
    for (int mask = 0; mask <= full; mask++)
        for (int shot : shots) need[mask | shot] = min(need[mask | shot], need[mask] + 1);
    printf("%d\n", need[full]);
    return 0;
}
