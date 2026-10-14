#include <bitset>
#include <cstdio>
#include <vector>
using namespace std;

const int MAXN = 100;

int n;
bitset<MAXN> heavier[MAXN]; // bit j of heavier[i]: hobbit i is known to outweigh j
int matchOf[MAXN];          // the heavier hobbit matched to a lighter one
bool seen[MAXN];

bool augment(int i) {
    for (int j = 0; j < n; j++)
        if (heavier[i][j] && !seen[j]) {
            seen[j] = true;
            if (matchOf[j] < 0 || augment(matchOf[j])) {
                matchOf[j] = i;
                return true;
            }
        }
    return false;
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            int x;
            scanf("%d", &x);
            heavier[i][j] = x == 1;
        }
    // the weighings are consistent, so the closure is a strict order
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            if (heavier[i][k])
                heavier[i] |= heavier[k];
    // by Dilworth, the largest set of incomparable hobbits is n minus a
    // maximum matching between "heavier" copies and "lighter" copies
    vector<bool> matched(n);
    for (int j = 0; j < n; j++)
        matchOf[j] = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            seen[j] = false;
        matched[i] = augment(i);
    }
    // Konig: walk alternating paths from the unmatched heavier copies; the
    // hobbits reached on the heavier side but not on the lighter side form
    // the answer, as everything else is a vertex cover
    vector<bool> left(n), right(n);
    vector<int> stack;
    for (int i = 0; i < n; i++)
        if (!matched[i]) {
            left[i] = true;
            stack.push_back(i);
        }
    while (!stack.empty()) {
        int i = stack.back();
        stack.pop_back();
        for (int j = 0; j < n; j++)
            if (heavier[i][j] && !right[j]) {
                right[j] = true;
                int owner = matchOf[j];
                if (owner >= 0 && !left[owner]) {
                    left[owner] = true;
                    stack.push_back(owner);
                }
            }
    }
    vector<int> chosen;
    for (int i = 0; i < n; i++)
        if (left[i] && !right[i])
            chosen.push_back(i + 1);
    printf("%d\n", (int)chosen.size());
    for (size_t t = 0; t < chosen.size(); t++)
        printf(t ? " %d" : "%d", chosen[t]);
    printf("\n");
}
