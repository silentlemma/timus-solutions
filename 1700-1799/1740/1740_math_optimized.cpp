#include <cstdio>

int main() {
    int l, k, h;
    // stdio avoids the iostream runtime for this constant-size input.
    scanf("%d %d %d", &l, &k, &h);
    // the time to reach x is x h / k plus a part that repeats every k km
    // and lies between 0 and h, so the last l mod k km take 0 to h hours
    int whole = l / k, rest = l % k;
    printf("%.8f %.8f\n", (double)whole * h, (double)(whole + (rest > 0)) * h);
}
