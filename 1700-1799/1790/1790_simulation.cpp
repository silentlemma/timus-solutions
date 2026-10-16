#include <cstdio>
#include <utility>

// the pedestals lo, lo + 2, ..., hi where the artifact may be; empty when
// lo > hi
struct Run {
    int lo, hi;
    bool empty() const { return lo > hi; }
};

// a touch inside the run leaves a hole that the next move fills again,
// so only a touch at an end shrinks it
void touch(Run &run, int x) {
    if (run.empty()) return;
    if (x == run.lo) {
        run.lo += 2;
    } else if (x == run.hi) {
        run.hi -= 2;
    }
}

Run spread(Run run, int n) {
    if (run.empty()) return run;
    return {run.lo > 1 ? run.lo - 1 : run.lo + 1, run.hi < n ? run.hi + 1 : run.hi - 1};
}

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2) return 0;
    // runs[p] holds the pedestals of parity p
    Run runs[2] = {{2, n % 2 == 0 ? n : n - 1}, {1, n % 2 == 1 ? n : n - 1}};
    for (int i = 0; i < m; i++) {
        int x;
        if (scanf("%d", &x) != 1) break;
        touch(runs[x % 2], x);
        // every step flips the parity of the pedestal
        Run even = spread(runs[1], n), odd = spread(runs[0], n);
        runs[0] = even;
        runs[1] = odd;
    }
    puts(runs[0].empty() && runs[1].empty() ? "YES" : "NO");
    return 0;
}
