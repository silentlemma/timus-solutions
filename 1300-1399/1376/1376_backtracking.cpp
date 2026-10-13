#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;

// Faces: 0 the base, 1..4 the sides clockwise from the one facing +y. On the
// base, side k rests on the edge (v[k - 1], v[k % 4]); on a side, v[0] and
// v[1] are its base corners and v[2] its apex.
const int SIDES = 4;
const int FACES = 5;
const int MAX_ROLLS = 32;
const double EPS = 1e-12;
const double NONE = -1e100;
const int BEAM = 4000;  // states kept per depth by the first, greedy pass
const int TRIANGLE = 3; // corners of a side: its centroid is a third of the way up

struct Pt {
    double x, y;
};

struct State {
    int face, prev;
    Pt v[SIDES];
    Pt c; // the centre of the face on the table
};

double s, t; // the base edge and the height of a side
double X, Y;
int N;
double reach[FACES * FACES][MAX_ROLLS + 1]; // the farthest the centre can go, ending on the base
double best;
int bestRolls;
int bestSeq[MAX_ROLLS + 1], seq[MAX_ROLLS + 1];

int key(int prev, int face) { return prev < 0 ? 0 : prev * FACES + face; }

bool canRoll(int face, int next) {
    if (face == next)
        return false;
    if (face == 0 || next == 0)
        return true;
    return (face - next + SIDES) % 2 == 1; // a neighbouring side, not the opposite one
}

double cross(Pt a, Pt b, Pt p) { return (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x); }

Pt reflect(Pt p, Pt a, Pt b) {
    double dx = b.x - a.x, dy = b.y - a.y;
    double k = ((p.x - a.x) * dx + (p.y - a.y) * dy) / (dx * dx + dy * dy);
    return {2 * (a.x + k * dx) - p.x, 2 * (a.y + k * dy) - p.y};
}

// the unit normal of a -> b pointing away from q
void away(Pt a, Pt b, Pt q, double &nx, double &ny) {
    double dx = b.x - a.x, dy = b.y - a.y, len = hypot(dx, dy);
    nx = -dy / len, ny = dx / len;
    if (cross(a, b, {a.x + nx, a.y + ny}) * cross(a, b, q) > 0)
        nx = -nx, ny = -ny;
}

State roll(const State &st, int next) {
    State ns;
    ns.face = next;
    ns.prev = st.face;
    const Pt *v = st.v;
    double nx, ny;
    if (st.face == 0) { // onto side next: its apex beyond the edge
        Pt a = v[next - 1], b = v[next % SIDES];
        away(a, b, st.c, nx, ny);
        ns.v[0] = a, ns.v[1] = b;
        ns.v[2] = {(a.x + b.x) / 2 + nx * t, (a.y + b.y) / 2 + ny * t};
    } else if (next == 0) { // onto the base: the square beyond the edge
        Pt a = v[0], b = v[1];
        away(a, b, v[2], nx, ny);
        Pt corner[SIDES] = {a, b, {b.x + nx * s, b.y + ny * s}, {a.x + nx * s, a.y + ny * s}};
        for (int i = 0; i < SIDES; i++)
            ns.v[(st.face - 1 + i) % SIDES] = corner[i];
    } else if (next == st.face % SIDES + 1) { // clockwise over the edge (v[1], apex)
        ns.v[0] = v[1], ns.v[1] = reflect(v[0], v[1], v[2]), ns.v[2] = v[2];
    } else { // counterclockwise over the edge (v[0], apex)
        ns.v[0] = reflect(v[1], v[0], v[2]), ns.v[1] = v[0], ns.v[2] = v[2];
    }
    int n = next == 0 ? SIDES : SIDES - 1;
    ns.c = {0, 0};
    for (int i = 0; i < n; i++)
        ns.c.x += ns.v[i].x / n, ns.c.y += ns.v[i].y / n;
    return ns;
}

double distTo(const State &st) { return hypot(st.c.x - X, st.c.y - Y); }

// can this state, with r rolls left, still beat the best?
bool hopeful(const State &st, int r) {
    double lim = best + reach[key(st.prev, st.face)][r] + EPS;
    double dx = st.c.x - X, dy = st.c.y - Y;
    return reach[key(st.prev, st.face)][r] > NONE && dx * dx + dy * dy <= lim * lim;
}

void consider(const int *sequence, int rolls, double d) {
    if (d + EPS < best || (fabs(d - best) <= EPS && rolls < bestRolls)) {
        best = d;
        bestRolls = rolls;
        copy(sequence, sequence + rolls + 1, bestSeq);
    }
}

void search(const State &st, int depth) {
    if (st.face == 0)
        consider(seq, depth, distTo(st));
    if (depth == N)
        return;
    pair<double, State> next[SIDES];
    int count = 0;
    for (int f = 0; f < FACES; f++) {
        if (!canRoll(st.face, f) || f == st.prev)
            continue;
        State ns = roll(st, f);
        if (hopeful(ns, N - depth - 1)) {
            double dx = ns.c.x - X, dy = ns.c.y - Y;
            next[count++] = {dx * dx + dy * dy, ns};
        }
    }
    for (int i = 1; i < count; i++) // nearest first
        for (int j = i; j > 0 && next[j].first < next[j - 1].first; j--)
            swap(next[j], next[j - 1]);
    for (int i = 0; i < count; i++) {
        seq[depth + 1] = next[i].second.face;
        search(next[i].second, depth + 1);
    }
}

struct Beam {
    double key;
    State st;
    int seq[MAX_ROLLS + 1];
};

// a first answer: a beam search keeping the states that may get closest
void beam(const State &start) {
    vector<Beam> states(1, Beam{0, start, {0}});
    for (int depth = 0; depth < N; depth++) {
        vector<Beam> next;
        for (const Beam &b : states)
            for (int f = 0; f < FACES; f++) {
                if (!canRoll(b.st.face, f) || f == b.st.prev)
                    continue;
                State ns = roll(b.st, f);
                double d = distTo(ns), r = reach[key(ns.prev, ns.face)][N - depth - 1];
                if (r <= NONE)
                    continue;
                Beam nb{max(0.0, d - r), ns, {}};
                copy(b.seq, b.seq + depth + 1, nb.seq);
                nb.seq[depth + 1] = f;
                if (f == 0)
                    consider(nb.seq, depth + 1, d);
                next.push_back(nb);
            }
        sort(next.begin(), next.end(), [](const Beam &a, const Beam &b) { return a.key < b.key; });
        if ((int)next.size() > BEAM)
            next.resize(BEAM);
        states.swap(next);
    }
}

int main() {
    double l;
    scanf("%lf %lf %lf %lf %d", &s, &l, &X, &Y, &N);
    t = sqrt(l * l - (s / 2) * (s / 2));
    // how far one roll moves the centre: base <-> side, and side <-> side
    double baseStep = s / 2 + t / TRIANGLE, sideStep = 2 * s * t / (TRIANGLE * l);
    for (auto &row : reach)
        fill(row, row + MAX_ROLLS + 1, NONE);
    for (int prev = -1; prev < FACES; prev++)
        if (prev != 0)
            reach[key(prev, 0)][0] = 0;
    for (int r = 1; r <= N; r++)
        for (int face = 0; face < FACES; face++)
            for (int prev = -1; prev < FACES; prev++) {
                if ((prev < 0 && face != 0) || (prev >= 0 && !canRoll(prev, face)))
                    continue;
                double &u = reach[key(prev, face)][r];
                u = reach[key(prev, face)][r - 1];
                if (face == 0)
                    u = max(u, 0.0);
                for (int f = 0; f < FACES; f++)
                    if (canRoll(face, f) && f != prev && reach[key(face, f)][r - 1] > NONE)
                        u = max(u, (face == 0 || f == 0 ? baseStep : sideStep) +
                                       reach[key(face, f)][r - 1]);
            }
    State start;
    start.face = 0, start.prev = -1;
    const Pt corners[SIDES] = {{-s / 2, s / 2}, {s / 2, s / 2}, {s / 2, -s / 2}, {-s / 2, -s / 2}};
    copy(corners, corners + SIDES, start.v);
    start.c = {0, 0};
    best = hypot(X, Y), bestRolls = 0, bestSeq[0] = seq[0] = 0;
    beam(start);
    search(start, 0);
    printf("%.3f\n%d\n", best + EPS, bestRolls);
    for (int i = 0; i <= bestRolls; i++)
        printf(i ? " %d" : "%d", bestSeq[i]);
    printf("\n");
}
