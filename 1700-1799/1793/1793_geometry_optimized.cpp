#include <algorithm>
#include <cstdio>

constexpr int FIELDS = 8;

bool fits(int a, int b, int border, int r1, int top1, int r2, int top2, int height) {
    const int level = std::min(border, height);
    const int w1 = r1 * height + (top1 - r1) * level;
    const int w2 = r2 * height + (top2 - r2) * level;
    // Both scaled diameters must fit along the shorter side of the tray.
    if (2 * std::max(w1, w2) > std::min(a, b) * height) {
        return false;
    }
    const long long dx = a * height - w1 - w2;
    const long long dy = b * height - w1 - w2;
    const long long separation = (top1 + top2) * height;
    return dx * dx + dy * dy >= separation * separation;
}

int main() {
    int a, b, border, r1, top1, r2, top2, height;
    if (std::scanf("%d%d%d%d%d%d%d%d", &a, &b, &border, &r1, &top1, &r2, &top2, &height) ==
        FIELDS) {
        std::puts(fits(a, b, border, r1, top1, r2, top2, height) ? "YES" : "NO");
    }
}
