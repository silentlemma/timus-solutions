#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    // a row ends in white or red; it comes from a row one shorter ending in
    // the other of the two, or from one two shorter followed by blue
    long long prev = 2, cur = 2;
    for (int i = 2; i < n; i++) {
        long long next = prev + cur;
        prev = cur;
        cur = next;
    }
    printf("%lld\n", cur);
}
