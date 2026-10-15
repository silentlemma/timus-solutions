#include <algorithm>
#include <cmath>
#include <cstdio>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // Sandro's own spot holds no demon: stay there and reach the farthest one
    double farthest = 0;
    for (int i = 0; i < n; i++) {
        int x, y;
        if (scanf("%d %d", &x, &y) != 2)
            return 0;
        farthest = std::max(farthest, std::hypot((double)x, (double)y));
    }
    printf("0 0 %.10f\n", farthest);
}
