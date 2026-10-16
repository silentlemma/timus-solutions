#include <cstdio>

typedef long long ll;
typedef __int128 big;

const int CORNERS = 3, POINTS = 5;

int main() {
    ll mana, h, top, x[POINTS], y[POINTS];
    if (scanf("%lld %lld %lld", &mana, &h, &top) < 1) return 0;
    for (int i = 0; i < POINTS; i++) scanf("%lld %lld", &x[i], &y[i]);
    // after flying up, mana - h is left for the radius, and the field must
    // reach the nearest of the floor and the three walls
    ll spare = mana - h;
    bool ok = spare >= h;
    for (int i = 1; i <= CORNERS && spare >= 0; i++) {
        int j = i % CORNERS + 1;
        ll ux = x[j] - x[i], uy = y[j] - y[i];
        ll wx = x[CORNERS + 1] - x[i], wy = y[CORNERS + 1] - y[i], wz = top;
        ll nx = uy * wz, ny = -ux * wz, nz = ux * wy - uy * wx;
        ll reach = nx * (x[0] - x[i]) + ny * (y[0] - y[i]) + nz * h;
        // the distance to the wall is reach / |normal|, compared exactly
        big length = (big)nx * nx + (big)ny * ny + (big)nz * nz;
        if ((big)reach * reach <= (big)spare * spare * length) ok = true;
    }
    puts(ok && spare >= 0 ? "YES" : "NO");
    return 0;
}
