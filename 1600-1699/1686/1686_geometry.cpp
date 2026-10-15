#include <algorithm>
#include <cstdio>

typedef long long ll;

const int DIM = 3;
const int VERTICES = 4;
// each face and the vertex opposite it
const int FACES[VERTICES][VERTICES] = {{0, 1, 2, 3}, {0, 1, 3, 2}, {0, 2, 3, 1}, {1, 2, 3, 0}};
const int OPPOSITE = 3;

int main() {
    ll v[VERTICES][DIM];
    for (auto& p : v) {
        scanf("%lld %lld %lld", &p[0], &p[1], &p[2]);
    }
    int n;
    scanf("%d", &n);
    ll normals[VERTICES][DIM];
    for (int f = 0; f < VERTICES; f++) {
        const int* face = FACES[f];
        ll u[DIM], w[DIM], d[DIM];
        for (int t = 0; t < DIM; t++) {
            u[t] = v[face[1]][t] - v[face[0]][t];
            w[t] = v[face[2]][t] - v[face[0]][t];
            d[t] = v[face[OPPOSITE]][t] - v[face[0]][t];
        }
        ll* c = normals[f];
        c[0] = u[1] * w[2] - u[2] * w[1];
        c[1] = u[2] * w[0] - u[0] * w[2];
        c[2] = u[0] * w[1] - u[1] * w[0];
        // point the cross product, twice the face area long, away from the body
        if (c[0] * d[0] + c[1] * d[1] + c[2] * d[2] > 0) {
            for (int t = 0; t < DIM; t++) {
                c[t] = -c[t];
            }
        }
    }
    // a lit face gives area * intensity * cosine = (cross . star) / 2, and the
    // doubled total is a plain integer sum; the body is convex, so no shadows
    ll total = 0;
    for (int i = 0; i < n; i++) {
        ll s[DIM];
        scanf("%lld %lld %lld", &s[0], &s[1], &s[2]);
        for (auto& c : normals) {
            total += std::max(0LL, c[0] * s[0] + c[1] * s[1] + c[2] * s[2]);
        }
    }
    printf("%lld.00000\n", total);
}
