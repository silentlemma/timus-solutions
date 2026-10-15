#include <algorithm>
#include <cmath>
#include <cstdio>
#include <limits>
#include <tuple>
#include <vector>
using namespace std;

const double FULL = 360, MINUTES = 60, EPS = 1e-9;
const double INF = numeric_limits<double>::infinity();

int main() {
    double a, w;
    int n;
    if (scanf("%lf %lf", &a, &w) != 2 || scanf("%d", &n) != 1)
        return 0;
    vector<int> first;  // ships right in front of the gun, shot at once
    vector<tuple<double, double, int>> ships;
    for (int k = 1; k <= n; k++) {
        double b, d, v;
        if (scanf("%lf %lf", &b, &d) != 2 || scanf("%lf", &v) != 1)
            return 0;
        double deadline = (d - 1) / v * MINUTES;  // when the ship reaches one mile
        double turn = fmod(fmod(b - a, FULL) + FULL, FULL);
        if (turn <= EPS || FULL - turn <= EPS)
            first.push_back(k);
        else
            ships.push_back({turn, deadline, k});
    }
    sort(ships.begin(), ships.end());
    int m = ships.size(), size = m + 1;
    double speed = FULL * w;  // degrees a minute
    auto angle = [&](int k) { return get<0>(ships[k]); };
    auto due = [&](int k) { return get<1>(ships[k]); };
    // the shot ships always form an arc around the start: i of them taken
    // turning left (from the end of the sorted list), j turning right; left
    // and right hold the earliest time with the gun at that end
    vector<double> left(size * size, INF), right(size * size, INF);
    vector<char> cameLeft(size * size), cameRight(size * size);  // the side before
    left[0] = right[0] = 0;
    for (int i = 0; i < size; i++)
        for (int j = 0; i + j < size; j++) {
            int here = i * size + j;
            double tl = left[here], tr = right[here];
            if (tl == INF && tr == INF)
                continue;
            if (i + j == m)
                continue;
            double atLeft = i ? FULL - angle(m - i) : 0, atRight = j ? angle(j - 1) : 0;
            double next = angle(j);  // the next ship turning right
            int there = here + 1;
            pair<double, int> moves[] = {{tr + (next - atRight) / speed, 1},
                                         {tl + (atLeft + next) / speed, 0}};
            for (auto [t, side] : moves)
                if (t <= due(j) + EPS && t + EPS < right[there])
                    right[there] = t, cameRight[there] = side;
            next = FULL - angle(m - i - 1);  // the next ship turning left
            there = here + size;
            pair<double, int> back[] = {{tl + (next - atLeft) / speed, 0},
                                        {tr + (atRight + next) / speed, 1}};
            for (auto [t, side] : back)
                if (t <= due(m - i - 1) + EPS && t + EPS < left[there])
                    left[there] = t, cameLeft[there] = side;
        }
    // ending at the left end wins ties, then the fewest ships taken leftwards
    double best = INF;
    int side = 0;
    for (int s = 0; s < 2; s++)
        for (int i = 0; i < size; i++) {
            double t = (s ? right : left)[i * size + m - i];
            if (t < best)
                best = t, side = s;
        }
    if (best == INF) {
        puts("Impossible");
        return 0;
    }
    const vector<double> &at = side ? right : left;
    int i = 0;
    while (fabs(at[i * size + m - i] - best) > EPS)
        i++;
    int j = m - i;
    vector<int> order;
    while (i || j) {
        int here = i * size + j;
        if (side) {
            order.push_back(get<2>(ships[j - 1]));
            side = cameRight[here], j--;
        } else {
            order.push_back(get<2>(ships[m - i]));
            side = cameLeft[here], i--;
        }
    }
    printf("%.3f\n", best);
    for (int k : first)
        printf("%d\n", k);
    for (int k = order.size() - 1; k >= 0; k--)
        printf("%d\n", order[k]);
}
