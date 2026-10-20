#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

using Integer = std::int64_t;

constexpr int Scale = 100000;
constexpr int Digits = 10;
constexpr double AngleEps = 1e-12;
constexpr double GridEps = 1e-7;
constexpr double HalfTurn = 180;
constexpr int BigDigits = 9;
constexpr Integer BigBase = 1000000000;

struct Big {
    std::array<Integer, BigDigits> digits{};

    Big() { digits[0] = 1; }

    void multiply(Integer value) {
        if (value < 0) {
            value = -value;
        }
        __int128 carry = 0;
        for (Integer &digit : digits) {
            __int128 current = static_cast<__int128>(digit) * value + carry;
            digit = current % BigBase;
            carry = current / BigBase;
        }
    }

    int compare(const Big &other) const {
        for (int i = BigDigits - 1; i >= 0; --i) {
            if (digits[i] != other.digits[i]) {
                return digits[i] < other.digits[i] ? -1 : 1;
            }
        }
        return 0;
    }
};

struct Gun {
    double angle;
    Integer x, y;
};

bool fits(const Gun &left, const Gun &right, Integer distance, Integer cosine) {
    Integer cross = left.x * right.y - left.y * right.x;
    Integer dot = left.x * right.x + left.y * right.y;
    if (cross < 0) {
        return false;
    }
    if (cross == 0) {
        return dot > 0;
    }
    if (dot >= 0 && cosine < 0) {
        return true;
    }
    if (cosine >= 0 && dot < 0) {
        return false;
    }
    // Squared cosines distinguish tangencies from very small angular gaps.
    Big lhs, rhs;
    for (Integer factor : {dot, dot, distance, distance}) {
        lhs.multiply(factor);
    }
    for (Integer factor : {cosine, cosine, left.x * left.x + left.y * left.y,
                           right.x * right.x + right.y * right.y}) {
        rhs.multiply(factor);
    }
    return dot >= 0 ? lhs.compare(rhs) >= 0 : lhs.compare(rhs) <= 0;
}

Big power(Integer base, int exponent) {
    Big result;
    for (int i = 0; i < exponent; ++i) {
        result.multiply(base);
    }
    return result;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, shots, queries;
    std::cin >> n >> shots >> queries;
    std::vector<Gun> guns(n);
    for (Gun &gun : guns) {
        std::cin >> gun.x >> gun.y;
        gun.angle = std::atan2(static_cast<double>(gun.y), static_cast<double>(gun.x));
    }
    Integer a, b, radius;
    std::cin >> a >> b >> radius;
    Integer distance = a * a + b * b;
    Integer radiusSquared = radius * radius;
    Integer cosine = distance - 2 * radiusSquared;
    double pi = std::acos(-1.0);
    double fullTurn = 2 * pi;
    double halfWidth = std::atan2(radius, std::sqrt(distance - radiusSquared));
    double width = 2 * halfWidth;
    double lower = std::atan2(static_cast<double>(b), static_cast<double>(a)) - halfWidth;
    std::sort(guns.begin(), guns.end(), [](const Gun &left, const Gun &right) {
        if (left.angle != right.angle) {
            return left.angle < right.angle;
        }
        return left.x * right.y - left.y * right.x > 0;
    });
    int initial = 0;
    for (const Gun &gun : guns) {
        Integer cross = a * gun.y - b * gun.x;
        if (a * gun.x + b * gun.y >= 0 &&
            static_cast<__int128>(cross) * cross <=
                static_cast<__int128>(radiusSquared) * (gun.x * gun.x + gun.y * gun.y)) {
            ++initial;
        }
    }
    double infinity = std::numeric_limits<double>::infinity();
    std::vector<double> best(n + 1, infinity);
    best[0] = best[initial] = 0;
    int end = 0;
    for (int begin = 0; begin < n; ++begin) {
        end = std::max(end, begin);
        while (end < begin + n) {
            const Gun &other = guns[end % n];
            double delta = other.angle - guns[begin].angle + (end >= n ? fullTurn : 0);
            bool inside = std::abs(delta - width) <= AngleEps
                              ? fits(guns[begin], other, distance, cosine)
                              : delta < width;
            if (!inside) {
                break;
            }
            ++end;
        }
        double angle = std::fmod(lower - guns[begin].angle, fullTurn);
        if (angle < 0) {
            angle += fullTurn;
        }
        if (angle <= AngleEps || fullTurn - angle <= AngleEps) {
            // The exact side of the tangent distinguishes zero from a full turn.
            const Gun &gun = guns[begin];
            Integer cross = a * gun.y - b * gun.x;
            bool strict = static_cast<__int128>(cross) * cross <
                          static_cast<__int128>(radiusSquared) * (gun.x * gun.x + gun.y * gun.y);
            angle = strict ? fullTurn - AngleEps : 0;
        }
        best[end - begin] = std::min(best[end - begin], angle);
    }
    for (int count = n - 1; count >= 0; --count) {
        best[count] = std::min(best[count], best[count + 1]);
    }
    std::vector<int> levels(n + 1);
    Big denominator = power(n, shots);
    for (int count = 1; count < n; ++count) {
        if (shots == 1) {
            levels[count] = static_cast<Integer>(Scale) * count / n;
            continue;
        }
        int remaining = n - count;
        double value = Scale * (1 - std::pow(static_cast<double>(remaining) / n, shots));
        int nearest = static_cast<int>(value + 1.0 / 2);
        int level = static_cast<int>(value);
        if (std::abs(value - nearest) < GridEps) {
            Big lhs = power(remaining, shots);
            Big rhs = denominator;
            lhs.multiply(Scale);
            rhs.multiply(Scale - nearest);
            level = lhs.compare(rhs) <= 0 ? nearest : nearest - 1;
        }
        levels[count] = std::min(level, Scale - 1);
    }
    levels[n] = Scale;
    std::cout << std::fixed << std::setprecision(Digits);
    for (int query = 0; query < queries; ++query) {
        std::string word;
        std::cin >> word;
        auto point = word.find('.');
        int probability = std::stoi(word.substr(0, point)) * Scale;
        if (point != std::string::npos) {
            std::string fraction = word.substr(point + 1);
            int place = Scale;
            for (char digit : fraction) {
                place /= 10;
                probability += (digit - '0') * place;
            }
        }
        int count = std::lower_bound(levels.begin(), levels.end(), probability) - levels.begin();
        if (std::isinf(best[count])) {
            std::cout << -1 << '\n';
        } else {
            std::cout << best[count] * HalfTurn / pi << '\n';
        }
    }
}
