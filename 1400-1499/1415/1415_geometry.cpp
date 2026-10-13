#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

const vector<string> COLORS = {"VIOLET", "INDIGO", "BLUE", "GREEN", "YELLOW", "ORANGE", "RED"};
const int RED = 6;
const double PER_DECADE = 5; // a level per 2 dB: five levels per tenfold distance
const double TEN = 10;
const double EPS = 1e-9; // events closer than this in segment time happen together
const double TIE = 1e-9; // powers closer than this relative gap are equal

int n;
vector<double> xs, ys, rs;
vector<string> names;
vector<vector<double>> bounds; // squared radii where the level steps up

int level(int i, double px, double py) {
    double d2 = (px - xs[i]) * (px - xs[i]) + (py - ys[i]) * (py - ys[i]);
    int l = 0;
    for (double b : bounds[i])
        l += d2 > b;
    return l;
}

// the strongest station at (px, py); equal powers go to the smaller name
int best(const vector<int> &cands, double px, double py) {
    int top = cands[0];
    for (size_t k = 1; k < cands.size(); k++) {
        int i = cands[k];
        // power is r / d: compare r_i * d_top with r_top * d_i
        double a = rs[i] * hypot(px - xs[top], py - ys[top]);
        double b = rs[top] * hypot(px - xs[i], py - ys[i]);
        if (a > b * (1 + TIE) || (fabs(a - b) <= TIE * max(a, b) && names[i] < names[top]))
            top = i;
    }
    return top;
}

double sx, sy, dx, dy, len2;

// times in (0, 1) where the distance to station i squared is rad2
void roots(int i, double rad2, vector<double> &out) {
    double px = sx - xs[i], py = sy - ys[i];
    double b = dx * px + dy * py, c = px * px + py * py - rad2;
    double disc = b * b - len2 * c;
    if (disc <= 0)
        return;
    double q = -(b + copysign(sqrt(disc), b));
    for (double t : {q / len2, c / q})
        if (t > 0 && t < 1)
            out.push_back(t);
}

// the level of station i just after time t, before its own next change
int levelAfter(int i, double t) {
    vector<double> ts;
    for (double b : bounds[i])
        roots(i, b, ts);
    double next = 1;
    for (double u : ts)
        if (u > t + EPS)
            next = min(next, u);
    double u = (t + next) / 2;
    return level(i, sx + dx * u, sy + dy * u);
}

int main() {
    ios::sync_with_stdio(false);
    cin >> n;
    xs.resize(n), ys.resize(n), rs.resize(n), names.resize(n), bounds.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> xs[i] >> ys[i] >> rs[i] >> names[i];
        for (int k = 0; k < RED; k++) {
            double r = rs[i] * pow(TEN, k / PER_DECADE);
            bounds[i].push_back(r * r);
        }
    }
    int m;
    cin >> m;
    vector<pair<double, double>> from(m), to(m); // the ends of each segment
    for (int j = 0; j < m; j++)
        cin >> from[j].first >> from[j].second >> to[j].first >> to[j].second;
    string out;
    vector<int> all(n);
    for (int i = 0; i < n; i++)
        all[i] = i;
    int cur = best(all, from[0].first, from[0].second);
    int lev = level(cur, from[0].first, from[0].second);
    out += "Power on. CELL_ID:" + names[cur] + ", SIGNAL_LEVEL:" + COLORS[lev] + "\n";

    for (int j = 0; j < m; j++) {
        sx = from[j].first, sy = from[j].second;
        dx = to[j].first - sx, dy = to[j].second - sy;
        len2 = dx * dx + dy * dy;
        if (len2 == 0)
            continue;
        // red and not red switch only on the outer circles
        vector<pair<double, int>> reds;
        for (int i = 0; i < n; i++) {
            vector<double> ts;
            roots(i, bounds[i][RED - 1], ts);
            for (double t : ts)
                reds.push_back({t, i});
        }
        auto timeline = [&](double after) {
            vector<pair<double, int>> events;
            vector<double> ts;
            for (double b : bounds[cur])
                roots(cur, b, ts);
            for (double t : ts)
                events.push_back({t, -1});
            for (auto &e : reds)
                events.push_back(e);
            sort(events.begin(), events.end());
            vector<pair<double, int>> kept;
            for (auto &e : events)
                if (e.first > after)
                    kept.push_back(e);
            return kept;
        };
        vector<pair<double, int>> events = timeline(-1);
        size_t k = 0;
        while (k < events.size()) {
            double t0 = events[k].first;
            vector<int> group;
            while (k < events.size() && events[k].first - t0 <= EPS)
                group.push_back(events[k++].second);
            // the state right after the group holds until the next event
            double tend = events[k - 1].first;
            double t1 = k < events.size() ? events[k].first : 1;
            double mx = sx + dx * (t0 + t1) / 2, my = sy + dy * (t0 + t1) / 2;
            double px = sx + dx * t0, py = sy + dy * t0;
            bool searching = false;
            vector<int> cands;
            if (lev != RED) {
                int now = level(cur, mx, my);
                if (now != lev) {
                    lev = now;
                    out += "Signal changed. SIGNAL_LEVEL:" + COLORS[lev] + "\n";
                    if (lev == RED) {
                        searching = true;
                        for (int i = 0; i < n; i++)
                            if (level(i, mx, my) < RED)
                                cands.push_back(i);
                    }
                }
            } else {
                searching = true;
                for (int i : group)
                    if (i >= 0 && level(i, mx, my) < RED)
                        cands.push_back(i);
            }
            if (!searching || cands.empty())
                continue;
            int pick = best(cands, px, py);
            lev = levelAfter(pick, tend);
            if (pick == cur) {
                out += "Signal changed. SIGNAL_LEVEL:" + COLORS[lev] + "\n";
            } else {
                cur = pick;
                out +=
                    "Cell changed. CELL_ID:" + names[cur] + ", SIGNAL_LEVEL:" + COLORS[lev] + "\n";
                events = timeline(tend + EPS);
                k = 0;
            }
        }
    }
    cout << out;
}
