#include <cstdio>

// everyone on the far side of Vasya can be made to trip except the two
// seats at the far end, who always come in from their own end
const int SAFE = 2;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    int far = k - 1 > n - k ? k - 1 : n - k;
    // stdio avoids the iostream runtime for just two input numbers.
    printf("%d\n", far > SAFE ? far - SAFE : 0);
}
