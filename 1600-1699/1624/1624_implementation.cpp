#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

typedef tuple<int, int, int> Edge; // kind (0 above row r, 1 left of column c), r, c

// the wall or door crossed from cell (r, c) in direction d
Edge edgeOf(int r, int c, char d) {
    if (d == 'N')
        return {0, r, c};
    if (d == 'S')
        return {0, r + 1, c};
    if (d == 'W')
        return {1, r, c};
    return {1, r, c + 1};
}

struct Scout {
    int r = 0, c = 0; // the position relative to the unknown start
    int loR = 0, hiR = 0, loC = 0, hiC = 0;
    map<Edge, int> seen;          // edge -> 1 for a door, 0 for a wall
    vector<Edge> byKind[2][2];    // [kind][door?]: the edges seen
};

int w, h, width;
Scout scouts[2];
vector<int> conflict; // reports ruling out the second start being the first shifted

// the start pairs left: 0, 1, or 2 for two or more
int starts() {
    Scout &a = scouts[0], &b = scouts[1];
    int lo1r = -a.loR, hi1r = h - 1 - a.hiR, lo1c = -a.loC, hi1c = w - 1 - a.hiC;
    int lo2r = -b.loR, hi2r = h - 1 - b.hiR, lo2c = -b.loC, hi2c = w - 1 - b.hiC;
    long long total = 0;
    for (int dr = -(h - 1); dr < h; dr++) {
        int top = max(lo1r, lo2r - dr), bottom = min(hi1r, hi2r - dr);
        if (top > bottom)
            continue;
        for (int dc = -(w - 1); dc < w; dc++) {
            if (conflict[(dr + h - 1) * width + dc + w - 1])
                continue;
            int left = max(lo1c, lo2c - dc), right = min(hi1c, hi2c - dc);
            if (left <= right) {
                total += (long long)(bottom - top + 1) * (right - left + 1);
                if (total > 1)
                    return 2;
            }
        }
    }
    return total;
}

int main() {
    int k;
    if (!(cin >> w >> h >> k))
        return 0;
    width = 2 * w - 1;
    conflict.assign((2 * h - 1) * width, 0);
    int safe = -1, count = starts();
    for (int step = 1; step <= k; step++) {
        string report;
        cin >> report;
        char d = report[0];
        int door = report[1] == '+';
        int who = (step - 1) % 2;
        Scout &me = scouts[who], &other = scouts[1 - who];
        Edge e = edgeOf(me.r, me.c, d);
        bool changed = false;
        auto it = me.seen.find(e);
        if (it == me.seen.end()) {
            me.seen[e] = door;
            auto [kind, er, ec] = e;
            me.byKind[kind][door].push_back(e);
            int sign = who == 0 ? 1 : -1;
            for (auto [fk, fr, fc] : other.byKind[kind][1 - door]) {
                int dr = sign * (er - fr), dc = sign * (ec - fc);
                if (-h < dr && dr < h && -w < dc && dc < w) {
                    conflict[(dr + h - 1) * width + dc + w - 1]++;
                    changed = true;
                }
            }
        } else if (it->second != door) {
            printf("A mistake has been made at step number %d\n", step);
            return 0;
        }
        if (door) {
            me.r += d == 'S' ? 1 : d == 'N' ? -1 : 0;
            me.c += d == 'E' ? 1 : d == 'W' ? -1 : 0;
            if (me.r < me.loR || me.r > me.hiR || me.c < me.loC || me.c > me.hiC) {
                me.loR = min(me.loR, me.r), me.hiR = max(me.hiR, me.r);
                me.loC = min(me.loC, me.c), me.hiC = max(me.hiC, me.c);
                changed = true;
            }
        }
        if (changed) // the count changes only with a new conflict or a wider path
            count = starts();
        if (count == 0) {
            printf("A mistake has been made at step number %d\n", step);
            return 0;
        }
        if (count == 1 && safe < 0)
            safe = step;
    }
    if (safe > 0)
        printf("The scouts are safe at step number %d\n", safe);
    else
        printf("There is not enough data\n");
}
