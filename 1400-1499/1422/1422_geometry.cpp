#include <algorithm>
#include <array>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

const int DIMS = 3; // x, y and z
typedef array<int, DIMS> Dir;

int gcd(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<Dir> p(n);
    for (Dir &q : p)
        scanf("%d %d %d", &q[0], &q[1], &q[2]);
    int best = 1;
    vector<Dir> dirs;
    for (int i = 0; i < n && n - i > best; i++) {
        int same = 0;
        dirs.clear();
        for (int j = i + 1; j < n; j++) {
            int dx = p[j][0] - p[i][0], dy = p[j][1] - p[i][1], dz = p[j][2] - p[i][2];
            int g = gcd(abs(dx), gcd(abs(dy), abs(dz)));
            if (g == 0) {
                same++; // several flies may hang at one point
                continue;
            }
            // one key per direction: reduced, with the first non-zero part positive
            if (dx < 0 || (dx == 0 && (dy < 0 || (dy == 0 && dz < 0))))
                g = -g;
            dirs.push_back({dx / g, dy / g, dz / g});
        }
        sort(dirs.begin(), dirs.end());
        int most = 0;
        for (size_t a = 0, b = 0; a < dirs.size(); a = b) {
            while (b < dirs.size() && dirs[b] == dirs[a])
                b++;
            most = max(most, (int)(b - a));
        }
        best = max(best, 1 + same + most);
    }
    printf("%d\n", best);
}
