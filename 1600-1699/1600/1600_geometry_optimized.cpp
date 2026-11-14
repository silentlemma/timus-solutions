#include <array>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <limits>
#include <vector>

constexpr int dimensions = 3;
constexpr int components = 2 * dimensions;
constexpr int token_size = 128;
constexpr int decimal_base = 10;
constexpr double rounding_margin = 64 * std::numeric_limits<double>::epsilon();
using Real = __float128;
constexpr Real precise_margin = 1e-31L;

struct Object {
    std::array<Real, components> values;
};

// Parse the decimal digits before rounding to double precision for the fast path.
Real read_decimal(const char *token) {
    const bool negative = *token == '-';
    if (*token == '-' || *token == '+') {
        ++token;
    }
    Real mantissa = 0;
    int fractional = 0;
    bool after_point = false;
    while (*token != '\0' && *token != 'e' && *token != 'E') {
        if (*token == '.') {
            after_point = true;
        } else {
            mantissa = mantissa * decimal_base + (*token - '0');
            fractional += after_point;
        }
        ++token;
    }
    int exponent = (*token == '\0' ? 0 : std::atoi(token + 1)) - fractional;
    const bool divide = exponent < 0;
    Real scale = 1;
    for (Real power = decimal_base; exponent != 0; exponent /= 2) {
        if (exponent % 2 != 0) {
            scale *= power;
        }
        if (exponent / 2 != 0) {
            power *= power;
        }
    }
    const Real value = divide ? mantissa / scale : mantissa * scale;
    return negative ? -value : value;
}

template <typename T>
T dot(const std::array<T, dimensions> &a, const std::array<T, dimensions> &b) {
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
}

template <typename T>
T perpendicular_loss(const std::array<T, dimensions> &p, const std::array<T, dimensions> &v) {
    std::array<T, dimensions> cross{p[1] * v[2] - p[2] * v[1], p[2] * v[0] - p[0] * v[2],
                                    p[0] * v[1] - p[1] * v[0]};
    return dot(cross, cross);
}

double arrival(const Object &a, const Object &b, Real limit) {
    std::array<Real, dimensions> position, velocity;
    std::array<double, dimensions> p, v;
    for (int i = 0; i < dimensions; ++i) {
        position[i] = b.values[i] - a.values[i];
        velocity[i] = b.values[i + dimensions] - a.values[i + dimensions];
        p[i] = static_cast<double>(position[i]);
        v[i] = static_cast<double>(velocity[i]);
    }
    const double infinity = std::numeric_limits<double>::infinity();
    const double length = dot(p, p), speed = dot(v, v);
    const double projection = dot(p, v);
    const double target = static_cast<double>(limit) * speed;
    const double loss = perpendicular_loss(p, v);
    const double discriminant = target - loss;
    const double gap = length - static_cast<double>(limit);
    const double scale = length * speed;
    if (projection > rounding_margin * std::sqrt(scale) || speed == 0) {
        return infinity;
    }
    if (projection < -rounding_margin * std::sqrt(scale) &&
        std::abs(discriminant) > rounding_margin * (target + loss + scale) &&
        gap > rounding_margin * (length + static_cast<double>(limit))) {
        return discriminant < 0 ? infinity : gap / (std::sqrt(discriminant) - projection);
    }
    const Real precise_projection = dot(position, velocity);
    if (precise_projection >= 0) {
        return infinity;
    }
    // The cross product gives the squared separation at closest approach.
    const Real precise_target = limit * dot(velocity, velocity);
    const Real precise_loss = perpendicular_loss(position, velocity);
    const Real precise_discriminant = precise_target - precise_loss;
    if (precise_discriminant < -precise_margin * (precise_target + precise_loss)) {
        return infinity;
    }
    const long double root =
        precise_discriminant > 0 ? std::sqrt(static_cast<long double>(precise_discriminant)) : 0;
    return static_cast<double>(dot(position, position) - limit) /
           static_cast<double>(root - precise_projection);
}

int main() {
    int count;
    char token[token_size];
    if (std::scanf("%d %127s", &count, token) != 2) {
        return 0;
    }
    const Real distance = read_decimal(token);
    const Real limit = distance * distance;
    std::vector<Object> objects(count);
    for (auto &object : objects) {
        for (auto &value : object.values) {
            if (std::scanf("%127s", token) != 1) {
                return 0;
            }
            value = read_decimal(token);
        }
    }
    double earliest = std::numeric_limits<double>::infinity();
    int first = 0, second = 0;
    for (int i = 0; i < count; ++i) {
        for (int j = i + 1; j < count; ++j) {
            const double time = arrival(objects[i], objects[j], limit);
            if (time >= 0 && time < earliest) {
                earliest = time;
                first = i + 1;
                second = j + 1;
            }
        }
    }
    if (first == 0) {
        std::puts("OK");
    } else {
        std::printf("ALARM!\n%.3f %d %d\n", earliest, first, second);
    }
}
