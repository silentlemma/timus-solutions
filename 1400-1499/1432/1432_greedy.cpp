#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int NINE = 9;
const int CLASSES = 4; // positions grouped by the signs of the two rules
const int BOTH_UP = 0, X_UP = 1, Y_UP = 2, BOTH_DOWN = 3;

int len;
vector<int> s;

struct Combo {
    vector<int> wx, wy, cls, tail; // tail[k]: sum of wx from k on
    vector<vector<int>> cnt;
    vector<long long> px, py;

    Combo(const vector<int> &x, const vector<int> &y) : wx(x), wy(y), cls(len), tail(len + 1, 0) {
        cnt.assign(CLASSES, vector<int>(len + 1, 0));
        px.assign(len + 1, 0);
        py.assign(len + 1, 0);
        for (int k = 0; k < len; k++) {
            cls[k] = (wx[k] > 0 ? 0 : 2) + (wy[k] > 0 ? 0 : 1);
            for (int c = 0; c < CLASSES; c++)
                cnt[c][k + 1] = cnt[c][k] + (cls[k] == c);
            px[k + 1] = px[k] + wx[k] * s[k];
            py[k + 1] = py[k] + wy[k] * s[k];
        }
        for (int k = len - 1; k >= 0; k--)
            tail[k] = tail[k + 1] + wx[k];
    }

    // digits before j give sums sx, sy; j in [lo_j, hi_j], free up to p,
    // p at most 8, nines after p; t must balance wx, t + 1 must balance wy
    bool feasible(long long sx, long long sy, int j, int p, int loJ, int hiJ) const {
        long long a = -sx - NINE * tail[p + 1], b = -sy - wy[p];
        long long lo[CLASSES] = {0, 0, 0, 0}, hi[CLASSES];
        for (int c = 0; c < CLASSES; c++)
            hi[c] = NINE * (cnt[c][p + 1] - cnt[c][j]);
        hi[cls[j]] += hiJ - NINE;
        lo[cls[j]] += loJ;
        if (p > j)
            hi[cls[p]] -= 1;
        if ((a + b) % 2 != 0)
            return false;
        long long u = (a + b) / 2, v = (a - b) / 2;
        return lo[BOTH_UP] - hi[BOTH_DOWN] <= u && u <= hi[BOTH_UP] - lo[BOTH_DOWN] &&
               lo[X_UP] - hi[Y_UP] <= v && v <= hi[X_UP] - lo[Y_UP];
    }

    // t from s up to j, then d, then the smallest digits that still fit, then nines after p
    vector<int> build(int p, int j, int d) const {
        vector<int> t(s.begin(), s.begin() + j);
        long long sx = px[j], sy = py[j];
        if (j > p) // t keeps s up to p and has nines after it
            return vector<int>(s.begin(), s.begin() + p + 1);
        t.push_back(d);
        sx += wx[j] * d;
        sy += wy[j] * d;
        for (int k = j + 1; k <= p; k++) {
            int x = 0;
            while (!feasible(sx, sy, k, p, x, x))
                x++;
            t.push_back(x);
            sx += wx[k] * x;
            sy += wy[k] * x;
        }
        return t;
    }
};

int main() {
    string line;
    cin >> line;
    len = line.size();
    s.resize(len);
    for (int k = 0; k < len; k++)
        s[k] = line[k] - '0';
    int half = len / 2;
    vector<int> ruleA(len), ruleB(len);
    for (int k = 0; k < len; k++) {
        ruleA[k] = k < half ? 1 : -1;
        ruleB[k] = k % 2 == 0 ? 1 : -1;
    }
    vector<vector<int>> rules = {ruleA, ruleB};
    vector<Combo> combos;
    for (auto &x : rules)
        for (auto &y : rules)
            combos.emplace_back(x, y); // the rule for t, then the rule for t + 1
    // best: the first position where t leaves s (later is better), then the digit there
    int bestDev = -1, bestDigit = NINE + 1;
    vector<int> best;
    bool found = false;
    for (auto &cb : combos)
        for (int p = 0; p < len; p++) {
            int dev = -1, digit = 0, j = -1, d = 0;
            if (s[p] < NINE && cb.px[p + 1] + NINE * cb.tail[p + 1] == 0 &&
                cb.py[p + 1] + cb.wy[p] == 0) {
                dev = len;
                for (int k = p + 1; k < len; k++)
                    if (s[k] < NINE) {
                        dev = k;
                        break;
                    }
                digit = NINE;
                j = p + 1;
            } else {
                for (int q = p; q >= 0 && dev < 0; q--) {
                    int top = q == p ? NINE - 1 : NINE;
                    if (s[q] + 1 > top || !cb.feasible(cb.px[q], cb.py[q], q, p, s[q] + 1, top))
                        continue;
                    d = s[q] + 1;
                    while (!cb.feasible(cb.px[q], cb.py[q], q, p, d, d))
                        d++;
                    dev = j = q;
                    digit = d;
                }
            }
            if (dev < 0 || dev < bestDev || (dev == bestDev && digit > bestDigit))
                continue;
            vector<int> t = cb.build(p, j, d);
            t.resize(len, NINE);
            if (!found || dev > bestDev || digit < bestDigit || t < best) {
                best = t;
                bestDev = dev;
                bestDigit = digit;
                found = true;
            }
        }
    if (!found) {
        printf("No solution\n");
        return 0;
    }
    vector<int> next = best;
    int k = len - 1;
    while (next[k] == NINE)
        next[k--] = 0;
    next[k]++;
    string a, b;
    for (int x : best)
        a += char('0' + x);
    for (int x : next)
        b += char('0' + x);
    printf("%s %s\n", a.c_str(), b.c_str());
}
