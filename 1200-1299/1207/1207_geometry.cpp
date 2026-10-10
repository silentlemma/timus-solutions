#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    std::vector<long long> x(n), y(n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &x[i], &y[i]);
    }
    // the lowest point (the leftmost of the lowest) sees all others within
    // half a turn, so they can be sorted by angle with cross products
    int pivot = 0;
    for (int i = 1; i < n; i++) {
        if (y[i] < y[pivot] || (y[i] == y[pivot] && x[i] < x[pivot])) {
            pivot = i;
        }
    }
    std::vector<int> others;
    for (int i = 0; i < n; i++) {
        if (i != pivot) {
            others.push_back(i);
        }
    }
    long long px = x[pivot], py = y[pivot];
    std::sort(others.begin(), others.end(), [&](int i, int j) {
        return (x[i] - px) * (y[j] - py) - (y[i] - py) * (x[j] - px) > 0;
    });
    // the middle one leaves (n - 2) / 2 points on each side of the line
    printf("%d %d\n", pivot + 1, others[(n - 2) / 2] + 1);
}
