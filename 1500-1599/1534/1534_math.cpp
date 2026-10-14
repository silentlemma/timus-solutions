#include <algorithm>
#include <iostream>
using namespace std;

int main() {
    long long k, l, n;
    cin >> k >> l >> n;
    long long d = k - l;
    // with W wins and R losses the team has n + 2W - R points; the goals
    // split into a common part, scored and conceded alike, plus at least
    // one goal of margin per win and per loss
    long long best, worst;
    if (d >= 0) {
        // no losses: the margin d covers up to d wins, the rest are draws
        best = n + 2 * min(d, n);
        worst = d == 0 ? n : n + 2;
    } else {
        // no wins: up to -d losses, at least one
        best = n - 1;
        worst = n - min(-d, n);
    }
    if (k >= 1 && l >= 1 && n >= 2) {
        // wins and losses together: one goal each is enough, so one loss
        // and up to k wins, or one win and up to l losses
        best = max(best, n - 1 + 2 * min(k, n - 1));
        worst = min(worst, n + 2 - min(l, n - 1));
    }
    cout << best << " " << worst << "\n";
}
