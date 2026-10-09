#include <cmath>
#include <cstdio>

struct Vec {
    long long x, y, z;
    Vec operator-(const Vec &o) const { return {x - o.x, y - o.y, z - o.z}; }
    long long dot(const Vec &o) const { return x * o.x + y * o.y + z * o.z; }
    Vec cross(const Vec &o) const {
        return {y * o.z - z * o.y, z * o.x - x * o.z, x * o.y - y * o.x};
    }
    double norm() const { return std::sqrt((double)dot(*this)); }
};

Vec read() {
    Vec v{0, 0, 0};
    scanf("%lld %lld %lld", &v.x, &v.y, &v.z);
    return v;
}

int main() {
    Vec a = read(), b = read(), c = read();
    long long r = 0;
    scanf("%lld", &r);
    Vec u = a - c, v = b - c;
    double angle = std::atan2(u.cross(v).norm(), (double)u.dot(v));
    double da = u.norm(), db = v.norm();
    // seen from C, the tangents from A and B cover these angles; when the angle
    // ACB fits in them, the segment AB misses the ball
    double reach = std::acos(r / da) + std::acos(r / db);
    double length = (a - b).norm();
    if (angle > reach)
        length = std::sqrt(da * da - r * r) + std::sqrt(db * db - r * r) + r * (angle - reach);
    printf("%.2f\n", length);
}
