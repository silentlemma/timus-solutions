#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

// Signed arbitrary-precision integers, stored in little-endian limbs.
struct Integer {
    static constexpr uint64_t BASE = 1ULL << 30;
    std::vector<uint64_t> digits;
    bool negative = false;

    Integer(long long v = 0) : negative(v < 0) {
        uint64_t u = v < 0 ? -v : v;
        while (u) {
            digits.push_back(u % BASE);
            u /= BASE;
        }
    }

    void normalize() {
        while (!digits.empty() && digits.back() == 0)
            digits.pop_back();
        if (digits.empty())
            negative = false;
    }

    int magnitude(const Integer& b) const {
        if (digits.size() != b.digits.size())
            return digits.size() < b.digits.size() ? -1 : 1;
        for (size_t i = digits.size(); i-- > 0;)
            if (digits[i] != b.digits[i])
                return digits[i] < b.digits[i] ? -1 : 1;
        return 0;
    }

    bool operator<(const Integer& b) const {
        if (negative != b.negative)
            return negative;
        return negative ? magnitude(b) > 0 : magnitude(b) < 0;
    }

    Integer operator+(const Integer& b) const {
        Integer out;
        if (negative == b.negative) {
            out.negative = negative;
            uint64_t carry = 0;
            for (size_t i = 0; i < std::max(digits.size(), b.digits.size()) || carry; i++) {
                uint64_t v = carry + (i < digits.size() ? digits[i] : 0)
                             + (i < b.digits.size() ? b.digits[i] : 0);
                out.digits.push_back(v % BASE);
                carry = v / BASE;
            }
        } else {
            const Integer& hi = magnitude(b) >= 0 ? *this : b;
            const Integer& lo = magnitude(b) >= 0 ? b : *this;
            out.negative = hi.negative;
            int64_t borrow = 0;
            for (size_t i = 0; i < hi.digits.size(); i++) {
                int64_t v = int64_t(hi.digits[i]) - borrow
                            - (i < lo.digits.size() ? int64_t(lo.digits[i]) : 0);
                borrow = v < 0;
                out.digits.push_back(v < 0 ? v + BASE : v);
            }
        }
        out.normalize();
        return out;
    }

    Integer operator-(Integer b) const {
        if (!b.digits.empty())
            b.negative = !b.negative;
        return *this + b;
    }

    Integer operator*(const Integer& b) const {
        Integer out;
        out.negative = negative != b.negative;
        out.digits.resize(digits.size() + b.digits.size());
        for (size_t i = 0; i < digits.size(); i++) {
            uint64_t carry = 0;
            for (size_t j = 0; j < b.digits.size() || carry; j++) {
                uint64_t v = out.digits[i + j] + carry
                             + (j < b.digits.size() ? digits[i] * b.digits[j] : 0);
                out.digits[i + j] = v % BASE;
                carry = v / BASE;
            }
        }
        out.normalize();
        return out;
    }

    static Integer parse(const std::string& text) {
        Integer out;
        for (char c : text)
            if (c >= '0' && c <= '9')
                out = out * 10 + (c - '0');
        out.negative = text[0] == '-' && !out.digits.empty();
        return out;
    }
};

Integer abs(Integer v) {
    v.negative = false;
    return v;
}

// squared distances carry these denominators: a point scaled by 2, a square
// by its projections
const long long POINT_DEN = 4, SQUARE_DEN = 8;

struct Fraction {
    Integer num;
    long long den;
};

// squared distance from P to the square with diagonal (x1, y1)-(x2, y2)
Fraction distance(long long x1, long long y1, long long x2, long long y2,
                  const Integer& px, const Integer& py) {
    // doubled coordinates of P relative to the centre, and the diagonal
    Integer qx = px * 2 - (x1 + x2), qy = py * 2 - (y1 + y2);
    long long dx = x2 - x1, dy = y2 - y1, h = dx * dx + dy * dy;
    if (h == 0)
        return {qx * qx + qy * qy, POINT_DEN};
    // projections on the two side directions, the diagonal turned by +-45
    // degrees; inside the square both stay within h
    Integer s1 = abs(qx * (dx - dy) + qy * (dy + dx));
    Integer s2 = abs(qx * (dx + dy) + qy * (dy - dx));
    Integer a = std::max(Integer(0), s1 - h), b = std::max(Integer(0), s2 - h);
    return {a * a + b * b, SQUARE_DEN * h};
}

int main() {
    int n;
    if (!(std::cin >> n))
        return 0;
    std::vector<long long> x1(n), y1(n), x2(n), y2(n);
    for (int i = 0; i < n; i++)
        std::cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
    std::string sx, sy;
    std::cin >> sx >> sy;
    Integer px = Integer::parse(sx), py = Integer::parse(sy);
    std::vector<Fraction> dist(n);
    for (int i = 0; i < n; i++)
        dist[i] = distance(x1[i], y1[i], x2[i], y2[i], px, py);
    // exact cross products, with the input index breaking ties
    std::vector<int> order(n);
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(), [&](int i, int j) {
        Integer a = dist[i].num * dist[j].den, b = dist[j].num * dist[i].den;
        return a < b || (!(b < a) && i < j);
    });
    for (int i = 0; i < n; i++)
        std::cout << order[i] + 1 << (i + 1 < n ? ' ' : '\n');
}
