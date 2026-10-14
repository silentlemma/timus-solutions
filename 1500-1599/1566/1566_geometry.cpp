#include <algorithm>
#include <cmath>
#include <cstdio>
using namespace std;

const double EPS = 1e-9; // touching counts as fitting
const int SIDES = 3;

// the third vertex of a triangle on the segment from (0, 0) to (base, 0)
// whose other sides are left (from the origin) and right
void apex(double base, double left, double right, double &x, double &y) {
    x = (base * base + left * left - right * right) / (2 * base);
    y = sqrt(max(0.0, left * left - x * x));
}

// can the card lie with its side card[0] on the envelope's side env[0], in
// either of its two mirror images?
bool fitsOn(const double env[], const double card[]) {
    double m = env[0], length = card[0], wx, height;
    if (length > m + EPS)
        return false;
    apex(m, env[1], env[2], wx, height);
    for (int mirror = 0; mirror < 2; mirror++) {
        double u, h;
        apex(length, card[1 + mirror], card[2 - mirror], u, h);
        if (h > height + EPS)
            continue;
        // the card slides along the side by t in [0, m - length]; its apex
        // (t + u, h) must stay between the envelope's two other sides
        double lo = max(0.0, h * wx / height - u);
        double hi = min(m - length, m - h * (m - wx) / height - u);
        if (lo <= hi + EPS)
            return true;
    }
    return false;
}

int main() {
    int e[SIDES], c[SIDES];
    for (int i = 0; i < SIDES; i++)
        if (scanf("%d", &e[i]) != 1)
            return 0;
    for (int i = 0; i < SIDES; i++)
        if (scanf("%d", &c[i]) != 1)
            return 0;
    sort(e, e + SIDES);
    sort(c, c + SIDES);
    bool fits = false;
    if (e[0] + e[1] == e[2]) {
        // a flat envelope holds only a flat card that is no longer
        fits = c[0] + c[1] == c[2] && c[2] <= e[2];
    } else {
        // a triangle fits in another one exactly when it fits with one of its
        // sides lying on a side of the other
        for (int i = 0; i < SIDES; i++)
            for (int j = 0; j < SIDES; j++) {
                double env[SIDES], card[SIDES];
                for (int k = 0; k < SIDES; k++) {
                    env[k] = e[(i + k) % SIDES];
                    card[k] = c[(j + k) % SIDES];
                }
                fits = fits || fitsOn(env, card);
            }
    }
    puts(fits ? "YES" : "NO");
}
