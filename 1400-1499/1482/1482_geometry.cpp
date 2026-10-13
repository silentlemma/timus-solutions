#include <algorithm>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;
const ll SCALE = 10000000000LL; // ten digits after the point
const double FULL_TURN = 360, HALF_TURN = 180;
const int VERTICES = 3, TEXT = 64;

struct P {
    ll x, y;
};

ll cross(P o, P a, P b) { return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x); }
ll length2(P a, P b) { return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y); }

// num / den with exactly ten digits after the point, rounded
string decimal(ll num, ll den) {
    if (den < 0)
        num = -num, den = -den;
    bool negative = num < 0;
    ll a = negative ? -num : num;
    ll whole = a / den, rem = a % den;
    ll part = (2 * rem * SCALE + den) / (2 * den);
    if (part == SCALE)
        whole++, part = 0;
    char buf[TEXT];
    snprintf(buf, sizeof buf, "%s%lld.%010lld", negative && (whole || part) ? "-" : "", whole,
             part);
    return buf;
}

int main() {
    P target[VERTICES], token[VERTICES];
    for (auto &p : target)
        scanf("%lld %lld", &p.x, &p.y);
    for (auto &p : token)
        scanf("%lld %lld", &p.x, &p.y);

    // a correspondence works when the sides match and the turn is the same
    // (the token cannot be flipped over)
    int idx[VERTICES] = {0, 1, 2};
    vector<vector<P>> fits;
    do {
        vector<P> order = {target[idx[0]], target[idx[1]], target[idx[2]]};
        bool same =
            length2(token[0], token[1]) == length2(order[0], order[1]) &&
            length2(token[0], token[2]) == length2(order[0], order[2]) &&
            length2(token[1], token[2]) == length2(order[1], order[2]) &&
            (cross(token[0], token[1], token[2]) > 0) == (cross(order[0], order[1], order[2]) > 0);
        if (same)
            fits.push_back(order);
    } while (next_permutation(idx, idx + VERTICES));
    if (fits.empty()) {
        puts("0");
        return 0;
    }
    for (auto &order : fits) {
        ll dx = order[0].x - token[0].x, dy = order[0].y - token[0].y;
        bool shift = true;
        for (int i = 1; i < VERTICES; i++)
            shift = shift && order[i].x - token[i].x == dx && order[i].y - token[i].y == dy;
        if (shift) {
            printf("1 %s %s\n", decimal(dx, 1).c_str(), decimal(dy, 1).c_str());
            return 0;
        }
    }

    vector<P> &order = fits[0];
    ll ux = token[1].x - token[0].x, uy = token[1].y - token[0].y;
    ll wx = order[1].x - order[0].x, wy = order[1].y - order[0].y;
    double angle =
        atan2((double)(ux * wy - uy * wx), (double)(ux * wx + uy * wy)) * HALF_TURN / acos(-1.0);
    if (angle < 0)
        angle += FULL_TURN;

    // the centre is a vertex that stays, or it lies on the perpendicular
    // bisector of every vertex and its image: 2 d . c = |t|^2 - |s|^2
    string cx, cy;
    for (int i = 0; i < VERTICES; i++)
        if (token[i].x == order[i].x && token[i].y == order[i].y)
            cx = decimal(token[i].x, 1), cy = decimal(token[i].y, 1);
    if (cx.empty()) {
        ll a[VERTICES], b[VERTICES], e[VERTICES];
        for (int i = 0; i < VERTICES; i++) {
            a[i] = 2 * (order[i].x - token[i].x);
            b[i] = 2 * (order[i].y - token[i].y);
            e[i] = order[i].x * order[i].x + order[i].y * order[i].y - token[i].x * token[i].x -
                   token[i].y * token[i].y;
        }
        for (int i = 0; i < VERTICES && cx.empty(); i++)
            for (int j = i + 1; j < VERTICES && cx.empty(); j++) {
                ll det = a[i] * b[j] - a[j] * b[i];
                if (det) {
                    cx = decimal(e[i] * b[j] - e[j] * b[i], det);
                    cy = decimal(a[i] * e[j] - a[j] * e[i], det);
                }
            }
    }
    printf("2 %s %s %.10f\n", cx.c_str(), cy.c_str(), angle);
}
