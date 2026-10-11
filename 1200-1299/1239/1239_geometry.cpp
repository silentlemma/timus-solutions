#include <cmath>
#include <cstdio>
#include <vector>

typedef long long ll;
typedef __int128 big;

const double EPS = 1e-9;

int main() {
    int n;
    scanf("%d", &n);
    std::vector<ll> x(n), y(n), z(n), r(n);
    for (int i = 0; i < n; i++)
        scanf("%lld %lld %lld %lld", &x[i], &y[i], &z[i], &r[i]);
    // a ray along d touches ghost i when d.C_i >= L_i |d|, where L_i is the
    // length of a tangent from the gun: L_i^2 = |C_i|^2 - R_i^2
    std::vector<ll> norm(n), tan2(n);
    std::vector<double> tan(n);
    std::vector<std::vector<ll>> dot(n, std::vector<ll>(n));
    for (int i = 0; i < n; i++) {
        norm[i] = x[i] * x[i] + y[i] * y[i] + z[i] * z[i];
        tan2[i] = norm[i] - r[i] * r[i];
        tan[i] = std::sqrt((double)tan2[i]);
    }
    for (int i = 0; i < n; i++)
        for (int k = 0; k < n; k++)
            dot[i][k] = x[i] * x[k] + y[i] * y[k] + z[i] * z[k];
    std::vector<int> best, hit;
    // the ray through the centre of ghost i, tested exactly in integers
    for (int i = 0; i < n; i++) {
        hit.clear();
        for (int k = 0; k < n; k++)
            if (dot[i][k] * dot[i][k] >= tan2[k] * norm[i])
                hit.push_back(k);
        if (hit.size() > best.size())
            best = hit;
    }
    // rays touching two ghosts i and j: d = (a C_i + b C_j + c C_i x C_j) / det
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) {
            ll g = dot[i][j], det = norm[i] * norm[j] - g * g;
            if (det == 0)
                continue;
            // 1 - |a C_i + b C_j|^2 = Q / det with Q = base + 2 g L_i L_j
            ll base = det - tan2[i] * norm[j] - tan2[j] * norm[i], p = tan2[i] * tan2[j];
            big gap = (big)(2 * g * 2 * g) * p - (big)base * base;
            if (base < 0 && gap < 0)
                continue; // the two outlines do not meet
            double root = std::sqrt((double)p), q;
            if (base >= 0)
                q = base + 2.0 * g * root;
            else
                q = (double)gap / (2.0 * g * root - base);
            // a det and b det, rationalised to avoid cancellation
            big na = (big)(tan2[i] * norm[j]) * norm[j] - (big)(tan2[j] * g) * g;
            big nb = (big)(tan2[j] * norm[i]) * norm[i] - (big)(tan2[i] * g) * g;
            double ad = (double)na / (tan[i] * norm[j] + tan[j] * g);
            double bd = (double)nb / (tan[j] * norm[i] + tan[i] * g);
            ll cx = y[i] * z[j] - z[i] * y[j], cy = z[i] * x[j] - x[i] * z[j],
               cz = x[i] * y[j] - y[i] * x[j];
            for (int sign = 1; sign >= -1; sign -= 2) {
                if (sign < 0 && q == 0)
                    break;
                double s = sign * std::sqrt(q);
                hit.clear();
                for (int k = 0; k < n; k++) {
                    double t = (double)(cx * x[k] + cy * y[k] + cz * z[k]);
                    double v = ad * dot[i][k] + bd * dot[j][k] + s * t;
                    if (k == i || k == j || v >= (double)det * tan[k] * (1 - EPS))
                        hit.push_back(k);
                }
                if (hit.size() > best.size())
                    best = hit;
            }
        }
    printf("%d\n", (int)best.size());
    for (size_t i = 0; i < best.size(); i++)
        printf(i ? " %d" : "%d", best[i] + 1);
    printf("\n");
}
