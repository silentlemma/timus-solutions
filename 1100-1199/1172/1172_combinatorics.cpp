#include <cstdio>
#include <vector>

typedef std::vector<long long> Big; // little-endian digits in base 10^9
const long long BASE = 1000000000;
const int ISLANDS = 3;

Big add(const Big &x, const Big &y) {
    Big r;
    long long carry = 0;
    for (size_t k = 0; k < x.size() || k < y.size() || carry; k++) {
        carry += (k < x.size() ? x[k] : 0) + (k < y.size() ? y[k] : 0);
        r.push_back(carry % BASE);
        carry /= BASE;
    }
    return r;
}

void mulSmall(Big &x, long long m) {
    long long carry = 0;
    for (auto &d : x) {
        carry += d * m;
        d = carry % BASE;
        carry /= BASE;
    }
    for (; carry; carry /= BASE) {
        x.push_back(carry % BASE);
    }
}

void divSmall(Big &x, long long m) {
    long long rest = 0;
    for (int k = x.size() - 1; k >= 0; k--) {
        long long cur = x[k] + rest * BASE;
        x[k] = cur / m;
        rest = cur % m;
    }
    while (x.size() > 1 && x.back() == 0) {
        x.pop_back();
    }
}

int main() {
    int n;
    scanf("%d", &n);
    // plane[b][c][i]: sequences of islands that start on the tourist's island
    // 0, use a, b and c cities of the islands (a fixed per plane), never
    // repeat an island twice in a row and end on island i
    typedef std::vector<std::vector<std::vector<Big>>> Plane;
    Plane prev, cur;
    for (int a = 1; a <= n; a++) {
        cur.assign(n + 1, std::vector<std::vector<Big>>(n + 1, std::vector<Big>(ISLANDS)));
        for (int b = 0; b <= n; b++) {
            for (int c = 0; c <= n; c++) {
                std::vector<Big> &cell = cur[b][c];
                if (a == 1 && b == 0 && c == 0) {
                    cell[0] = {1};
                }
                if (a > 1) {
                    cell[0] = add(prev[b][c][1], prev[b][c][2]);
                }
                if (b > 0) {
                    cell[1] = add(cur[b - 1][c][0], cur[b - 1][c][2]);
                }
                if (c > 0) {
                    cell[2] = add(cur[b][c - 1][0], cur[b][c - 1][1]);
                }
            }
        }
        prev.swap(cur);
    }
    // the trip closes back on island 0, so it must not end there
    Big total = add(prev[n][n][1], prev[n][n][2]);
    if (total.empty()) {
        total = {0};
    }
    // cities fill the island slots in any order, except the fixed start, and
    // every trip is counted once in each direction; (n-1)! n!^2 is the
    // product of k^2 (k-1) over k from 2 to n
    for (int k = 2; k <= n; k++) {
        mulSmall(total, (long long)k * k * (k - 1));
    }
    divSmall(total, 2);
    printf("%lld", total.back());
    for (int k = total.size() - 2; k >= 0; k--) {
        printf("%09lld", total[k]);
    }
    printf("\n");
}
