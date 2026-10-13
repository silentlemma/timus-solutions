#include <algorithm>
#include <cstdio>

const int TOP = 30;

int main() {
    int n, count[TOP + 2] = {};
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int c;
        scanf("%d", &c);
        count[c]++;
    }
    // two types share a symmetric alternating row only as ABA...BA, counts differing by one,
    // along the chain of counts, pairing the leftovers of c with c + 1 at once is best
    int pairs = 0, left = 0;
    for (int c = 1; c <= TOP; c++) {
        int matched = std::min(left, count[c]);
        pairs += matched;
        left = count[c] - matched;
    }
    printf("%d\n", n - pairs);
}
