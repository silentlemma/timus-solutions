#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

using namespace std;

constexpr int MODULUS = 998244353;
constexpr int PRIMITIVE_ROOT = 3;

int power(int base, int exponent) {
    int result = 1;
    while (exponent > 0) {
        if (exponent & 1) {
            result = static_cast<int>(int64_t(result) * base % MODULUS);
        }
        base = static_cast<int>(int64_t(base) * base % MODULUS);
        exponent >>= 1;
    }
    return result;
}

vector<int> make_roots(int size) {
    vector<int> roots(size);
    roots[1] = 1;
    for (int length = 2; length < size; length <<= 1) {
        int step = power(PRIMITIVE_ROOT, (MODULUS - 1) / (length * 2));
        for (int index = length / 2; index < length; ++index) {
            roots[index * 2] = roots[index];
            roots[index * 2 + 1] = static_cast<int>(int64_t(roots[index]) * step % MODULUS);
        }
    }
    return roots;
}

void forward_transform(vector<int> &values, const vector<int> &roots) {
    int size = static_cast<int>(values.size());
    for (int length = size; length > 1; length >>= 1) {
        int half = length / 2;
        for (int start = 0; start < size; start += length) {
            for (int offset = 0; offset < half; ++offset) {
                int first = values[start + offset];
                int second = values[start + offset + half];
                int sum = first + second;
                if (sum >= MODULUS) {
                    sum -= MODULUS;
                }
                int difference = first - second;
                if (difference < 0) {
                    difference += MODULUS;
                }
                values[start + offset] = sum;
                values[start + offset + half] =
                    static_cast<int>(int64_t(difference) * roots[half + offset] % MODULUS);
            }
        }
    }
}

void reverse_transform(vector<int> &values, const vector<int> &roots) {
    int size = static_cast<int>(values.size());
    for (int length = 2; length <= size; length <<= 1) {
        int half = length / 2;
        for (int start = 0; start < size; start += length) {
            for (int offset = 0; offset < half; ++offset) {
                int first = values[start + offset];
                int second = static_cast<int>(int64_t(values[start + offset + half]) *
                                              roots[half + offset] % MODULUS);
                int sum = first + second;
                if (sum >= MODULUS) {
                    sum -= MODULUS;
                }
                int difference = first - second;
                if (difference < 0) {
                    difference += MODULUS;
                }
                values[start + offset] = sum;
                values[start + offset + half] = difference;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    int total = n + m;
    int size = 1;
    while (size < n + total - 1) {
        size <<= 1;
    }
    vector<int> factorial(total, 1), inverse_factorial(total, 1);
    for (int index = 1; index < total; ++index) {
        factorial[index] = static_cast<int>(int64_t(factorial[index - 1]) * index % MODULUS);
    }
    inverse_factorial[total - 1] = power(factorial[total - 1], MODULUS - 2);
    for (int index = total - 1; index > 0; --index) {
        inverse_factorial[index - 1] =
            static_cast<int>(int64_t(inverse_factorial[index]) * index % MODULUS);
    }

    vector<int> first(size), second(size);
    for (int index = 0; index < n; ++index) {
        int value;
        cin >> value;
        int weight = static_cast<int>(int64_t(value) * inverse_factorial[index] % MODULUS *
                                      inverse_factorial[n - 1 - index] % MODULUS);
        if ((n - 1 - index) & 1) {
            weight = weight == 0 ? 0 : MODULUS - weight;
        }
        first[index] = weight;
    }
    for (int index = 1; index < total; ++index) {
        second[index] =
            static_cast<int>(int64_t(factorial[index - 1]) * inverse_factorial[index] % MODULUS);
    }

    vector<int> roots = make_roots(size);
    forward_transform(first, roots);
    forward_transform(second, roots);
    for (int index = 0; index < size; ++index) {
        first[index] = static_cast<int>(int64_t(first[index]) * second[index] % MODULUS);
    }
    reverse_transform(first, roots);

    // The paired passes leave coefficients reversed and multiplied by size.
    int inverse_size = power(size, MODULUS - 2);
    for (int index = n; index < total; ++index) {
        int answer =
            static_cast<int>(int64_t(first[size - index]) * inverse_size % MODULUS *
                             factorial[index] % MODULUS * inverse_factorial[index - n] % MODULUS);
        if (index > n) {
            cout << ' ';
        }
        cout << answer;
    }
    cout << '\n';
}
