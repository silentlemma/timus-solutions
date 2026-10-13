#include <algorithm>
#include <cmath>
#include <cstdio>
#include <tuple>
#include <unordered_map>
#include <vector>

using namespace std;

const double CELL = 1e-3; // distinct crossing points are at least this far apart
const double SAME = 1e-4; // two estimates of one point are much closer than this

const long long ROW = 1LL << 32;   // grid cells as one number: x * ROW + y
const long long SHIFT = 1LL << 31; // keeps cell numbers positive

vector<double> px, py;
unordered_map<long long, vector<int>> grid;

int pointId(double x, double y) {
    long long cx = (long long)floor(x / CELL), cy = (long long)floor(y / CELL);
    for (long long gx = cx - 1; gx <= cx + 1; gx++)
        for (long long gy = cy - 1; gy <= cy + 1; gy++) {
            auto it = grid.find((gx + SHIFT) * ROW + gy + SHIFT);
            if (it == grid.end())
                continue;
            for (int p : it->second)
                if (fabs(px[p] - x) < SAME && fabs(py[p] - y) < SAME)
                    return p;
        }
    px.push_back(x);
    py.push_back(y);
    grid[(cx + SHIFT) * ROW + cy + SHIFT].push_back(px.size() - 1);
    return px.size() - 1;
}

vector<int> parent;

int find(int a) {
    while (parent[a] != a)
        a = parent[a] = parent[parent[a]];
    return a;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<tuple<long long, long long, long long>> circles(n);
    for (auto &[x, y, r] : circles)
        scanf("%lld %lld %lld", &x, &y, &r);
    // a cut made twice is still one cut
    sort(circles.begin(), circles.end());
    circles.erase(unique(circles.begin(), circles.end()), circles.end());
    int k = circles.size();
    parent.resize(k);
    for (int i = 0; i < k; i++)
        parent[i] = i;
    vector<vector<int>> onCircle(k);
    for (int i = 0; i < k; i++) {
        auto [x1, y1, r1] = circles[i];
        for (int j = i + 1; j < k; j++) {
            auto [x2, y2, r2] = circles[j];
            long long dx = x2 - x1, dy = y2 - y1, d2 = dx * dx + dy * dy;
            if (d2 > (r1 + r2) * (r1 + r2) || d2 < (r1 - r2) * (r1 - r2))
                continue; // apart, or one inside the other
            // the crossings are p1 + (m * (dx, dy) +- sqrt(K) * (-dy, dx)) / (2 d2), K exact
            long long m = d2 + r1 * r1 - r2 * r2;
            double root = sqrt((double)((2 * r1) * (2 * r1) * d2 - m * m));
            for (int sign = 1; sign >= -1; sign -= 2) {
                double x = x1 + (m * dx - sign * root * dy) / (2.0 * d2);
                double y = y1 + (m * dy + sign * root * dx) / (2.0 * d2);
                int p = pointId(x, y);
                onCircle[i].push_back(p);
                onCircle[j].push_back(p);
                if (root == 0)
                    break;
            }
            parent[find(i)] = find(j);
        }
    }
    // Euler's formula for a plane graph: faces = edges - vertices + components + 1,
    // a circle with no crossings counts as one vertex and one edge
    long long edges = 0;
    int components = 0;
    for (int i = 0; i < k; i++) {
        sort(onCircle[i].begin(), onCircle[i].end());
        edges += unique(onCircle[i].begin(), onCircle[i].end()) - onCircle[i].begin();
        components += find(i) == i;
    }
    printf("%lld\n", edges - (long long)px.size() + components + 1);
}
