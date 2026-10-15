#include <cstdio>

const int FAR = 2000;  // beyond every coordinate

int main() {
    int n, x;
    if (scanf("%d %d", &n, &x) != 2)
        return 0;
    // the nearest obstacles on both sides; walking away from the exit is
    // promised to meet one, so the one needed below always exists
    int left = -FAR, right = FAR;
    for (int i = 0; i < n; i++) {
        int w;
        if (scanf("%d", &w) != 1)
            return 0;
        if (w < 0 && w > left)
            left = w;
        if (w > 0 && w < right)
            right = w;
    }
    if (x < left || x > right)
        puts("Impossible");  // an obstacle stands between the start and the exit
    else if (x > 0)
        printf("%d %d\n", x, -2 * left + x);
    else
        printf("%d %d\n", 2 * right - x, -x);
}
