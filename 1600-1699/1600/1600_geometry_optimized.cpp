#include <array>
#include <cmath>
#include <cstdint>
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

constexpr int cent_scale = 100;
constexpr std::int64_t cent_limit = std::int64_t{1} << 40;

constexpr int input_capacity = 4096;
unsigned char input_data[input_capacity];
int input_position = 0, input_available = 0;
int input_byte() {
    if (input_position == input_available) {
        input_available = static_cast<int>(std::fread(input_data, 1, input_capacity, stdin));
        input_position = 0;
        if (input_available == 0)
            return EOF;
    }
    return input_data[input_position++];
}
bool next_token(char *token) {
    int ch = input_byte();
    while (ch != EOF && ch <= ' ')
        ch = input_byte();
    if (ch == EOF)
        return false;
    int length = 0;
    while (ch > ' ') {
        if (length + 1 >= token_size)
            return false;
        token[length++] = static_cast<char>(ch);
        ch = input_byte();
    }
    token[length] = 0;
    return true;
}

struct Object {
    std::array<Real, components> values;
    std::array<std::int64_t, components> cents{};
    bool cent_grid = true;
};

void cache_cent(Object &object, int index, const char *token) {
    if (!object.cent_grid)
        return;
    const Real value = object.values[index], scaled = value * cent_scale;
    if (!(scaled >= -cent_limit && scaled <= cent_limit) || (value == 0 && token[0] == '-')) {
        object.cent_grid = false;
        return;
    }
    const auto integer = static_cast<std::int64_t>(static_cast<double>(scaled));
    object.cents[index] = integer;
    object.cent_grid &= value == static_cast<Real>(integer) / cent_scale;
}

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

bool not_approaching(const Object &a, const Object &b) {
    // Certified cents have magnitude at most two to the fortieth power.
    // Their differences and three-product sum fit signed 128-bit arithmetic.
    __int128 projection = 0;
    for (int i = 0; i < dimensions; ++i) {
        const auto position = b.cents[i] - a.cents[i];
        const auto velocity = b.cents[i + dimensions] - a.cents[i + dimensions];
        projection += static_cast<__int128>(position) * velocity;
    }
    return projection > 0;
}

double arrival(const Object &a, const Object &b, Real limit, double fast_limit) {
    std::array<Real, dimensions> position, velocity;
    std::array<double, dimensions> p, v;
    const bool cent_pair = a.cent_grid && b.cent_grid;
    if (cent_pair && not_approaching(a, b)) {
        // Starting outside the critical radius, squared distance never decreases.
        return std::numeric_limits<double>::infinity();
    }
    if (cent_pair) {
        // Bounded canonical cents give the same rounded double differences.
        // Ambiguous geometry still uses the original Real values below.
        for (int i = 0; i < dimensions; ++i) {
            p[i] = static_cast<double>(b.cents[i] - a.cents[i]) / cent_scale;
            v[i] =
                static_cast<double>(b.cents[i + dimensions] - a.cents[i + dimensions]) / cent_scale;
        }
    } else {
        for (int i = 0; i < dimensions; ++i) {
            position[i] = b.values[i] - a.values[i];
            velocity[i] = b.values[i + dimensions] - a.values[i + dimensions];
            p[i] = static_cast<double>(position[i]);
            v[i] = static_cast<double>(velocity[i]);
        }
    }
    const double infinity = std::numeric_limits<double>::infinity();
    const double length = dot(p, p), speed = dot(v, v);
    const double projection = dot(p, v);
    const double target = fast_limit * speed;
    const double loss = perpendicular_loss(p, v);
    const double discriminant = target - loss;
    const double gap = length - fast_limit;
    const double scale = length * speed;
    if (projection > rounding_margin * std::sqrt(scale) || speed == 0) {
        return infinity;
    }
    if (projection < -rounding_margin * std::sqrt(scale) &&
        std::abs(discriminant) > rounding_margin * (target + loss + scale) &&
        gap > rounding_margin * (length + fast_limit)) {
        return discriminant < 0 ? infinity : gap / (std::sqrt(discriminant) - projection);
    }
    if (cent_pair) {
        for (int i = 0; i < dimensions; ++i) {
            position[i] = b.values[i] - a.values[i];
            velocity[i] = b.values[i + dimensions] - a.values[i + dimensions];
        }
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
    if (!next_token(token)) {
        return 0;
    }
    count = std::atoi(token);
    if (!next_token(token))
        return 0;
    const Real distance = read_decimal(token);
    const Real limit = distance * distance;
    const double fast_limit = static_cast<double>(limit);
    std::vector<Object> objects(count);
    for (auto &object : objects) {
        for (int i = 0; i < components; ++i) {
            if (!next_token(token)) {
                return 0;
            }
            object.values[i] = read_decimal(token);
            cache_cent(object, i, token);
        }
    }
    double earliest = std::numeric_limits<double>::infinity();
    int first = 0, second = 0;
    for (int i = 0; i < count; ++i) {
        for (int j = i + 1; j < count; ++j) {
            const double time = arrival(objects[i], objects[j], limit, fast_limit);
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
