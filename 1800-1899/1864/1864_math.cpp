#include <algorithm>
#include <cstdio>
#include <vector>

const int MONEY = 100;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<int> bought(n);
    int total = 0;
    for (int &b : bought) {
        scanf("%d", &b);
        total += b;
    }
    // everybody, Den too, drinks total / (n + 1); in units of 1 / (n + 1)
    // litre, friend i paid for bought[i] (n + 1) - total litres of others
    std::vector<int> over(n);
    int all = 0;
    for (int i = 0; i < n; i++) {
        over[i] = std::max(0, bought[i] * (n + 1) - total);
        all += over[i];
    }
    for (int i = 0; i < n; i++) printf(i ? " %d" : "%d", MONEY * over[i] / all);
    printf("\n");
    return 0;
}
