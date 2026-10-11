#include <cstdio>
#include <vector>

const int SIDE = 512; // the cave is at most 500 x 500
const int DIRS = 4;
const int FIELDS = 5; // W, H, X, Y and D

int main() {
    int w = 0, h = 0, x = 0, y = 0, d = 0;
    if (scanf("%d %d %d %d %d", &w, &h, &x, &y, &d) != FIELDS)
        return 0;
    std::vector<char> open(w * h), wet(w * h, 0);
    static char row[SIDE];
    for (int r = 0; r < h; r++) {
        if (scanf("%511s", row) != 1)
            return 0;
        for (int c = 0; c < w; c++)
            open[r * w + c] = row[c] != '#';
    }
    // water reaches a cell that has a way to the surface without going down,
    // so search back from the top row: down, left and right
    std::vector<int> stack;
    for (int c = 0; c < w; c++) {
        if (open[c]) {
            wet[c] = 1;
            stack.push_back(c);
        }
    }
    while (!stack.empty()) {
        int cell = stack.back(), r = cell / w, c = cell % w;
        stack.pop_back();
        int next[] = {r + 1 < h ? cell + w : -1, c > 0 ? cell - 1 : -1, c + 1 < w ? cell + 1 : -1};
        for (int n : next) {
            if (n >= 0 && open[n] && !wet[n]) {
                wet[n] = 1;
                stack.push_back(n);
            }
        }
    }
    // label: moves made under water since the last breath; an air pocket
    // resets it to 0, and no stretch under water may take more than D moves
    int start = (h - y) * w + (x - 1);
    std::vector<int> label(w * h, d + 1);
    std::vector<std::vector<int>> buckets(d + 1);
    label[start] = 0;
    buckets[0].push_back(start);
    for (int level = 0; level <= d;) {
        if (buckets[level].empty()) {
            level++;
            continue;
        }
        int cell = buckets[level].back();
        buckets[level].pop_back();
        int here = label[cell];
        if (here != level)
            continue;
        int r = cell / w, c = cell % w;
        if (r == 0 && here + 1 <= d) {
            puts("Can be rescued by himself");
            return 0;
        }
        int next[DIRS] = {r > 0 ? cell - w : -1, r + 1 < h ? cell + w : -1, c > 0 ? cell - 1 : -1,
                          c + 1 < w ? cell + 1 : -1};
        for (int n : next) {
            if (n < 0 || !open[n])
                continue;
            int nl = 0;
            if (wet[n]) {
                nl = here + 1;
            } else if (wet[cell] && here + 1 > d) {
                continue;
            }
            if (nl <= d && nl < label[n]) {
                label[n] = nl;
                buckets[nl].push_back(n);
                if (nl < level)
                    level = nl;
            }
        }
    }
    puts("Rescue operation required");
    return 0;
}
