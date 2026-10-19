#include <algorithm>
#include <array>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <utility>
#include <vector>

using Integer = long long;
using Interval = std::pair<double, double>;
constexpr Integer GRAVITY = 10;
constexpr Integer HALF_GRAVITY = GRAVITY / 2;
constexpr Integer QUADRATIC_FACTOR = 4;
constexpr int INPUT_FIELDS = 8;
constexpr int OUTPUT_DIGITS = 17;
constexpr double MARGIN = 1e-6;
using Data = std::array<Integer, INPUT_FIELDS>;

struct Polynomial {
    Integer a, b, c;
};
struct Piece {
    double left, right;
    Polynomial polynomial;
};

bool roots(Polynomial p, Interval &answer) {
    Integer delta = p.b * p.b + QUADRATIC_FACTOR * p.a * p.c;
    if (delta < 0)
        return false;
    if (delta == 0) {
        double value = static_cast<double>(p.b) / (2 * p.a);
        answer = {value, value};
        return true;
    }
    double q = (p.b + std::copysign(std::sqrt(static_cast<double>(delta)), p.b)) / 2;
    double x = q / p.a, y = -static_cast<double>(p.c) / q;
    answer = {std::min(x, y), std::max(x, y)};
    return true;
}

std::vector<Interval> feasible(const Data &data) {
    auto [distance, height, thickness, diameter, vx, vy, ux, uy] = data;
    double lo = 0, hi = std::min(2.0 * vy / GRAVITY, static_cast<double>(distance) / vx);
    auto face = [&](Integer x, Integer level) {
        return Polynomial{HALF_GRAVITY * (ux * ux + vx * vx),
                          vy * ux * ux - uy * vx * ux + GRAVITY * x * vx,
                          uy * x * ux - HALF_GRAVITY * x * x - level * ux * ux};
    };
    for (Integer x : {distance, distance + thickness}) {
        Interval pair;
        if (!roots(face(x, height), pair))
            return {};
        lo = std::max(lo, pair.first);
        hi = std::min(hi, pair.second);
        if (lo >= hi)
            return {};
    }
    Integer ceiling = height + diameter;
    double before = static_cast<double>(GRAVITY * distance - ux * uy) / (GRAVITY * vx);
    double after = static_cast<double>(GRAVITY * (distance + thickness) - ux * uy) / (GRAVITY * vx);
    std::vector<Piece> pieces{
        {lo, std::min(hi, before), face(distance, ceiling)},
        {std::max(lo, before),
         std::min(hi, after),
         {GRAVITY * GRAVITY, 2 * GRAVITY * vy, uy * uy - 2 * GRAVITY * ceiling}},
        {std::max(lo, after), hi, face(distance + thickness, ceiling)}};
    bool found = false;
    double bad_lo = hi, bad_hi = lo;
    for (const auto &piece : pieces) {
        Interval pair;
        if (piece.left > piece.right || !roots(piece.polynomial, pair))
            continue;
        double a = std::max(piece.left, pair.first), b = std::min(piece.right, pair.second);
        if (a <= b) {
            found = true;
            bad_lo = std::min(bad_lo, a);
            bad_hi = std::max(bad_hi, b);
        }
    }
    if (!found)
        return {{lo, hi}};
    std::vector<Interval> answer;
    if (lo < bad_lo)
        answer.push_back({lo, bad_lo});
    if (bad_hi < hi)
        answer.push_back({bad_hi, hi});
    return answer;
}

double solve(const Data &data) {
    double best_width = 2 * MARGIN, answer = -1;
    for (auto [lo, hi] : feasible(data)) {
        if (hi - lo > best_width) {
            best_width = hi - lo;
            answer = (lo + hi) / 2;
        }
    }
    return answer;
}

void run(std::istream &in, std::ostream &out) {
    Data data;
    for (auto &value : data)
        in >> value;
    out << std::setprecision(OUTPUT_DIGITS) << solve(data) << '\n';
}

int main() {
    run(std::cin, std::cout);
    return 0;
}
