#include <cstdio>

// four times the square of the shortest longest chord of a cover: a circle's
// diameter, a square's side, a triangle's height
long long narrowest(int kind, long long size) {
    const long long factor[] = {0, 16, 4, 3};
    return factor[kind] * size * size;
}

// four times the square of the longest segment in a hole: a circle's
// diameter, a square's diagonal, a triangle's side
long long widest(int kind, long long size) {
    const long long factor[] = {0, 16, 8, 4};
    return factor[kind] * size * size;
}

int main() {
    int kind, size, n, count = 0;
    if (scanf("%d %d", &kind, &size) != 2 || scanf("%d", &n) != 1)
        return 0;
    long long hole = widest(kind, size);
    // a cover held upright crosses the plane of the hole along parallel chords,
    // so it passes when its longest chord in some direction fits in the hole
    for (int i = 0; i < n; i++) {
        if (scanf("%d %d", &kind, &size) != 2)
            return 0;
        if (narrowest(kind, size) <= hole)
            count++;
    }
    printf("%d\n", count);
}
