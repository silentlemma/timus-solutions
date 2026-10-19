#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>

using namespace std;
typedef long long ll;

constexpr ll QUAD = 4;  // the discriminant of a t^2 + b t + c is b^2 - 4 a c

// compares sign * sqrt(disc) with the integer k exactly: -1, 0 or 1
int signSqrtVs(int sign, ll disc, ll k) {
    if (sign > 0) {
        if (k < 0) return 1;
        return (disc > k * k) - (disc < k * k);
    }
    if (k > 0) return -1;
    return (k * k > disc) - (k * k < disc);
}

int main() {
    ll x, y, z, vx, vy, ex, ey;
    scanf("%lld %lld %lld %lld %lld %lld %lld", &x, &y, &z, &vx, &vy, &ex, &ey);
    // Stewart: the point at fraction t of the way from Denis to the hall is at
    // squared distance (1 - t) X^2 + t Y^2 - t (1 - t) Z^2 from Vanya; Eugene is
    // at d^2, so t solves z2 t^2 + b t + c = 0 with integer coefficients
    ll d2 = (ex - vx) * (ex - vx) + (ey - vy) * (ey - vy);
    ll z2 = z * z, b = y * y - x * x - z2, c = x * x - d2;
    ll disc = b * b - QUAD * z2 * c;
    vector<pair<double, bool>> found;  // t, and whether Eugene is at Denis's place
    if (disc >= 0) {
        for (int s : {1, -1}) {
            if (s < 0 && disc == 0) break;
            // t = (-b + s sqrt(disc)) / (2 z2) must lie in [0, 1]
            if (signSqrtVs(s, disc, b) < 0 || signSqrtVs(s, disc, 2 * z2 + b) > 0) continue;
            double t = (-b + s * sqrt((double)disc)) / (2.0 * z2);
            found.push_back({t, c == 0 && signSqrtVs(s, disc, b) == 0});
        }
    }
    // a model triangle: Vanya at 0, Denis on the x axis, the hall above it
    double cosV = double(x * x + y * y - z2) / (2.0 * x * y);
    double hx = y * cosV, hy = y * sqrt(max(0.0, 1 - cosV * cosV));
    double ux = ex - vx, uy = ey - vy;
    vector<pair<double, double>> points;
    for (auto [t, atDenis] : found) {
        double px = x + t * (hx - x), py = t * hy;
        for (int mirror : {1, -1}) {
            if (mirror < 0 && atDenis) break;
            // rotate (and maybe reflect) the model so that its point lands on Eugene
            double qx = px, qy = mirror * py, norm = qx * qx + qy * qy;
            double cosR = (qx * ux + qy * uy) / norm, sinR = (qx * uy - qy * ux) / norm;
            points.push_back({vx + cosR * x, vy + sinR * x});
        }
    }
    printf("%d\n", (int)points.size());
    for (auto [px, py] : points) printf("%.12f %.12f\n", px, py);
}
