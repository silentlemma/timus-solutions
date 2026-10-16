#include <cstdio>
#include <iostream>
#include <vector>

typedef std::vector<std::vector<long long>> Matrix;

Matrix multiply(const Matrix &a, const Matrix &b, long long mod) {
    size_t n = a.size();
    Matrix c(n, std::vector<long long>(n, 0));
    for (size_t i = 0; i < n; i++) {
        for (size_t k = 0; k < n; k++) {
            if (!a[i][k]) continue;
            for (size_t j = 0; j < n; j++) c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % mod;
        }
    }
    return c;
}

int main() {
    std::ios::sync_with_stdio(false);
    long long n, m, d, mod;
    int q;
    std::cin >> n >> m >> d >> mod >> q;
    std::vector<std::vector<long long>> points(q, std::vector<long long>(n));
    for (auto &p : points) {
        for (auto &x : p) std::cin >> x;
    }
    // the number of routes depends only on how many coordinates differ
    // from the target: a move fixes one of them, changes one of them to
    // another wrong value, or spoils one that was right
    int size = n + 1;
    Matrix step(size, std::vector<long long>(size, 0)), power = step;
    for (int h = 0; h < size; h++) {
        if (h > 0) {
            step[h][h - 1] = h % mod;
            step[h][h] = h * (m - 2) % mod;
        }
        if (h < n) step[h][h + 1] = (n - h) * (m - 1) % mod;
        power[h][h] = 1 % mod;
    }
    for (; d > 0; d >>= 1) {
        if (d & 1) power = multiply(power, step, mod);
        step = multiply(step, step, mod);
    }
    for (int i = 0; i < q; i++) {
        for (int j = 0; j < q; j++) {
            int differ = 0;
            for (int k = 0; k < n; k++) differ += points[i][k] != points[j][k];
            printf(j ? " %lld" : "%lld", power[differ][0]);
        }
        printf("\n");
    }
}
