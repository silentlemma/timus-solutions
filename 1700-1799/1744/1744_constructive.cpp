#include <cstdio>
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    // every day uses three pairs and every pair may meet three times, so
    // at most n (n - 1) / 2 days; the triples i, i + d, i + 2d modulo n
    // give each pair three meetings: twice as neighbours, once apart
    printf("%d\n", n * (n - 1) / 2);
    for (int d = 1; d <= (n - 1) / 2; d++) {
        for (int i = 0; i < n; i++) {
            printf("%d %d %d\n", i + 1, (i + d) % n + 1, (i + 2 * d) % n + 1);
        }
    }
}
