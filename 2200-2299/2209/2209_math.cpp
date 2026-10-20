#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    long long depth, position;
    std::cin >> depth >> position;
    const long long index = position - 1;
    int bits = 0;
    for (long long value = index; value > 0; value /= 2) {
        ++bits;
    }

    long long left_num = 0, left_den = 1;
    long long right_num = 1, right_den = depth - 1 - bits;
    // Leading zero bits move only the right denominator.
    for (int bit = bits - 1; bit >= 0; --bit) {
        if ((index >> bit) & 1) {
            left_num += right_num;
            left_den += right_den;
        } else {
            right_num += left_num;
            right_den += left_den;
        }
    }

    std::cout << left_num + right_num << ' ' << left_den + right_den << '\n';
}
