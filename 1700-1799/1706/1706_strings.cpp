#include <cstdio>
#include <string>
#include <vector>

const int COPIES = 4;  // the text repeated so that every comparison below stays inside it
const int MAX_LEN = 4096;

int main() {
    int k;
    static char buffer[MAX_LEN + 1];
    scanf("%d %4096s", &k, buffer);
    std::string s = buffer;
    int n = s.size();
    std::string t;
    for (int c = 0; c < COPIES; c++) {
        t += s;
    }
    // a substring is counted at its leftmost start j in the window [a, a + k):
    // its lengths up to a + k - j minus the longest common prefix of j with an
    // earlier start of the window, best[j]; going down over a adds start a
    int top = n + 2 * k;
    std::vector<int> common(k, 0);  // common[d] = lcp of positions a and a + d
    std::vector<int> best(top + k, 0);
    std::vector<long long> answers(n);
    for (int a = top; a >= 0; a--) {
        char ca = t[a];
        for (int d = 1; d < k; d++) {
            int j = a + d;
            if (t[j] == ca) {
                common[d]++;
                if (common[d] > best[j]) {
                    best[j] = common[d];
                }
            } else {
                common[d] = 0;
            }
        }
        if (a < n) {
            int end = a + k;
            long long total = 0;
            for (int j = a; j < end; j++) {
                int fresh = end - j - best[j];
                if (fresh > 0) {
                    total += fresh;
                }
            }
            answers[a] = total;
        }
    }
    for (int i = 0; i < n; i++) {
        printf(i ? " %lld" : "%lld", answers[i]);
    }
    printf("\n");
}
