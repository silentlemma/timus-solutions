#include <cstdio>
#include <utility>
#include <vector>

// the disks start on the source rod and go to the target rod
const int SOURCE = 1, TARGET = 2, SPARE = 3;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<int> rod(n + 1);
    for (int i = 1; i <= n; i++)
        if (scanf("%d", &rod[i]) != 1)
            return 0;
    // disks 1..k are being moved from a to b over c; disk k moves once, in the
    // middle: before it the others go to c, after it they go from c to b
    int a = SOURCE, b = TARGET, c = SPARE;
    long long steps = 0;
    for (int k = n; k >= 1; k--) {
        if (rod[k] == a) {
            std::swap(b, c);
        } else if (rod[k] == b) {
            steps += 1LL << (k - 1);
            std::swap(a, c);
        } else {
            steps = -1;
            break;
        }
    }
    printf("%lld\n", steps);
}
