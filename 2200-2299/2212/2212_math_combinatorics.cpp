#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

constexpr int MOD = 998244353;
constexpr int ROOT = 3;

int power(int base, int exponent) {
    int result = 1;
    while (exponent > 0) {
        if (exponent & 1) {
            result = static_cast<long long>(result) * base % MOD;
        }
        base = static_cast<long long>(base) * base % MOD;
        exponent >>= 1;
    }
    return result;
}

void transform(vector<int> &a, bool inverse) {
    int size = static_cast<int>(a.size());
    for (int i = 1, j = 0; i < size; ++i) {
        int bit = size >> 1;
        while (j & bit) {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
        if (i < j) {
            swap(a[i], a[j]);
        }
    }
    for (int length = 2; length <= size; length <<= 1) {
        int step = power(ROOT, (MOD - 1) / length);
        if (inverse) {
            step = power(step, MOD - 2);
        }
        int half = length / 2;
        for (int start = 0; start < size; start += length) {
            long long weight = 1;
            for (int j = 0; j < half; ++j) {
                int left = a[start + j];
                int right = weight * a[start + j + half] % MOD;
                int sum = left + right;
                int difference = left - right;
                if (sum >= MOD) {
                    sum -= MOD;
                }
                if (difference < 0) {
                    difference += MOD;
                }
                a[start + j] = sum;
                a[start + j + half] = difference;
                weight = weight * step % MOD;
            }
        }
    }
    if (inverse) {
        int scale = power(size, MOD - 2);
        for (int &value : a) {
            value = static_cast<long long>(value) * scale % MOD;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, days;
    cin >> n >> days;
    int size = 1;
    while (size < 2 * n - 1) {
        size <<= 1;
    }
    vector<int> values(size), kernel(size), inverses(n);
    for (int i = 0; i < n; ++i) {
        cin >> values[i];
    }
    inverses[1] = 1;
    kernel[0] = 1;
    // Repeated prefix sums have coefficients C(days + i - 1, i).
    for (int i = 1; i < n; ++i) {
        if (i > 1) {
            inverses[i] = MOD - static_cast<long long>(MOD / i) * inverses[MOD % i] % MOD;
        }
        kernel[i] = static_cast<long long>(kernel[i - 1]) * (days + i - 1) % MOD;
        kernel[i] = static_cast<long long>(kernel[i]) * inverses[i] % MOD;
    }
    transform(values, false);
    transform(kernel, false);
    for (int i = 0; i < size; ++i) {
        values[i] = static_cast<long long>(values[i]) * kernel[i] % MOD;
    }
    transform(values, true);
    for (int i = 0; i < n; ++i) {
        cout << values[i] << (i + 1 == n ? '\n' : ' ');
    }
}
