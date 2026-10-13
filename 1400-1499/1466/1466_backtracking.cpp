#include <algorithm>
#include <array>
#include <cstdio>
#include <map>
#include <numeric>
#include <set>
#include <vector>

using namespace std;

const int FIELDS = 3; // a given cell: its column, its row and its number

typedef vector<int> Perm;
typedef pair<Perm, Perm> Slot; // pi and sigma of one number

int n;
vector<Slot> slots, chosen;
vector<vector<Slot>> found;
vector<vector<set<pair<int, int>>>> used;

// The square survives block swaps exactly when each number v sits in row pi_v(J) of
// every block in column J and column sigma_v(I) of every block in row I, and each pair
// (I, J) meets all positions (pi_v(J), sigma_v(I)) once; such sets are searched.
void grow(size_t start) {
    if ((int)chosen.size() == n * n) {
        found.push_back(chosen);
        return;
    }
    for (size_t k = start; k < slots.size(); k++) {
        const Perm &x = slots[k].first, &y = slots[k].second;
        bool free = true;
        for (int i = 0; i < n && free; i++)
            for (int j = 0; j < n && free; j++)
                free = !used[i][j].count({x[j], y[i]});
        if (!free)
            continue;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                used[i][j].insert({x[j], y[i]});
        chosen.push_back(slots[k]);
        grow(k + 1);
        chosen.pop_back();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                used[i][j].erase({x[j], y[i]});
    }
}

int main() {
    int k;
    scanf("%d %d", &n, &k);
    vector<array<int, FIELDS>> given = {{0, 0, 0}}; // the corner holds 0
    for (int i = 0; i < k; i++) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        given.push_back({a, b, c});
    }
    Perm p(n);
    iota(p.begin(), p.end(), 0);
    vector<Perm> perms;
    do
        perms.push_back(p);
    while (next_permutation(p.begin(), p.end()));
    for (auto &x : perms)
        for (auto &y : perms)
            slots.push_back({x, y});
    used.assign(n, vector<set<pair<int, int>>>(n));
    grow(0);
    for (auto &structure : found) {
        // each given cell pins its number to the one slot that lands there
        map<int, int> slotOf, numberOf;
        bool fine = true;
        for (auto &g : given) {
            int j = g[0] / n, c = g[0] % n, i = g[1] / n, r = g[1] % n, v = g[2];
            int s = 0;
            while (structure[s].first[j] != r || structure[s].second[i] != c)
                s++;
            if ((slotOf.count(v) && slotOf[v] != s) || (numberOf.count(s) && numberOf[s] != v)) {
                fine = false;
                break;
            }
            slotOf[v] = s;
            numberOf[s] = v;
        }
        if (fine) {
            puts("YES");
            return 0;
        }
    }
    puts("NO");
}
