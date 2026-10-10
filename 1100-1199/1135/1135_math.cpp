#include <cstdio>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // a turning pair "><" becomes "<>", a swap of neighbours that removes one
    // pair with '>' before '<', so the count of such pairs is the answer
    long long right = 0, turns = 0;
    for (int seen = 0; seen < n;) {
        int c = getchar();
        if (c == EOF)
            break;
        if (c == '>') {
            right++;
            seen++;
        } else if (c == '<') {
            turns += right;
            seen++;
        }
    }
    printf("%lld\n", turns);
}
