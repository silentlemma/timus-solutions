#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

using Wide = __int128;
constexpr long long FIRST_ODD = 3;
constexpr long long MIN_HYPOTENUSE = 5;

Wide integer_root(Wide value) {
    Wide low = 0, high = 1;
    while (high * high <= value)
        high *= 2;
    while (high - low > 1) {
        Wide middle = (low + high) / 2;
        if (middle * middle <= value)
            low = middle;
        else
            high = middle;
    }
    return low;
}

std::vector<long long> divisors(long long number) {
    std::vector<long long> values{1};
    for (long long prime = 2; prime * prime <= number; prime = prime == 2 ? FIRST_ODD : prime + 2) {
        std::size_t previous = values.size();
        long long power = 1;
        while (number % prime == 0) {
            number /= prime;
            power *= prime;
            for (std::size_t i = 0; i < previous; ++i)
                values.push_back(values[i] * power);
        }
    }
    if (number > 1) {
        std::size_t previous = values.size();
        for (std::size_t i = 0; i < previous; ++i)
            values.push_back(values[i] * number);
    }
    return values;
}

struct Geometry {
    Wide dot, cross, denominator;

    std::vector<long long> point(long long x, long long y) const {
        Wide u = dot * x - cross * y;
        Wide v = dot * y + cross * x;
        if (u % denominator != 0 || v % denominator != 0)
            return {};
        return {0,
                0,
                x,
                y,
                static_cast<long long>(u / denominator),
                static_cast<long long>(v / denominator)};
    }
};

std::vector<long long> solve(std::vector<long long> sides) {
    std::sort(sides.begin(), sides.end());
    long long radius = sides[0], length = sides[1], opposite = sides[2];
    Wide r = radius, b = length, a = opposite;
    Wide twice_dot = r * r + b * b - a * a;
    if (twice_dot % 2 != 0)
        return {};
    Wide dot = twice_dot / 2;
    Wide square = r * r * b * b - dot * dot;
    if (square < 0)
        return {};
    Wide cross = integer_root(square);
    if (cross * cross != square)
        return {};
    Geometry geometry{dot, cross, r * r};
    for (auto point : {geometry.point(radius, 0), geometry.point(0, radius)}) {
        if (!point.empty())
            return point;
    }
    for (long long hypotenuse : divisors(radius)) {
        if (hypotenuse < MIN_HYPOTENUSE || hypotenuse % 2 == 0)
            continue;
        long long end = static_cast<long long>(integer_root(hypotenuse - 1));
        for (long long m = static_cast<long long>(integer_root(hypotenuse / 2)) + 1; m <= end;
             ++m) {
            long long rest = hypotenuse - m * m;
            long long k = static_cast<long long>(integer_root(rest));
            if (k * k != rest || std::gcd(m, k) != 1 || (m - k) % 2 == 0)
                continue;
            long long scale = radius / hypotenuse;
            long long x = scale * (m * m - k * k), y = scale * 2 * m * k;
            auto answer = geometry.point(x, y);
            if (!answer.empty())
                return answer;
            answer = geometry.point(y, x);
            if (!answer.empty())
                return answer;
        }
    }
    return {};
}

int main() {
    long long a, b, c;
    if (!(std::cin >> a >> b >> c))
        return 0;
    auto answer = solve({a, b, c});
    if (answer.empty())
        std::cout << -1 << '\n';
    else {
        for (std::size_t i = 0; i < answer.size(); i += 2)
            std::cout << answer[i] << ' ' << answer[i + 1] << '\n';
    }
}
