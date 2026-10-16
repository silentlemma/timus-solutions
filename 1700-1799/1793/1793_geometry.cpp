#include <algorithm>
#include <iostream>

int main() {
    long long a, b, d, r1, top1, r2, top2, h;
    if (!(std::cin >> a >> b >> d >> r1 >> top1 >> r2 >> top2 >> h)) return 0;
    // the widest part of a plate inside the borders, at height min(d, h),
    // scaled by h to stay in integers
    long long low = std::min(d, h);
    long long w1 = r1 * h + (top1 - r1) * low, w2 = r2 * h + (top2 - r2) * low;
    bool fits = 2 * w1 <= a * h && 2 * w1 <= b * h && 2 * w2 <= a * h && 2 * w2 <= b * h;
    // the centres can be this far apart along each side, and the plates
    // must be at least top1 + top2 apart, where they are widest
    long long dx = a * h - w1 - w2, dy = b * h - w1 - w2, need = (top1 + top2) * h;
    bool apart = dx * dx + dy * dy >= need * need;
    std::cout << (fits && apart ? "YES" : "NO") << "\n";
    return 0;
}
