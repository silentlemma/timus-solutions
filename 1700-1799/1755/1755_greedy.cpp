#include <algorithm>
#include <cstdio>

struct Good {
    long long worth, cost, amount;
    int slot;
};

int main() {
    long long a1, b1, a2, b2, n, m;
    if (scanf("%lld %lld %lld %lld %lld %lld", &a1, &b1, &a2, &b2, &n, &m) < 1) return 0;
    // Karlsson leaves the piece he likes no more than half, so the best is
    // the piece of greatest worth to Little Boy within half of Karlsson's total:
    // a fractional knapsack where each ingredient is taken by worth per cost
    Good goods[] = {{a1, a2, n, 0}, {b1, b2, m, 1}};
    // zero-cost goods first, then by worth over cost, highest first
    if (goods[1].worth * goods[0].cost > goods[0].worth * goods[1].cost) {
        std::swap(goods[0], goods[1]);
    }
    double room = (a2 * n + b2 * m) / 2.0;
    double piece[2] = {0, 0};
    for (const Good &g : goods) {
        double take = g.cost * g.amount <= room ? g.amount : room / g.cost;
        piece[g.slot] = take;
        room -= take * g.cost;
    }
    printf("%.8f %.8f\n", piece[0], piece[1]);
    return 0;
}
