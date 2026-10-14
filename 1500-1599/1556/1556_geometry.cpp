#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

const double TAU = 2 * acos(-1.0);
const double EPS = 1e-12; // events closer than this in angle happen together
const long long PERCENT = 100;
const double HALF = 0.5;
const int MOST_HITS = 5;        // an arrow stops after the fifth cow
const int ENTER = 0, LEAVE = 1; // at one angle, rays start touching before they stop

struct Event {
    double angle;
    int kind;
    bool operator<(const Event &o) const {
        return angle != o.angle ? angle < o.angle : kind < o.kind;
    }
};

// the angle in [0, 2 pi); a tiny negative angle may round up to 2 pi
double norm(double a) {
    a = fmod(a, TAU);
    if (a < 0)
        a += TAU;
    return a >= TAU ? 0.0 : a;
}

int main() {
    ios::sync_with_stdio(false);
    int n, k, p;
    double r, vx, vy;
    cin >> n >> k >> p >> r >> vx >> vy;
    // expected hits of an arrow whose ray meets m cows, kept exact as integers
    // in units of 1 / 100^4: each further cow adds p / 100 of the last addition
    long long scale = 1;
    for (int m = 1; m < MOST_HITS; m++)
        scale *= PERCENT;
    vector<long long> gain(n + 1, 0);
    for (long long m = 1, term = scale; m <= n; m++) {
        gain[m] = gain[m - 1] + (m <= MOST_HITS ? term : 0);
        if (m < MOST_HITS)
            term = term / PERCENT * p;
    }
    vector<double> turn(k);
    for (int i = 0; i < k; i++)
        turn[i] = norm(atan(double(i) / (k - 1) - HALF));
    // the angle a seen by arrow i: the events of one arrow come in this order
    auto turned = [&](double a, int i) { return a >= turn[i] ? a - turn[i] : a - turn[i] + TAU; };
    // rays meet a cow at angles within asin(R / d) of its centre, and
    // each arrow sees the same angular intervals turned back by its offset
    vector<Event> base(2 * n);
    vector<int> count(k, 0);
    for (int j = 0; j < n; j++) {
        double x, y;
        cin >> x >> y;
        x -= vx, y -= vy;
        double centre = atan2(y, x), half = asin(min(1.0, r / hypot(x, y)));
        base[2 * j] = {norm(centre - half), ENTER};
        base[2 * j + 1] = {norm(centre + half), LEAVE};
        // the intervals that wrap hold the angle 0 of the arrow
        for (int i = 0; i < k; i++)
            if (turned(base[2 * j].angle, i) > turned(base[2 * j + 1].angle, i))
                count[i]++;
    }
    sort(base.begin(), base.end());
    int size = 2 * n;
    // arrow i takes the sorted events from cut[i] on, wrapping around once
    vector<int> cut(k), used(k, 0), leaving;
    for (int i = 0; i < k; i++)
        cut[i] = lower_bound(base.begin(), base.end(), Event{turn[i], ENTER}) - base.begin();
    auto at = [&](int i) { return base[(cut[i] + used[i]) % size]; };
    // the arrow whose next event comes first, or -1 when all are done
    auto pick = [&]() {
        int choice = -1;
        double angle = 0;
        int kind = 0;
        for (int i = 0; i < k; i++) {
            if (used[i] == size)
                continue;
            Event e = at(i);
            double a = turned(e.angle, i);
            if (choice < 0 || a < angle || (a == angle && e.kind < kind))
                choice = i, angle = a, kind = e.kind;
        }
        return choice;
    };
    long long best = -1, total = 0;
    double bestAngle = 0;
    for (int i = 0; i < k; i++)
        total += gain[count[i]];
    int next = pick();
    double first = turned(at(next).angle, next);
    while (next >= 0) {
        double x = turned(at(next).angle, next);
        leaving.clear();
        while (next >= 0 && turned(at(next).angle, next) - x <= EPS) {
            if (at(next).kind == ENTER) {
                total += gain[count[next] + 1] - gain[count[next]];
                count[next]++;
            } else
                leaving.push_back(next);
            used[next]++;
            next = pick();
        }
        // at the angle itself, touching counts: new cows join, none leave yet
        long long point = total;
        for (int i : leaving) {
            count[i]--;
            total -= gain[count[i] + 1] - gain[count[i]];
        }
        // after the last event the stretch runs on past 2 pi to the first one
        double following = next >= 0 ? turned(at(next).angle, next) : TAU + first;
        // an open stretch is safer than a single tangent angle, so it wins ties
        if (following - x > EPS && total >= best)
            best = total, bestAngle = (x + following) / 2;
        if (point > best)
            best = point, bestAngle = x;
    }
    printf("The best shot at (%.10f;%.10f) gives Vasya %.4f average hits.\n", cos(bestAngle),
           sin(bestAngle), double(best) / scale);
}
