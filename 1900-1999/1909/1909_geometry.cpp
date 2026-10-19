#include <cstdint>
#include <iostream>

using Wide = __int128;

struct Vector {
    Wide x, y, z;
};

Wide dot(Vector a, Vector b) { return a.x * b.x + a.y * b.y + a.z * b.z; }

Vector subtract(Vector a, Vector b) { return {a.x - b.x, a.y - b.y, a.z - b.z}; }

Vector scale(Vector a, Wide factor) { return {a.x * factor, a.y * factor, a.z * factor}; }

Vector cross(Vector a, Vector b) {
    return {a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x};
}

int sign(Wide value) { return (value > 0) - (value < 0); }

int projection_sign(Vector point, Vector edge, Vector velocity, Wide a, Wide b,
                    Wide plane_discriminant, Wide radius_squared) {
    const Wide x = dot(edge, point), y = dot(edge, velocity);
    if (y == 0)
        return sign(x);
    const Wide numerator = y > 0 ? -x : x;
    const Wide denominator = y > 0 ? y : -y;
    const Wide vertex_offset = a * numerator + b * denominator;
    int comparison;
    if (vertex_offset >= 0) {
        comparison = vertex_offset == 0 && plane_discriminant == 0 ? 0 : -1;
    } else {
        const Vector scaled = subtract(scale(point, y), scale(velocity, x));
        comparison = sign(dot(scaled, scaled) - radius_squared * y * y);
    }
    return comparison * sign(y);
}

bool ray_hits(Vector point, Vector velocity, Wide radius_squared) {
    const Wide projection = dot(point, velocity);
    return projection < 0 && projection * projection >=
                                 dot(velocity, velocity) * (dot(point, point) - radius_squared);
}

const char *classify(Vector center, Wide radius, Vector first, Vector second, Vector velocity) {
    const Vector left = subtract(first, center), right = subtract(second, center);
    const Vector edge = subtract(right, left);
    const Vector normal = cross(edge, velocity), offset = cross(edge, left);
    const Wide radius_squared = radius * radius;
    const Wide a = dot(normal, normal), b = dot(offset, normal);
    const Wide c = dot(offset, offset) - radius_squared * dot(edge, edge);
    if (a != 0 && c > 0 && b < 0) {
        const Wide height = dot(left, normal);
        const Wide plane_discriminant = radius_squared * a - height * height;
        if (plane_discriminant >= 0) {
            const int left_sign =
                projection_sign(left, edge, velocity, a, b, plane_discriminant, radius_squared);
            const int right_sign =
                projection_sign(right, edge, velocity, a, b, plane_discriminant, radius_squared);
            if (left_sign < 0 && right_sign > 0)
                return "Warning";
        }
    }
    if (ray_hits(left, velocity, radius_squared) || ray_hits(right, velocity, radius_squared))
        return "Crash";
    return "False alarm";
}

Vector read_vector() {
    int64_t x, y, z;
    std::cin >> x >> y >> z;
    return {x, y, z};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    const Vector center = read_vector();
    int64_t radius;
    std::cin >> radius;
    const Vector first = read_vector(), second = read_vector(), velocity = read_vector();
    std::cout << classify(center, radius, first, second, velocity) << '\n';
}
