#include <algorithm>
#include <cmath>
#include <cstdio>
#include <numeric>
#include <vector>

using namespace std;

const double EPS = 1e-9;
const double BOX = 2;  // the starting cell is a square of half-side BOX * R around the table
const double SPAN = 4; // a piece cuts a cell only within twice its reach: squared, 4 times

struct Pt {
    double x, y;
};

double norm2(Pt p) { return p.x * p.x + p.y * p.y; }

// the part of the convex polygon with (p - m) . d <= 0
vector<Pt> clip(const vector<Pt> &poly, Pt m, Pt d) {
    vector<Pt> out;
    size_t n = poly.size();
    for (size_t k = 0; k < n; k++) {
        Pt p = poly[k], q = poly[(k + 1) % n];
        double sp = (p.x - m.x) * d.x + (p.y - m.y) * d.y;
        double sq = (q.x - m.x) * d.x + (q.y - m.y) * d.y;
        if (sp <= 0)
            out.push_back(p);
        if ((sp < 0 && sq > 0) || (sq < 0 && sp > 0)) {
            double t = sp / (sp - sq);
            out.push_back({p.x + t * (q.x - p.x), p.y + t * (q.y - p.y)});
        }
    }
    return out;
}

// a point of the table edge where piece i is the nearest: the Voronoi cell
// of the piece is convex and reaches the edge exactly when its farthest
// vertex from the centre is at least R away
bool seat(const vector<Pt> &pieces, int i, double r, Pt &answer) {
    Pt c = pieces[i];
    double side = BOX * r, limit = r * r - EPS;
    vector<Pt> poly = {{-side, -side}, {side, -side}, {side, side}, {-side, side}};
    int k = pieces.size();
    vector<double> dist(k);
    for (int j = 0; j < k; j++)
        dist[j] = norm2({pieces[j].x - c.x, pieces[j].y - c.y});
    vector<int> order(k);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int a, int b) { return dist[a] < dist[b]; });
    for (int j : order) {
        if (j == i)
            continue;
        double reach = 0;
        for (Pt v : poly)
            reach = max(reach, norm2({v.x - c.x, v.y - c.y}));
        if (dist[j] > SPAN * reach)
            break; // farther than twice the cell's reach: cannot cut it
        Pt o = pieces[j];
        poly = clip(poly, {(o.x + c.x) / 2, (o.y + c.y) / 2}, {o.x - c.x, o.y - c.y});
        double far = 0;
        for (Pt v : poly)
            far = max(far, norm2(v));
        if (far < limit)
            return false;
    }
    Pt v = *max_element(poly.begin(), poly.end(), [](Pt a, Pt b) { return norm2(a) < norm2(b); });
    // the segment from the piece to that vertex lies in the cell and crosses
    // the edge: solve |c + t (v - c)| = R
    Pt u = {v.x - c.x, v.y - c.y};
    double a = norm2(u), b = c.x * u.x + c.y * u.y, cc = norm2(c) - r * r;
    double t = min(1.0, (-b + sqrt(max(0.0, b * b - a * cc))) / a);
    Pt p = {c.x + t * u.x, c.y + t * u.y};
    double len = sqrt(norm2(p));
    answer = {p.x * r / len, p.y * r / len};
    return true;
}

int main() {
    double r;
    int k;
    scanf("%lf %d", &r, &k);
    vector<Pt> pieces(k);
    vector<int> weight(k), order(k);
    for (int i = 0; i < k; i++)
        scanf("%lf %lf %d", &pieces[i].x, &pieces[i].y, &weight[i]);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int a, int b) { return weight[a] > weight[b]; });
    Pt answer;
    for (int i : order)
        if (seat(pieces, i, r, answer)) {
            printf("%.10f %.10f\n", answer.x, answer.y);
            return 0;
        }
}
