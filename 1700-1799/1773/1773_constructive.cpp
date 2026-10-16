#include <algorithm>
#include <cstdio>
#include <vector>

int n, h, d;
std::vector<int> lefts;

// the place of a left end on the line from start, or -1 if it has none
int spot(int value, int start) {
    int diff = value - start;
    if (diff % d != 0) return -1;
    int step = diff / d;
    return step >= 0 && step < n ? step : -1;
}

// the strips in order, signed when turned over, if their left ends can be
// start, start + d, ..., start + (n - 1) d; empty otherwise
std::vector<int> arrange(int start) {
    std::vector<int> place(n, 0);
    std::vector<int> flexible;
    for (int k = 0; k < n; k++) {
        // with a flat line every strip keeps its own place in the order
        int a = d ? spot(lefts[k], start) : (lefts[k] == start ? k : -1);
        int b = d ? spot(h - d - lefts[k], start) : (h - lefts[k] == start ? k : -1);
        if (b == a) b = -1;
        if (a < 0 && b < 0) return {};
        if (a >= 0 && b >= 0) {
            flexible.push_back(k);
            continue;
        }
        int step = a >= 0 ? a : b;
        if (place[step]) return {};
        place[step] = a >= 0 ? k + 1 : -(k + 1);
    }
    // a strip that fits two places pairs place i with place K - i, so only
    // strips of the same pair compete once the strips with one choice are in
    for (int k : flexible) {
        int a = spot(lefts[k], start), b = spot(h - d - lefts[k], start);
        if (!place[a]) place[a] = k + 1;
        else if (!place[b]) place[b] = -(k + 1);
        else return {};
    }
    return place;
}

int main() {
    if (scanf("%d %d", &h, &n) != 2) return 0;
    lefts.resize(n);
    std::vector<int> rights(n);
    for (int i = 0; i < n; i++) scanf("%d %d", &lefts[i], &rights[i]);
    // turning a strip over keeps its slope, so all slopes must be equal; the
    // left end x of a strip turns into h - d - x
    d = rights[0] - lefts[0];
    for (int i = 0; i < n; i++) {
        if (rights[i] - lefts[i] != d) {
            puts("0");
            return 0;
        }
    }
    std::vector<int> starts;
    if (d == 0) {
        starts = {lefts[0], h - lefts[0]};
    } else {
        int low = h, high = 0;
        for (int x : lefts) {
            low = std::min({low, x, h - d - x});
            high = std::max({high, x, h - d - x});
        }
        // the strip with the extreme end either starts the line or, turned,
        // ends it
        int first = d > 0 ? low : high, last = d > 0 ? high : low;
        starts = {first, last - (n - 1) * d};
    }
    for (int start : starts) {
        std::vector<int> place = arrange(start);
        if (place.empty()) continue;
        for (int i = 0; i < n; i++) printf(i ? " %d" : "%d", place[i]);
        printf("\n");
        return 0;
    }
    puts("0");
    return 0;
}
