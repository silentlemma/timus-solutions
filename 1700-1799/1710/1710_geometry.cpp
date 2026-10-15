#include <cstdio>

int main() {
    long long ax, ay, bx, by, cx, cy;
    scanf("%lld %lld %lld %lld %lld %lld", &ax, &ay, &bx, &by, &cx, &cy);
    // C' on the ray AC with |BC'| = |BC| is the other root t of
    // t^2 - 2 t (AB . u) + |AB|^2 - |BC|^2 = 0, u the unit vector along AC:
    // t' = 2 (AB . AC) / |AC| - |AC|, so C' = A + (C - A) (2 dot - |AC|^2) / |AC|^2
    long long dot = (bx - ax) * (cx - ax) + (by - ay) * (cy - ay);
    long long side = (cx - ax) * (cx - ax) + (cy - ay) * (cy - ay);
    if (2 * dot <= side || dot == side) {
        printf("YES\n");
        return 0;
    }
    double k = (double)(2 * dot - side) / side;
    printf("NO\n%.10f %.10f\n%.10f %.10f\n", (double)ax, (double)ay, (double)bx, (double)by);
    printf("%.10f %.10f\n", ax + (cx - ax) * k, ay + (cy - ay) * k);
}
