#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <tuple>
#include <vector>

constexpr int64_t MAX_VALUE = 1000000000;

std::tuple<int64_t, int64_t, int64_t> extended_gcd(int64_t a, int64_t b) {
    int64_t x = 1, next_x = 0, y = 0, next_y = 1;
    while (b) {
        const int64_t quotient = a / b;
        std::tie(a, b) = std::make_tuple(b, a - quotient * b);
        std::tie(x, next_x) = std::make_tuple(next_x, x - quotient * next_x);
        std::tie(y, next_y) = std::make_tuple(next_y, y - quotient * next_y);
    }
    return {a, x, y};
}

int64_t normalized(__int128 value, int64_t modulus) {
    value %= modulus;
    if (value < 0)
        value += modulus;
    return static_cast<int64_t>(value);
}

int64_t largest_modulus(int64_t d, int64_t e, int64_t constraint) {
    if (e % std::gcd(d, constraint) == 0)
        return constraint;
    const int64_t common = std::gcd(constraint, e);
    int64_t remaining = constraint / common;
    const int64_t forbidden = d / std::gcd(d, e);
    while (true) {
        const int64_t divisor = std::gcd(remaining, forbidden);
        if (divisor == 1)
            return common * remaining;
        remaining /= divisor;
    }
}

struct Answer {
    int length;
    int64_t modulus, multiplier;
};

Answer witness(int length, int64_t d, int64_t e, int64_t constraint) {
    const int64_t modulus = constraint ? largest_modulus(d, e, constraint) : d * MAX_VALUE + 1;
    const int64_t common = std::gcd(d, modulus), reduced = modulus / common;
    int64_t multiplier = 0;
    if (reduced != 1) {
        const auto [divisor, inverse, unused] = extended_gcd(d / common, reduced);
        static_cast<void>(divisor);
        static_cast<void>(unused);
        multiplier = normalized(static_cast<__int128>(e / common) * inverse, reduced);
    }
    return {length, modulus, multiplier};
}

Answer solve(const std::vector<int64_t> &values) {
    const int n = static_cast<int>(values.size());
    if (values[0] == 0) {
        int length = 0;
        while (length < n && values[length] == 0)
            ++length;
        return {length, 1, 0};
    }
    if (n == 1)
        return {1, values[0] + 1, 0};
    int64_t d = values[0], e = values[1], constraint = 0;
    int64_t largest = std::max(values[0], values[1]);
    int length = 2;
    for (int index = 1; index < n - 1; ++index) {
        const int64_t a = values[index], b = values[index + 1];
        if (a == 0) {
            if (b)
                break;
            length = index + 2;
            continue;
        }
        const int64_t divisor = std::gcd(d, a);
        __int128 next_e = e;
        if (divisor != d) {
            const auto [unused, x, y] = extended_gcd(d, a);
            static_cast<void>(unused);
            next_e = static_cast<__int128>(x) * e + static_cast<__int128>(y) * b;
        }
        __int128 determinant =
            static_cast<__int128>(d / divisor) * b - static_cast<__int128>(a / divisor) * e;
        if (determinant < 0)
            determinant = -determinant;
        const int64_t next_constraint =
            constraint ? std::gcd(constraint, static_cast<int64_t>(determinant % constraint))
                       : static_cast<int64_t>(determinant);
        const int64_t next_value =
            next_constraint ? normalized(next_e, next_constraint) : static_cast<int64_t>(next_e);
        const int64_t next_largest = std::max(largest, b);
        if (next_constraint &&
            largest_modulus(divisor, next_value, next_constraint) <= next_largest) {
            break;
        }
        d = divisor;
        e = next_value;
        constraint = next_constraint;
        largest = next_largest;
        length = index + 2;
    }
    return witness(length, d, e, constraint);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    std::vector<int64_t> values(count);
    for (int64_t &value : values)
        std::cin >> value;
    const Answer answer = solve(values);
    std::cout << answer.length << ' ' << answer.modulus << ' ' << answer.multiplier << '\n';
}
