#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <vector>

using Integer = std::int64_t;

constexpr double MAX_DISTANCE = 3.0e9;
constexpr double CLOSE_DISTANCE = 1.0e-5;
constexpr double SPLITTER = 134217729.0;
constexpr double PI_HIGH = 3.141592653589793;
constexpr double PI_LOW = 1.2246467991473532e-16;

struct DoubleDouble {
    double high;
    double low;

    static DoubleDouble integer(Integer value) {
        double high = static_cast<double>(value);
        return {high, static_cast<double>(value - static_cast<Integer>(high))};
    }
};

DoubleDouble operator+(DoubleDouble a, DoubleDouble b) {
    double sum = a.high + b.high;
    double part = sum - a.high;
    double error = (a.high - (sum - part)) + (b.high - part) + a.low + b.low;
    double high = sum + error;
    return {high, error - (high - sum)};
}

DoubleDouble operator-(DoubleDouble a, DoubleDouble b) { return a + DoubleDouble{-b.high, -b.low}; }

DoubleDouble operator*(DoubleDouble a, DoubleDouble b) {
    double product = a.high * b.high;
    double split_a = SPLITTER * a.high;
    double high_a = split_a - (split_a - a.high);
    double low_a = a.high - high_a;
    double split_b = SPLITTER * b.high;
    double high_b = split_b - (split_b - b.high);
    double low_b = b.high - high_b;
    double error = ((high_a * high_b - product) + high_a * low_b) + low_a * high_b;
    error += low_a * low_b + a.high * b.low + a.low * b.high;
    double high = product + error;
    return {high, error - (high - product)};
}

bool nonnegative(DoubleDouble value) {
    return value.high > 0 || (value.high == 0 && value.low >= 0);
}

struct Distance {
    double value;
    Integer base;
    Integer denominator;
    bool square;
};

struct Point {
    Integer x;
    Integer y;
};

Integer cross(Integer ax, Integer ay, Integer bx, Integer by) { return ax * by - ay * bx; }

class Polygon {
    std::vector<Point> vertices;
    std::vector<Integer> dx, dy, length_squared, rx, ry;
    std::vector<double> radii;
    std::vector<DoubleDouble> extras;
    double perimeter;
    int size;

    bool visible(int edge, Point query) const {
        return cross(dx[edge], dy[edge], query.x - vertices[edge].x, query.y - vertices[edge].y) <
               0;
    }

    Integer end_dot(int edge, Point query) const {
        int next = (edge + 1) % size;
        return (vertices[next].x - query.x) * dx[edge] + (vertices[next].y - query.y) * dy[edge];
    }

    Distance distance(Point query) const {
        bool first = visible(0, query);
        bool last = visible(size - 1, query);
        int hidden;
        int shown;
        if (first != last) {
            shown = first ? 0 : size - 1;
            hidden = first ? size - 1 : 0;
        } else {
            Integer qx = query.x - vertices[0].x;
            Integer qy = query.y - vertices[0].y;
            int low = 1;
            int high = size - 1;
            while (high - low > 1) {
                int middle = (low + high) / 2;
                Integer turn = cross(rx[middle], ry[middle], qx, qy);
                if (first ? turn <= 0 : turn >= 0) {
                    low = middle;
                } else {
                    high = middle;
                }
            }
            if (first) {
                shown = 0;
                hidden = low;
            } else {
                shown = low;
                if (!visible(shown, query)) {
                    return {0, 0, 1, false};
                }
                hidden = 0;
            }
        }

        Integer projection =
            (query.x - vertices[shown].x) * dx[shown] + (query.y - vertices[shown].y) * dy[shown];
        int closest = shown;
        // Restrict the derivative test to the visible chain to keep each search monotone.
        if (projection > length_squared[shown]) {
            int low = 0;
            int high = (hidden - shown + size) % size;
            while (high - low > 1) {
                int middle = (low + high) / 2;
                int edge = (shown + middle) % size;
                if (!visible(edge, query) || end_dot(edge, query) >= 0) {
                    high = middle;
                } else {
                    low = middle;
                }
            }
            closest = (shown + high) % size;
        } else if (projection < 0) {
            int low = 0;
            int high = (shown - hidden + size) % size;
            while (high - low > 1) {
                int middle = (low + high) / 2;
                int edge = (hidden + middle) % size;
                if (visible(edge, query) && end_dot(edge, query) >= 0) {
                    high = middle;
                } else {
                    low = middle;
                }
            }
            closest = (hidden + high) % size;
        }

        Integer qx = query.x - vertices[closest].x;
        Integer qy = query.y - vertices[closest].y;
        projection = qx * dx[closest] + qy * dy[closest];
        if (projection <= 0) {
            return {std::hypot(static_cast<double>(qx), static_cast<double>(qy)), qx * qx + qy * qy,
                    1, false};
        }
        if (projection >= length_squared[closest]) {
            int next = (closest + 1) % size;
            qx = query.x - vertices[next].x;
            qy = query.y - vertices[next].y;
            return {std::hypot(static_cast<double>(qx), static_cast<double>(qy)), qx * qx + qy * qy,
                    1, false};
        }
        Integer base = cross(dx[closest], dy[closest], qx, qy);
        return {std::abs(static_cast<double>(base)) /
                    std::sqrt(static_cast<double>(length_squared[closest])),
                base, length_squared[closest], true};
    }

    bool infected(int day, Distance separation) const {
        double difference = radii[day] - separation.value;
        if (std::abs(difference) > CLOSE_DISTANCE) {
            return difference > 0;
        }
        // Squared distance is numerator/denominator; compare areas without a square root.
        DoubleDouble numerator = DoubleDouble::integer(separation.base);
        if (separation.square) {
            numerator = numerator * numerator;
        }
        DoubleDouble denominator = DoubleDouble::integer(separation.denominator);
        DoubleDouble remainder =
            extras[day] * denominator - DoubleDouble{PI_HIGH, PI_LOW} * numerator;
        DoubleDouble boundary = DoubleDouble{perimeter, 0};
        DoubleDouble left = boundary * boundary * numerator * denominator;
        return nonnegative(remainder) && nonnegative(remainder * remainder - left);
    }

  public:
    explicit Polygon(const std::vector<Point> &input) {
        int count = static_cast<int>(input.size());
        for (int i = 0; i < count; ++i) {
            Point previous = input[(i + count - 1) % count];
            Point current = input[i];
            Point next = input[(i + 1) % count];
            if (cross(current.x - previous.x, current.y - previous.y, next.x - current.x,
                      next.y - current.y) != 0) {
                vertices.push_back(current);
            }
        }
        size = static_cast<int>(vertices.size());
        dx.resize(size);
        dy.resize(size);
        length_squared.resize(size);
        rx.resize(size);
        ry.resize(size);
        perimeter = 0;
        double correction = 0;
        Integer twice_area = 0;
        for (int i = 0; i < size; ++i) {
            int next = (i + 1) % size;
            dx[i] = vertices[next].x - vertices[i].x;
            dy[i] = vertices[next].y - vertices[i].y;
            length_squared[i] = dx[i] * dx[i] + dy[i] * dy[i];
            rx[i] = vertices[i].x - vertices[0].x;
            ry[i] = vertices[i].y - vertices[0].y;
            double adjusted =
                std::hypot(static_cast<double>(dx[i]), static_cast<double>(dy[i])) - correction;
            double total = perimeter + adjusted;
            correction = (total - perimeter) - adjusted;
            perimeter = total;
            if (i > 1) {
                twice_area += cross(rx[i - 1], ry[i - 1], rx[i], ry[i]);
            }
        }
        double area = static_cast<double>(twice_area) / 2;
        double half_perimeter = perimeter / 2;
        double multiplier = 1;
        double radius = 0;
        const double pi = std::acos(-1.0);
        DoubleDouble exact_area = DoubleDouble::integer(twice_area) * DoubleDouble{1.0 / 2, 0};
        DoubleDouble threshold = exact_area;
        radii.push_back(radius);
        extras.push_back({0, 0});
        // A + P*r + pi*r*r = A*2^day; use the stable positive root.
        while (radius <= MAX_DISTANCE) {
            threshold = threshold + threshold;
            extras.push_back(threshold - exact_area);
            multiplier *= 2;
            double extra = area * (multiplier - 1);
            radius =
                extra / (half_perimeter + std::sqrt(half_perimeter * half_perimeter + pi * extra));
            radii.push_back(radius);
        }
    }

    int day(Point query) const {
        Distance separation = distance(query);
        if (separation.value == 0) {
            return 0;
        }
        int result = static_cast<int>(
            std::lower_bound(radii.begin(), radii.end(), separation.value) - radii.begin());
        while (result > 0 && infected(result - 1, separation)) {
            --result;
        }
        while (!infected(result, separation)) {
            ++result;
        }
        return result;
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    std::vector<Point> vertices(count);
    for (Point &point : vertices) {
        std::cin >> point.x >> point.y;
    }
    Polygon polygon(vertices);
    int queries;
    std::cin >> queries;
    while (queries-- > 0) {
        Point query;
        std::cin >> query.x >> query.y;
        std::cout << polygon.day(query) << '\n';
    }
}
