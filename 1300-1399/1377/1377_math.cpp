#include <algorithm>
#include <cstdio>
#include <cstdlib>

int index(int n, int m, int r, int c) {
    int layer = std::min({r, c, n - 1 - r, m - 1 - c});
    int height = n - 2 * layer, width = m - 2 * layer;
    r -= layer;
    c -= layer;
    // Outer layers contain the cells outside this remaining rectangle.
    int before = n * m - height * width, offset;
    if (height == 1)
        offset = c;
    else if (width == 1)
        offset = r;
    else if (r == 0)
        offset = c;
    else if (c == width - 1)
        offset = width - 1 + r;
    else if (r == height - 1)
        offset = width - 1 + height - 1 + width - 1 - c;
    else
        offset = 2 * (height + width - 2) - r;
    return before + offset;
}

int main() {
    int n, m, r1, c1, r2, c2;
    scanf("%d%d%d%d%d%d", &n, &m, &r1, &c1, &r2, &c2);
    printf("%d\n", std::abs(index(n, m, r1 - 1, c1 - 1) - index(n, m, r2 - 1, c2 - 1)));
}
