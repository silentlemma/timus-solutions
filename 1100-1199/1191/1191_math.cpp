#include <cstdio>

int main() {
    int gap, n;
    scanf("%d %d", &gap, &n);
    // at a stop with trams every k minutes the officer, arriving gap
    // minutes after the thief, leaves at best gap - gap % k minutes later,
    // and a gap below k means the thief may still be waiting there
    for (int i = 0; i < n; i++) {
        int k;
        scanf("%d", &k);
        gap -= gap % k;
        if (gap == 0) {
            printf("YES\n");
            return 0;
        }
    }
    printf("NO\n");
}
