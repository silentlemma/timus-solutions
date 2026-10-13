#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

// from the centre, r1 reaches the farthest point and r2 reaches across it:
// area / (pi r1 r2) is 1 for any oval and 2 / pi for a square, and
// area / (pi r1^2) is 2 / pi for a square, at most 0.41 for a triangle
const double OVAL = 0.8, SQUARE = 0.5;
const double HALF = 0.5; // a pixel reaches half a pixel beyond its centre

int main() {
    int w = 0, h = 0;
    if (scanf("%d %d", &w, &h) != 2)
        return 0;
    std::vector<std::pair<double, double>> ends; // the first and last pixel of each row
    double count = 0, sx = 0, sy = 0;
    for (int y = 0; y < h; y++) {
        int first = -1, last = -1;
        for (int x = 0; x < w; x++) {
            int ch = getchar();
            while (ch != '0' && ch != '1')
                ch = getchar();
            if (ch == '1') {
                if (first < 0)
                    first = x;
                last = x;
                count++;
                sx += x;
                sy += y;
            }
        }
        if (first >= 0) {
            ends.push_back({first, y});
            ends.push_back({last, y});
        }
    }
    double cx = sx / count, cy = sy / count;
    std::pair<double, double> far = ends[0];
    for (const auto &p : ends)
        if (std::hypot(p.first - cx, p.second - cy) > std::hypot(far.first - cx, far.second - cy))
            far = p;
    double r1 = std::hypot(far.first - cx, far.second - cy);
    double ux = (far.first - cx) / r1, uy = (far.second - cy) / r1, r2 = 0;
    for (const auto &p : ends)
        r2 = std::max(r2, std::fabs((p.second - cy) * ux - (p.first - cx) * uy));
    double pi = std::acos(-1.0);
    if (count / (pi * (r1 + HALF) * (r2 + HALF)) > OVAL)
        puts("circle");
    else if (count / (pi * (r1 + HALF) * (r1 + HALF)) > SQUARE)
        puts("square");
    else
        puts("triangle");
    return 0;
}
