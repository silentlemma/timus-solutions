#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>

const int ROLLS = 70;
const int DIRS = 6;
const double TURN = 60; // degrees between neighbouring directions
const double DEGREE = std::acos(-1.0) / 180;
const int OFF = 80; // coordinates stay within ROLLS of the origin
const int SIZE = 2 * OFF + 1;
const int MOVES = 3; // two side faces and the far side of the base
// the six directions of a hexagonal lattice, as integer combinations of
// the first two of them
const int UA[DIRS] = {1, 0, -1, -1, 0, 1};
const int UB[DIRS] = {0, 1, 1, 0, -1, -1};
const double CLASSES[] = {0, 90}; // starting edges at 0 and 180, or at 90 and 270 degrees

struct State {
    int a, b, d;
};

int cost[SIZE][SIZE][DIRS];

int main() {
    double tx = 0, ty = 0;
    if (scanf("%lf %lf", &tx, &ty) != 2)
        return 0;
    // a jump through the base in half steps: (1 + sqrt 3) / 2 = 1/2 + sin 60
    const double side = (1 + 2 * std::sin(TURN * DEGREE)) / 2;
    double best = std::hypot(tx, ty); // no rolls at all
    for (double start : CLASSES) {
        double wx[DIRS], wy[DIRS];
        for (int k = 0; k < DIRS; k++) {
            wx[k] = std::cos((start + TURN * k) * DEGREE);
            wy[k] = std::sin((start + TURN * k) * DEGREE);
        }
        // a state is a triangle lying on the table: twice its apex position
        // (in steps of the base jump) and the direction from the apex to the
        // base edge; it costs one roll to reach from the start
        for (auto &plane : cost)
            for (auto &row : plane)
                for (int &c : row)
                    c = ROLLS;
        std::vector<std::vector<State>> buckets(ROLLS + 1);
        for (int u : {0, DIRS / 2}) {
            State s = {UA[u], UB[u], (u + DIRS / 2) % DIRS};
            cost[s.a + OFF][s.b + OFF][s.d] = 1;
            buckets[1].push_back(s);
        }
        for (int c = 1; c < ROLLS; c++) {
            for (size_t i = 0; i < buckets[c].size(); i++) {
                State s = buckets[c][i];
                if (cost[s.a + OFF][s.b + OFF][s.d] != c)
                    continue;
                // roll onto the base: its centre is half a step beyond the apex
                int ea = s.a + UA[s.d], eb = s.b + UB[s.d];
                double x = side * (ea * wx[0] + eb * wx[1]);
                double y = side * (ea * wy[0] + eb * wy[1]);
                best = std::min(best, std::hypot(x - tx, y - ty));
                State next[] = {{s.a, s.b, (s.d + 1) % DIRS},
                                {s.a, s.b, (s.d + DIRS - 1) % DIRS},
                                {s.a + 2 * UA[s.d], s.b + 2 * UB[s.d], (s.d + DIRS / 2) % DIRS}};
                int add[] = {1, 1, 2}; // a side face is one roll, the base two
                for (int k = 0; k < MOVES; k++) {
                    State n = next[k];
                    int nc = c + add[k];
                    if (nc < ROLLS && cost[n.a + OFF][n.b + OFF][n.d] > nc) {
                        cost[n.a + OFF][n.b + OFF][n.d] = nc;
                        buckets[nc].push_back(n);
                    }
                }
            }
        }
    }
    printf("%.4f\n", best);
    return 0;
}
