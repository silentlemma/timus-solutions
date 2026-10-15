#include <algorithm>
#include <cmath>
#include <cstdio>

typedef long long ll;

const int DIM = 3;

void cross(const double u[], const double v[], double w[]) {
    w[0] = u[1] * v[2] - u[2] * v[1];
    w[1] = u[2] * v[0] - u[0] * v[2];
    w[2] = u[0] * v[1] - u[1] * v[0];
}

int main() {
    ll a, b, p[DIM], q[DIM], d[DIM];
    scanf("%lld %lld", &a, &b);
    for (ll& x : p) {
        scanf("%lld", &x);
    }
    for (ll& x : q) {
        scanf("%lld", &x);
    }
    for (int i = 0; i < DIM; i++) {
        d[i] = q[i] - p[i];
    }
    // the elbow's axis is parallel to the rail and across both segments, so the
    // shoulder, the elbow and the claw lie in the plane through the shoulder
    // across the rail, and the claw sits at the rail's point h nearest to it
    ll c[DIM] = {p[1] * d[2] - p[2] * d[1], p[2] * d[0] - p[0] * d[2], p[0] * d[1] - p[1] * d[0]};
    ll dd = d[0] * d[0] + d[1] * d[1] + d[2] * d[2];
    ll num = c[0] * c[0] + c[1] * c[1] + c[2] * c[2];  // |h|^2 = num / dd, exactly
    // the bend (the angle opposite h) is not acute and the triangle closes:
    // a^2 + b^2 <= |h|^2 <= (a + b)^2
    if (!((a * a + b * b) * dd <= num && num <= (a + b) * (a + b) * dd)) {
        printf("No solution.\n");
        return 0;
    }
    double t = -(double)(p[0] * d[0] + p[1] * d[1] + p[2] * d[2]) / dd;
    double r = std::sqrt((double)num / dd), e1[DIM], unit[DIM], e2[DIM];
    for (int i = 0; i < DIM; i++) {
        e1[i] = (p[i] + t * d[i]) / r;
        unit[i] = d[i] / std::sqrt((double)dd);
    }
    cross(unit, e1, e2);
    // the elbow is at distance a from the shoulder and b from h
    double along = (a * a - b * b + r * r) / (2 * r);
    double side = std::sqrt(std::max(0.0, a * a - along * along));
    double bend = std::acos(std::max(-1.0, std::min(1.0, (a * a + b * b - r * r) / (2.0 * a * b))));
    for (int i = 0; i < DIM; i++) {
        printf("%.15f ", along * e1[i] + side * e2[i]);
    }
    printf("%.15f\n", bend);
}
