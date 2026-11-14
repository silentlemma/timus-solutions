#include <algorithm>
#include <cmath>
#include <cstdio>

struct Point {
    double x, y;
};

double distance(Point a, Point b) {
    const double dx = a.x - b.x, dy = a.y - b.y;
    const double squared = dx * dx + dy * dy;
    return std::isnormal(squared) ? std::sqrt(squared) : std::hypot(dx, dy);
}

int main() {
    constexpr int max_camps = 200;
    int count;
    if (scanf("%d", &count) != 1)
        return 0;

    Point cycle[2 * max_camps];
    double edge[2 * max_camps];
    for (int i = 0; i < count; ++i) {
        if (scanf("%lf %lf", &cycle[i].x, &cycle[i].y) != 2)
            return 0;
        cycle[i + count] = cycle[i];
    }
    for (int i = 0; i + 1 < 2 * count; ++i)
        edge[i] = distance(cycle[i], cycle[i + 1]);

    double left[max_camps + 1] = {}, right[max_camps + 1] = {};
    for (int span = 1; span < count; ++span) {
        // Preserve the cyclic successor before overwriting the first arc.
        left[count] = left[0];
        right[count] = right[0];
        for (int start = 0; start < count; ++start) {
            const int end = start + span;
            const double chord = distance(cycle[start], cycle[end]);
            const double next_left =
                std::min(left[start + 1] + edge[start], right[start + 1] + chord);
            right[start] = std::min(left[start] + chord, right[start] + edge[end - 1]);
            left[start] = next_left;
        }
    }
    printf("%.3f\n", std::min(*std::min_element(left, left + count),
                              *std::min_element(right, right + count)));
}
