#include <cstdio>
#include <string>
#include <vector>
using namespace std;

const int LONGEST = 100, TOP = 9;  // digits allowed in the answer, largest digit
const int S1 = LONGEST * TOP, S2 = LONGEST * TOP * TOP;
const unsigned char NONE = 255;

int main() {
    // fewest[s1][s2]: the fewest nonzero digits with these sums, NONE if
    // more than 100 are needed or none will do
    vector<unsigned char> fewest((S1 + 1) * (S2 + 1), NONE);
    auto at = [](int s1, int s2) { return s1 * (S2 + 1) + s2; };
    fewest[0] = 0;
    for (int s1 = 1; s1 <= S1; s1++)
        for (int s2 = 1; s2 <= S2; s2++) {
            int best = NONE;
            for (int d = 1; d <= TOP && d <= s1 && d * d <= s2; d++)
                if (fewest[at(s1 - d, s2 - d * d)] + 1 < best)
                    best = fewest[at(s1 - d, s2 - d * d)] + 1;
            if (best <= LONGEST)
                fewest[at(s1, s2)] = best;
        }
    int t;
    if (scanf("%d", &t) != 1)
        return 0;
    string out;
    while (t--) {
        int s1, s2;
        if (scanf("%d %d", &s1, &s2) != 2)
            return 0;
        if (s1 > S1 || s2 > S2 || fewest[at(s1, s2)] == NONE) {
            out += "No solution\n";
            continue;
        }
        // the smallest digit first that still leaves a way to finish; the
        // digits come out sorted, so each search starts at the last one
        int d = 1;
        for (int left = fewest[at(s1, s2)] - 1; left >= 0; left--) {
            while (d * d > s2 || d > s1 || fewest[at(s1 - d, s2 - d * d)] != left)
                d++;
            out += char('0' + d);
            s1 -= d, s2 -= d * d;
        }
        out += '\n';
    }
    fputs(out.c_str(), stdout);
}
