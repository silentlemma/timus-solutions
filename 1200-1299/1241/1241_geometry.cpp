#include <cstdio>
#include <numeric>
#include <vector>

// the four small triangles of a unit square, cut by both its diagonals
enum { SOUTH, EAST, NORTH, WEST, PARTS };
// outward directions of a triangle's edges, counterclockwise from +x
enum { RIGHT, UP_RIGHT, UP, UP_LEFT, LEFT, DOWN_LEFT, DOWN, DOWN_RIGHT };
const int TRIANGLE = 3;

std::vector<int> parent;
std::vector<unsigned> out;

int find(int a) {
    while (parent[a] != a)
        a = parent[a] = parent[parent[a]];
    return a;
}

// joins two small triangles, or records their outward directions when a
// cut separates them
void side(int a, int da, int b, int db, bool cut) {
    if (cut) {
        out[a] |= 1u << da;
        out[b] |= 1u << db;
    } else {
        parent[find(a)] = find(b);
    }
}

int main() {
    int m, n, k;
    scanf("%d %d %d", &m, &n, &k);
    // a cut runs from border to border, so it is a whole line of one of the
    // four kinds: x = c, y = c, x - y = c or x + y = c
    std::vector<bool> vert(m + 1), hor(n + 1), diff(m + n + 1), sum(m + n + 1);
    while (k--) {
        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        if (x1 == x2)
            vert[x1] = true;
        else if (y1 == y2)
            hor[y1] = true;
        else if (x2 - x1 == y2 - y1)
            diff[x1 - y1 + n] = true;
        else
            sum[x1 + y1] = true;
    }
    auto cell = [&](int i, int j, int t) { return (i * n + j) * PARTS + t; };
    parent.resize(m * n * PARTS);
    std::iota(parent.begin(), parent.end(), 0);
    out.assign(m * n * PARTS, 0);
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            int s = cell(i, j, SOUTH), e = cell(i, j, EAST), no = cell(i, j, NORTH),
                w = cell(i, j, WEST);
            side(s, UP_RIGHT, e, DOWN_LEFT, sum[i + j + 1]);
            side(s, UP_LEFT, w, DOWN_RIGHT, diff[i - j + n]);
            side(e, UP_LEFT, no, DOWN_RIGHT, diff[i - j + n]);
            side(no, DOWN_LEFT, w, UP_RIGHT, sum[i + j + 1]);
            if (j == 0)
                out[s] |= 1u << DOWN;
            else
                side(s, DOWN, cell(i, j - 1, NORTH), UP, hor[j]);
            if (i == 0)
                out[w] |= 1u << LEFT;
            else
                side(w, LEFT, cell(i - 1, j, EAST), RIGHT, vert[i]);
            if (j == n - 1)
                out[no] |= 1u << UP;
            if (i == m - 1)
                out[e] |= 1u << RIGHT;
        }
    // every piece is convex with sides in these 8 directions, one side per
    // direction, so a piece is a triangle when its edges face 3 directions
    std::vector<unsigned> faces(out.size(), 0);
    for (size_t a = 0; a < out.size(); a++)
        faces[find(a)] |= out[a];
    int count = 0;
    for (size_t a = 0; a < faces.size(); a++)
        if (find(a) == (int)a && __builtin_popcount(faces[a]) == TRIANGLE)
            count++;
    printf("%d\n", count);
}
