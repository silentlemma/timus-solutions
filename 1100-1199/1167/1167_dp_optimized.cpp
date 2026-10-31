#include <algorithm>
#include <cstdio>
#include <utility>

int n;
constexpr int MAX_HORSES = 500;
// n <= 500; three fixed rows avoid heap storage and repeated allocation.
int black[MAX_HORSES + 1], first[MAX_HORSES + 1], second[MAX_HORSES + 1];
int *prev = first, *cur = second;

// horses j..i-1 in one stable: black times white
int cost(int j, int i) {
    int b = black[i] - black[j];
    return b * (i - j - b);
}

// fills cur[lo..hi] knowing that their best last splits lie in
// [optLo, optHi]
void solve(int lo, int hi, int optLo, int optHi) {
    if (lo > hi) {
        return;
    }
    int mid = (lo + hi) / 2, arg = optLo;
    long long best = -1;
    for (int j = optLo; j <= std::min(mid - 1, optHi); j++) {
        long long v = (long long)prev[j] + cost(j, mid);
        if (best < 0 || v < best) {
            best = v;
            arg = j;
        }
    }
    cur[mid] = best;
    solve(lo, mid - 1, optLo, arg);
    solve(mid + 1, hi, arg, optHi);
}

int main() {
    int k;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        int c;
        scanf("%d", &c);
        black[i + 1] = black[i] + c;
    }
    // prev[j]: the least unhappiness of the first j horses in the stables
    // so far; with no stables only j = 0 is possible
    const int NONE = 1000000000;
    std::fill(prev, prev + n + 1, NONE);
    prev[0] = 0;
    for (int stables = 1; stables <= k; stables++) {
        // the best last split never moves left as i grows (the black-white
        // cost satisfies the quadrangle inequality)
        solve(stables, n, stables - 1, n - 1);
        std::swap(prev, cur);
    }
    printf("%d\n", prev[n]);
}
