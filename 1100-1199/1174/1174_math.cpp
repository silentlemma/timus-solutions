#include <cstdio>
#include <vector>

const long long BASE = 1000000000;

// rank = rank * m + add, on little-endian digits in base 10^9
void mulAdd(std::vector<long long> &rank, long long m, long long add) {
    long long carry = add;
    for (auto &d : rank) {
        carry += d * m;
        d = carry % BASE;
        carry /= BASE;
    }
    for (; carry; carry /= BASE) {
        rank.push_back(carry % BASE);
    }
}

int main() {
    int n;
    scanf("%d", &n);
    std::vector<int> where(n + 1);
    for (int i = 0; i < n; i++) {
        int v;
        scanf("%d", &v);
        where[v] = i;
    }
    // rank of the order of 1..k among themselves: element k sweeps once
    // across the order of 1..k-1, to the left in even sweeps and to the
    // right in odd ones, and that order's rank counts the sweeps before
    std::vector<long long> rank = {0};
    for (int k = 2; k <= n; k++) {
        int smallerLeft = 0;
        for (int v = 1; v < k; v++) {
            smallerLeft += where[v] < where[k];
        }
        int step = rank[0] % 2 ? smallerLeft : k - 1 - smallerLeft;
        mulAdd(rank, k, step);
    }
    mulAdd(rank, 1, 1);
    printf("%lld", rank.back());
    for (int k = rank.size() - 2; k >= 0; k--) {
        printf("%09lld", rank[k]);
    }
    printf("\n");
}
