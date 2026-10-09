#include <algorithm>
#include <cstdio>
#include <iostream>
#include <set>
#include <vector>

const int JURY = 255;

struct Plot {
    int w, s, x, y;
};

int main() {
    int size, park, m;
    if (!(std::cin >> size >> park >> m))
        return 0;
    std::vector<Plot> plots(m);
    for (auto &p : plots)
        std::cin >> p.w >> p.s >> p.x >> p.y;
    int top = size - park + 1;
    // sliding the park left only drops plots until its left side reaches a
    // plot's right side or the border, so only those positions are tried
    std::set<int> xs{1}, ys{1};
    for (const auto &p : plots) {
        if (p.x + p.s <= top)
            xs.insert(p.x + p.s);
        if (p.y + p.s <= top)
            ys.insert(p.y + p.s);
    }
    int best = JURY;
    for (int px : xs)
        for (int py : ys) {
            int worst = 1;
            for (const auto &p : plots)
                if (px < p.x + p.s && p.x < px + park && py < p.y + p.s && p.y < py + park)
                    worst = std::max(worst, p.w);
            best = std::min(best, worst);
        }
    if (best == JURY)
        puts("IMPOSSIBLE");
    else
        printf("%d\n", best);
}
