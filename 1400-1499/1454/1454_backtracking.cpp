#include <cstdio>
#include <set>
#include <utility>
#include <vector>

using namespace std;

const int PIECES = 5;

struct Seg {
    int x, span, level;
};

int pw[PIECES], ph[PIECES], height;
bool used[PIECES];

// skyline filling: the lowest, then leftmost, stretch of the outline must
// hold the bottom-left corner of some piece in every tiling
bool fill(const vector<Seg> &sky, int left) {
    if (left == 0)
        return true;
    int k = 0;
    for (int i = 1; i < (int)sky.size(); i++)
        if (sky[i].level < sky[k].level)
            k = i;
    Seg s = sky[k];
    set<pair<int, int>> tried;
    for (int i = 0; i < PIECES; i++) {
        if (used[i])
            continue;
        for (auto [w, h] : {make_pair(pw[i], ph[i]), make_pair(ph[i], pw[i])}) {
            if (tried.count({w, h}) || w > s.span || s.level + h > height)
                continue;
            tried.insert({w, h});
            vector<Seg> parts = {{s.x, w, s.level + h}};
            if (w < s.span)
                parts.push_back({s.x + w, s.span - w, s.level});
            vector<Seg> all(sky.begin(), sky.begin() + k), next;
            all.insert(all.end(), parts.begin(), parts.end());
            all.insert(all.end(), sky.begin() + k + 1, sky.end());
            for (const Seg &seg : all)
                if (!next.empty() && next.back().level == seg.level)
                    next.back().span += seg.span;
                else
                    next.push_back(seg);
            used[i] = true;
            if (fill(next, left - 1))
                return true;
            used[i] = false;
        }
    }
    return false;
}

int main() {
    long long area = 0;
    for (int i = 0; i < PIECES; i++) {
        scanf("%d %d", &pw[i], &ph[i]);
        area += (long long)pw[i] * ph[i];
    }
    for (long long width = 1; width * width <= area; width++)
        if (area % width == 0) {
            height = area / width;
            if (fill({{0, (int)width, 0}}, PIECES)) {
                puts("YES");
                return 0;
            }
        }
    puts("NO");
}
