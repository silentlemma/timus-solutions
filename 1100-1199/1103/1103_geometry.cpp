#include <algorithm>
#include <cstdio>
#include <vector>

struct Point {
    long long x, y;
    bool operator==(const Point &o) const { return x == o.x && y == o.y; }
};

long long cross(Point o, Point a, Point b) {
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<Point> pts(n);
    for (auto &p : pts)
        scanf("%lld %lld", &p.x, &p.y);
    // A is the lowest point and B the next one on the hull, so every other
    // point lies on the left of AB and sees it under an angle below 180
    Point a = *std::min_element(pts.begin(), pts.end(), [](Point p, Point q) {
        return p.y != q.y ? p.y < q.y : p.x < q.x;
    });
    std::vector<Point> rest;
    for (auto p : pts)
        if (!(p == a))
            rest.push_back(p);
    Point b = rest[0];
    for (auto p : rest)
        if (cross(a, b, p) < 0)
            b = p;
    std::vector<Point> others;
    for (auto p : rest)
        if (!(p == b))
            others.push_back(p);
    // the angle APB grows as its cotangent dot / cross falls; the products
    // reach 10^33, hence 128 bits
    auto smaller_angle = [&](Point p, Point q) {
        long long dp = (a.x - p.x) * (b.x - p.x) + (a.y - p.y) * (b.y - p.y);
        long long dq = (a.x - q.x) * (b.x - q.x) + (a.y - q.y) * (b.y - q.y);
        return (__int128)dp * cross(q, a, b) > (__int128)dq * cross(p, a, b);
    };
    size_t mid = others.size() / 2;
    std::nth_element(others.begin(), others.begin() + mid, others.end(), smaller_angle);
    // points seeing AB under a larger angle than C lie inside the circle ABC
    Point c = others[mid];
    printf("%lld %lld\n%lld %lld\n%lld %lld\n", a.x, a.y, b.x, b.y, c.x, c.y);
}
