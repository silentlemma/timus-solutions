#include <algorithm>
#include <array>
#include <cstdio>
#include <vector>
using namespace std;

typedef array<long long, 2> Point;
struct Line {
    long long a, b, c;  // a x + b y = c
};

const int CORNERS = 3;
const int GLIDE = 3;  // a glide reflection takes three reflections
const int NONE = -1;

long long cross(const Point &o, const Point &a, const Point &b) {
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
}

long long dist2(const Point &p, const Point &q) {
    return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1]);
}

// the line of points as far from p as from q
Line bisector(const Point &p, const Point &q) {
    return {2 * (q[0] - p[0]), 2 * (q[1] - p[1]), dist2(q, {0, 0}) - dist2(p, {0, 0})};
}

bool sameLine(const Line &u, const Line &v) {
    return u.a * v.b == u.b * v.a && u.a * v.c == u.c * v.a && u.b * v.c == u.c * v.b;
}

// reflections taking cur[i] to to[i], or NONE when no isometry does
int moves(const vector<Point> &cur, const vector<Point> &to) {
    for (int i = 0; i < CORNERS; i++)
        for (int j = i + 1; j < CORNERS; j++)
            if (dist2(cur[i], cur[j]) != dist2(to[i], to[j]))
                return NONE;
    if (cur == to)
        return 0;
    if ((cross(cur[0], cur[1], cur[2]) > 0) == (cross(to[0], to[1], to[2]) > 0))
        return 2;  // a rotation or a translation: two reflections
    // orientation reversed: one reflection if a single mirror fits all three
    vector<Line> lines;
    vector<Point> fixed;
    for (int i = 0; i < CORNERS; i++) {
        if (cur[i] == to[i])
            fixed.push_back(cur[i]);
        else
            lines.push_back(bisector(cur[i], to[i]));
    }
    const Line &mirror = lines[0];
    for (const Line &line : lines)
        if (!sameLine(mirror, line))
            return GLIDE;
    for (const Point &p : fixed)
        if (mirror.a * p[0] + mirror.b * p[1] != mirror.c)
            return GLIDE;
    return 1;
}

int main() {
    vector<Point> target(CORNERS), cur(CORNERS);
    for (Point &p : target)
        if (scanf("%lld %lld", &p[0], &p[1]) != 2)
            return 0;
    for (Point &p : cur)
        if (scanf("%lld %lld", &p[0], &p[1]) != 2)
            return 0;
    vector<int> order = {0, 1, 2};
    int best = NONE;
    do {
        vector<Point> to(CORNERS);
        for (int i = 0; i < CORNERS; i++)
            to[i] = target[order[i]];
        int m = moves(cur, to);
        if (m != NONE && (best == NONE || m < best))
            best = m;
    } while (next_permutation(order.begin(), order.end()));
    if (best == NONE)
        puts("IMPOSSIBLE");
    else
        printf("%d\n", best);
}
