#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>

const int MAX_ROPE = 30000;

int main() {
    long long ax = 0, ay = 0, bx = 0, by = 0, cx = 0, cy = 0, rope = 0;
    std::string token;
    if (!(std::cin >> ax >> ay >> bx >> by >> cx >> cy >> token))
        return 0;
    for (char digit : token) {
        if (digit < '0' || digit > '9')
            continue;
        rope = std::min(static_cast<long long>(MAX_ROPE), rope * 10 + digit - '0');
        if (rope == MAX_ROPE)
            break;
    }
    long long dx = bx - ax, dy = by - ay, length = dx * dx + dy * dy;
    // the nearest point of the bed: C projected onto AB, kept inside it
    double t = 0;
    if (length != 0)
        t = std::max(0.0, std::min(1.0, double((cx - ax) * dx + (cy - ay) * dy) / length));
    double nearest = std::hypot(ax + t * dx - cx, ay + t * dy - cy);
    double farthest = std::max(std::hypot(double(ax - cx), double(ay - cy)),
                               std::hypot(double(bx - cx), double(by - cy)));
    printf("%.2f\n%.2f\n", std::max(0.0, nearest - rope), std::max(0.0, farthest - rope));
    return 0;
}
