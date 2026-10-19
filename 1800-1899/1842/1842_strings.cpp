#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

// start of the lexicographically greatest suffix (the least one when flip
// is set), by the comparison loop of the Two-Way algorithm
static int suffixStart(const std::string &w, bool flip) {
    int n = w.size(), best = -1, j = 0, k = 1, p = 1;
    while (j + k < n) {
        char a = w[j + k], b = w[best + k];
        if (a != b && (a < b) != flip) {
            j += k;
            k = 1;
            p = j - best;
        } else if (a == b) {
            if (k != p) {
                k++;
            } else {
                j += p;
                k = 1;
            }
        } else {
            best = j;
            j = best + 1;
            k = 1;
            p = 1;
        }
    }
    return best + 1;
}

int main() {
    std::string w;
    for (int c = getchar(); c != EOF; c = getchar()) {
        if (c >= 'a' && c <= 'z') w += char(c);
    }
    int n = w.size();
    // the longest border gives the period of the word
    std::vector<int> border(n, 0);
    for (int i = 1, k = 0; i < n; i++) {
        while (k && w[k] != w[i]) k = border[k - 1];
        if (w[k] == w[i]) k++;
        border[i] = k;
    }
    // the critical factorization theorem: the split before the later of the
    // two greatest suffixes has a local root as long as the period (both are
    // the whole word only for a power of one letter)
    int split = std::max({suffixStart(w, false), suffixStart(w, true), 1});
    printf("%d %d\n", split, n - border[n - 1]);
    return 0;
}
