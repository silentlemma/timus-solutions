#include <algorithm>
#include <cstdio>
#include <limits>
#include <vector>

using namespace std;

typedef long long ll;

const double PERCENT = 100;
const double INF = numeric_limits<double>::infinity();

struct Flight {
    int a, b;
    ll t, f, d;
    int p;
};

int n;
// per airport, over the flights seen so far (latest first): departure
// times, and the best expected arrival over the flights leaving at that time
// or later
vector<vector<ll>> departs;
vector<vector<double>> best;

// the best expected arrival for someone at airport a at this time
double expected(int a, ll time) {
    if (a == n) return time;
    const vector<ll>& late = departs[a];
    // late is decreasing; count the departures at time or later
    int k = upper_bound(late.begin(), late.end(), time, greater<ll>()) - late.begin();
    return k > 0 ? best[a][k - 1] : INF;
}

int main() {
    int m;
    if (scanf("%d %d", &n, &m) != 2) return 0;
    vector<Flight> flights(m);
    for (Flight& x : flights)
        scanf("%d %d %lld %lld %d %lld", &x.a, &x.b, &x.t, &x.f, &x.p, &x.d);
    departs.assign(n + 1, {});
    best.assign(n + 1, {});
    // an arrival is always later than the departure, so taking flights from
    // the latest departure down sees every flight a connection could use
    sort(flights.begin(), flights.end(),
         [](const Flight& x, const Flight& y) { return x.t > y.t; });
    for (const Flight& x : flights) {
        double on_time = expected(x.b, x.t + x.f), delayed = expected(x.b, x.t + x.f + x.d);
        double value = ((PERCENT - x.p) * on_time + x.p * delayed) / PERCENT;
        if (!best[x.a].empty()) value = min(value, best[x.a].back());
        departs[x.a].push_back(x.t);
        best[x.a].push_back(value);
    }
    double answer = expected(1, 0);
    if (answer == INF)
        puts("Fail");
    else
        printf("%.6f\n", answer);
    return 0;
}
