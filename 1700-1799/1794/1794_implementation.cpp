#include <cstdio>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    // votes[k]: how many students get their wish if student k starts
    std::vector<int> votes(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        int want;
        if (scanf("%d", &want) != 1) return 0;
        // student i speaks want-th when student i - want + 1 starts
        int start = ((i - want) % n + n) % n + 1;
        votes[start]++;
    }
    int best = 1;
    for (int k = 2; k <= n; k++) {
        if (votes[k] > votes[best]) best = k;
    }
    printf("%d\n", best);
    return 0;
}
