#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <set>
#include <vector>

// a draught is hit when its centre is this close to the path of the centre of
// the moving one, two radii of 0.4
const double REACH = 0.8;
const double EPS = 1e-9;
const int SIDE = 8, PIECES = 2 * SIDE;
const double PI = std::acos(-1.0);

std::vector<std::vector<int>> kills(PIECES);
std::vector<int8_t> memo; // -1 unknown, else whether the player to move wins

// the player to move, red (0) or white (1), wins from here
bool wins(int alive, int turn) {
    int key = alive << 1 | turn;
    if (memo[key] >= 0)
        return memo[key];
    int own = alive & (turn ? ((1 << SIDE) - 1) << SIDE : (1 << SIDE) - 1);
    bool result = false;
    for (int p = 0; p < PIECES && !result; p++)
        if (own >> p & 1)
            for (int s : kills[p])
                if (!wins(alive & ~s, 1 - turn)) {
                    result = true;
                    break;
                }
    memo[key] = result;
    return result;
}

int main() {
    double x[PIECES], y[PIECES];
    for (int k = 0; k < PIECES; k++)
        if (scanf("%lf %lf", &x[k], &y[k]) != 2)
            return 0;
    // every direction kills the draughts within REACH of its ray; the set
    // changes only where the ray becomes tangent to some draught, so the
    // tangent directions and the gaps between them give every possible set
    for (int p = 0; p < PIECES; p++) {
        std::vector<double> angles;
        for (int q = 0; q < PIECES; q++)
            if (q != p) {
                double d = std::hypot(x[q] - x[p], y[q] - y[p]);
                double centre = std::atan2(y[q] - y[p], x[q] - x[p]);
                double half = std::asin(std::min(1.0, REACH / d));
                for (double a : {centre - half, centre + half})
                    angles.push_back(std::fmod(a + 2 * PI, 2 * PI));
            }
        std::sort(angles.begin(), angles.end());
        std::vector<double> tries = angles;
        for (size_t k = 0; k < angles.size(); k++) {
            double next = k + 1 < angles.size() ? angles[k + 1] : angles[0] + 2 * PI;
            tries.push_back((angles[k] + next) / 2);
        }
        std::set<int> sets;
        for (double t : tries) {
            double ux = std::cos(t), uy = std::sin(t);
            int mask = 1 << p;
            for (int q = 0; q < PIECES; q++) {
                double dx = x[q] - x[p], dy = y[q] - y[p];
                if (q != p && dx * ux + dy * uy >= 0 && std::fabs(dx * uy - dy * ux) <= REACH + EPS)
                    mask |= 1 << q;
            }
            sets.insert(mask);
        }
        kills[p].assign(sets.begin(), sets.end());
    }
    memo.assign(1 << (PIECES + 1), -1);
    puts(wins((1 << PIECES) - 1, 0) ? "RED" : "WHITE");
}
