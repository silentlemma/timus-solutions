#include <cstdio>

typedef unsigned long long u64;
typedef unsigned __int128 u128;

const int INPUTS = 3;
u64 m;

struct Matrix {
    u64 a[2][2];
};

Matrix multiply(const Matrix &x, const Matrix &y) {
    Matrix r;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            r.a[i][j] = ((u128)x.a[i][0] * y.a[0][j] + (u128)x.a[i][1] * y.a[1][j]) % m;
    return r;
}

int main() {
    u64 n, k;
    if (scanf("%llu %llu %llu", &n, &k, &m) != INPUTS)
        return 1;
    u64 d = (k - 1) % m;
    // (zero, other) -> (other, (zero + other)(K - 1)) is the matrix step,
    // after the first digit the pair is (0, K - 1)
    Matrix step = {{{0, 1 % m}, {d, d}}}, power = {{{1 % m, 0}, {0, 1 % m}}};
    for (u64 e = n - 1; e > 0; e >>= 1) {
        if (e & 1)
            power = multiply(power, step);
        step = multiply(step, step);
    }
    u64 zero = (u128)power.a[0][1] * d % m, other = (u128)power.a[1][1] * d % m;
    printf("%llu\n", (u64)(((u128)zero + other) % m));
}
