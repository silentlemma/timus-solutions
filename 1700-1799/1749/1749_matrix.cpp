#include <cstdio>
#include <iostream>
#include <string>

const int SIZE = 4;
const long long BASE = 10;

typedef long long Matrix[SIZE][SIZE];

void multiply(const Matrix a, const Matrix b, Matrix c, long long m) {
    Matrix t = {};
    for (int i = 0; i < SIZE; i++) {
        for (int k = 0; k < SIZE; k++) {
            for (int j = 0; j < SIZE; j++) t[i][j] = (t[i][j] + a[i][k] * b[k][j]) % m;
        }
    }
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) c[i][j] = t[i][j];
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::string digits;
    long long k, m;
    std::cin >> digits >> k >> m;
    // going left to right, E is the sum of the substrings ending at the
    // current digit: E' = 10 E + digit * (its position), and S adds up E,
    // so one copy of p acts linearly on (S, E, J, 1), J digits before it
    long long power = 1 % m, value = 0, weighted = 0;
    long long sumPower = 0, sumValue = 0, sumWeighted = 0;
    for (size_t i = 0; i < digits.size(); i++) {
        long long d = digits[i] - '0';
        power = power * BASE % m;
        value = (value * BASE + d) % m;
        weighted = (weighted * BASE + d * (long long)(i + 1)) % m;
        sumPower = (sumPower + power) % m;
        sumValue = (sumValue + value) % m;
        sumWeighted = (sumWeighted + weighted) % m;
    }
    Matrix block = {{1 % m, sumPower, sumValue, sumWeighted},
                    {0, power, value, weighted},
                    {0, 0, 1 % m, (long long)digits.size() % m},
                    {0, 0, 0, 1 % m}};
    Matrix result = {};
    for (int i = 0; i < SIZE; i++) result[i][i] = 1 % m;
    for (; k > 0; k >>= 1) {
        if (k & 1) multiply(result, block, result, m);
        multiply(block, block, block, m);
    }
    // starting from S = E = J = 0, the total is the constant column of S
    printf("%lld\n", result[0][SIZE - 1]);
}
