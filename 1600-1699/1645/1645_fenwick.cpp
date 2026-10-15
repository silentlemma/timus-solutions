#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<int> place(n + 1);  // place[s]: finishing position of skier s
    for (int p = 1; p <= n; p++) {
        int s;
        if (scanf("%d", &s) != 1)
            return 0;
        place[s] = p;
    }
    vector<int> tree(n + 1);  // finishing positions of the skiers who started before
    for (int skier = 1; skier <= n; skier++) {
        int p = place[skier], earlier = 0;  // started and finished before: undecided
        for (int i = p - 1; i > 0; i &= i - 1)
            earlier += tree[i];
        // started later yet finished before: surely faster
        int faster = p - 1 - earlier;
        // started before yet finished later: surely slower, the rest undecided
        printf("%d %d\n", faster + 1, (n - skier) + earlier + 1);
        for (int i = p; i <= n; i += i & -i)
            tree[i]++;
    }
}
