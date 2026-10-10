#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

// the colour of the white sheet
const int WHITE = 1;
// colours are at most this
const int COLOURS = 2500;
// the first line holds A, B and N, and a rectangle is five numbers
const int HEADER = 3, FIELDS = 5;

struct Rect {
    int x1, y1, x2, y2, colour;
};

int main() {
    int width, height, n;
    if (scanf("%d %d %d", &width, &height, &n) != HEADER)
        return 0;
    std::vector<Rect> rects(n);
    std::vector<int> xs = {0, width}, ys = {0, height};
    for (auto &r : rects) {
        if (scanf("%d %d %d %d %d", &r.x1, &r.y1, &r.x2, &r.y2, &r.colour) != FIELDS)
            return 0;
        xs.insert(xs.end(), {r.x1, r.x2});
        ys.insert(ys.end(), {r.y1, r.y2});
    }
    for (auto *v : {&xs, &ys}) {
        std::sort(v->begin(), v->end());
        v->erase(std::unique(v->begin(), v->end()), v->end());
    }
    auto at = [&](int c) { return int(std::lower_bound(ys.begin(), ys.end(), c) - ys.begin()); };
    std::vector<long long> area(COLOURS + 1, 0);
    std::vector<int> skip(ys.size());
    auto find = [&](int j) {
        while (skip[j] != j)
            j = skip[j] = skip[skip[j]];
        return j;
    };
    for (size_t i = 0; i + 1 < xs.size(); i++) {
        long long strip = xs[i + 1] - xs[i];
        // the top rectangles paint the cells of this strip first, and skip[j]
        // leads past painted cells to the next unpainted one
        std::iota(skip.begin(), skip.end(), 0);
        long long painted = 0;
        for (int k = n - 1; k >= 0 && painted < height; k--) {
            const Rect &r = rects[k];
            if (r.x1 > xs[i] || r.x2 < xs[i + 1])
                continue;
            int hi = at(r.y2);
            long long got = 0;
            for (int j = find(at(r.y1)); j < hi; j = find(j + 1)) {
                got += ys[j + 1] - ys[j];
                skip[j] = j + 1;
            }
            area[r.colour] += got * strip;
            painted += got;
        }
        area[WHITE] += (height - painted) * strip;
    }
    for (int c = 1; c <= COLOURS; c++)
        if (area[c])
            printf("%d %lld\n", c, area[c]);
}
