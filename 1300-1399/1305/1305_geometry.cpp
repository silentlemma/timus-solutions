#include <algorithm>
#include <climits>
#include <cstdio>
#include <utility>
#include <vector>

typedef std::pair<int, int> Point;

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    int minX = INT_MAX, maxX = INT_MIN, minY = INT_MAX, maxY = INT_MIN;
    int minS = INT_MAX, maxS = INT_MIN, minD = INT_MAX, maxD = INT_MIN;
    for (int i = 0; i < n; i++) {
        int x = 0, y = 0;
        if (scanf("%d %d", &x, &y) != 2)
            break;
        minX = std::min(minX, x);
        maxX = std::max(maxX, x);
        minY = std::min(minY, y);
        maxY = std::max(maxY, y);
        minS = std::min(minS, x + y);
        maxS = std::max(maxS, x + y);
        minD = std::min(minD, x - y);
        maxD = std::max(maxD, x - y);
    }
    // the hull is cut out by eight lines, x, y, x + y and x - y each at
    // their extremes; going counterclockwise from the bottom edge, every
    // corner joins an axis line to a diagonal one
    Point corners[] = {
        {minS - minY, minY}, {maxD + minY, minY}, {maxX, maxX - maxD}, {maxX, maxS - maxX},
        {maxS - maxY, maxY}, {minD + maxY, maxY}, {minX, minX - minD}, {minX, minS - minX},
    };
    std::vector<Point> hull;
    for (const Point &p : corners) {
        if (hull.empty() || hull.back() != p)
            hull.push_back(p);
    }
    while (hull.size() > 1 && hull.front() == hull.back())
        hull.pop_back();
    // the sides left all point in different directions, so no corner is in
    // the middle of a straight side
    for (const Point &p : hull)
        printf("%d %d\n", p.first, p.second);
    return 0;
}
