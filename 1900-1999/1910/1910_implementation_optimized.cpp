#include <cstdio>

int main() {
    // the sections are not stored: only the two before the current one are kept
    int n, previous, last;
    scanf("%d%d%d", &n, &previous, &last);
    int best = 0, position = 2;
    for (int middle = 2; middle < n; ++middle) {
        int value;
        scanf("%d", &value);
        int sum = previous + last + value;
        if (sum > best) {
            best = sum;
            position = middle;
        }
        previous = last;
        last = value;
    }
    printf("%d %d\n", best, position);
}
