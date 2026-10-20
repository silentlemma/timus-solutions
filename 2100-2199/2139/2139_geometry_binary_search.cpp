#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using Integer = std::int64_t;
constexpr Integer SCALE = 1000;
constexpr Integer AREA_SCALE = SCALE * SCALE;
constexpr Integer FULL_TURN = 360000;
constexpr Integer HALF_TURN = FULL_TURN / 2;
constexpr Integer QUARTER_TURN = HALF_TURN / 2;
constexpr Integer OCTANT = QUARTER_TURN / 2;
constexpr int OUTPUT_DIGITS = 6;
constexpr double PI = 3.141592653589793;
constexpr double ANGLE_EPSILON = 1e-11;
constexpr double SIN_COEFFICIENTS[] = {
    2.8114572543455206e-15, -7.647163731819816e-13, 1.6059043836821613e-10,
    -2.505210838544172e-8,  2.7557319223985893e-6,  -0.0001984126984126984,
    0.008333333333333333,   -0.16666666666666666,   1.0};
constexpr double COS_COEFFICIENTS[] = {-1.5619206968586225e-16,
                                       4.779477332387385e-14,
                                       -1.1470745597729725e-11,
                                       2.08767569878681e-9,
                                       -2.755731922398589e-7,
                                       2.48015873015873e-5,
                                       -0.001388888888888889,
                                       0.041666666666666664,
                                       -0.5,
                                       1.0};

Integer read_fixed() {
    std::string token;
    std::cin >> token;
    Integer value = 0;
    for (char c : token) {
        if (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
        }
    }
    return token[0] == '-' ? -value : value;
}

std::pair<double, double> sine_cosine(Integer angle) {
    angle = (angle % FULL_TURN + FULL_TURN) % FULL_TURN;
    Integer quadrant = angle / QUARTER_TURN;
    Integer reduced = angle % QUARTER_TURN;
    bool mirror = reduced > OCTANT;
    if (mirror) {
        reduced = QUARTER_TURN - reduced;
    }
    double x = reduced * (PI / HALF_TURN);
    double squared = x * x;
    double sine = 0;
    double cosine = 0;
    // Identical polynomial evaluation keeps all language versions in agreement.
    for (double coefficient : SIN_COEFFICIENTS) {
        sine = sine * squared + coefficient;
    }
    for (double coefficient : COS_COEFFICIENTS) {
        cosine = cosine * squared + coefficient;
    }
    sine = x * sine;
    if (reduced == OCTANT) {
        sine = cosine;
    }
    if (mirror) {
        std::swap(sine, cosine);
    }
    if (quadrant == 0) {
        return {sine, cosine};
    }
    if (quadrant == 1) {
        return {cosine, -sine};
    }
    if (quadrant == 2) {
        return {-sine, -cosine};
    }
    return {-cosine, sine};
}

struct Point {
    Integer x, y;
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    std::vector<Point> points(n);
    for (auto &p : points) {
        p = {read_fixed(), read_fixed()};
    }
    Integer hole_x = read_fixed();
    Integer hole_y = read_fixed();
    for (auto &p : points) {
        p.x -= hole_x;
        p.y -= hole_y;
    }
    int start = 0;
    for (int i = 0; i < n; ++i) {
        const auto &a = points[i];
        const auto &b = points[(i + 1) % n];
        if (a.x * b.y - a.y * b.x == 0 && a.x * b.x + a.y * b.y < 0) {
            start = (i + 1) % n;
            break;
        }
    }
    std::rotate(points.begin(), points.begin() + start, points.end());
    std::vector<Integer> prefix(n);
    for (int i = 0; i + 1 < n; ++i) {
        prefix[i + 1] = prefix[i] + points[i].x * points[i + 1].y - points[i].y * points[i + 1].x;
    }
    Integer total = prefix.back();
    auto capacity = [&](Integer angle) {
        auto [sine, cosine] = sine_cosine(angle);
        auto height = [&](int i) { return points[i].x * sine + points[i].y * cosine; };
        double first = height(0);
        if (first == 0) {
            return points[0].x * cosine - points[0].y * sine < 0 ? double(total) : 0.0;
        }
        bool below = first < 0;
        int low = 0, high = n - 1;
        while (high - low > 1) {
            int middle = (low + high) / 2;
            if ((height(middle) < 0) == below) {
                low = middle;
            } else {
                high = middle;
            }
        }
        double left = height(low), right = height(high);
        double fraction = std::clamp(left / (left - right), 0.0, 1.0);
        Integer triangle = prefix[high] - prefix[low];
        if (below) {
            return double(prefix[low]) + fraction * double(triangle);
        }
        return double(total - prefix[high]) + (1.0 - fraction) * double(triangle);
    };
    bool empty = points[0].y == 0 && points[0].x > 0;
    double zero = -std::atan2(double(points[0].y), double(points[0].x)) * (HALF_TURN / PI);
    double lower = zero > 0 ? zero - FULL_TURN : zero;
    double upper = zero > 0 ? zero : zero + FULL_TURN;
    double remaining = empty ? 0.0 : capacity(0);
    auto record = [&]() {
        Integer units = Integer(remaining / 2 + 1.0 / 2);
        std::cout << units / AREA_SCALE << '.' << std::setfill('0') << std::setw(OUTPUT_DIGITS)
                  << units % AREA_SCALE << "000\n";
    };
    record();
    int queries;
    std::cin >> queries;
    Integer angle = 0;
    for (int i = 0; i < queries; ++i) {
        angle += read_fixed();
        if (!empty) {
            // A swept interval reaching either empty orientation loses all juice.
            if (angle <= lower + ANGLE_EPSILON || angle >= upper - ANGLE_EPSILON) {
                empty = true;
                remaining = 0;
            } else {
                remaining = std::min(remaining, capacity(angle));
            }
        }
        record();
    }
}
