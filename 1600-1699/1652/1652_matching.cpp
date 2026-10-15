#include <algorithm>
#include <cstdio>
#include <map>
#include <numeric>
#include <vector>
using namespace std;

struct Debt {
    int creditor, debtor;
    long long amount;
};

vector<Debt> debts;
vector<int> reach, holder, skipTo;
vector<char> seen;
map<int, vector<int>> own;

int unseen(int j) {
    int root = j;
    while (skipTo[root] != root)
        root = skipTo[root];
    while (skipTo[j] != root) {
        int next = skipTo[j];
        skipTo[j] = root;
        j = next;
    }
    return root;
}

void visit(int j) {
    seen[j] = 1;
    skipTo[j] = j + 1;
}

bool augment(int b) {
    for (int j : own[b])
        if (!seen[j]) {
            visit(j);
            if (holder[j] < 0 || augment(holder[j])) {
                holder[j] = b;
                return true;
            }
        }
    for (int j = unseen(0); j < reach[b]; j = unseen(j + 1))
        if (debts[j].debtor != b) {  // a bank cannot hold its own debt
            visit(j);
            if (holder[j] < 0 || augment(holder[j])) {
                holder[j] = b;
                return true;
            }
        }
    return false;
}

// a maximum matching of banks to debts of their own country: a bank keeps
// a debt it already holds or buys one it can afford
int mostResponsible(const vector<int> &banks, vector<Debt> local, const vector<long long> &money) {
    stable_sort(local.begin(), local.end(),
                [](const Debt &a, const Debt &b) { return a.amount < b.amount; });
    debts = local;
    int nd = debts.size();
    own.clear();
    for (int b : banks)
        own[b];
    for (int j = 0; j < nd; j++)
        if (own.count(debts[j].creditor))
            own[debts[j].creditor].push_back(j);
    reach.assign(money.size(), 0);
    for (int b : banks)  // the affordable prefix
        reach[b] = upper_bound(debts.begin(), debts.end(), money[b],
                               [](long long v, const Debt &d) { return v < d.amount; }) -
                   debts.begin();
    holder.assign(nd, -1);
    seen.assign(nd, 0);
    skipTo.resize(nd + 1);
    iota(skipTo.begin(), skipTo.end(), 0);
    vector<int> order = banks;
    // banks that hold a debt already go first, then the poorer ones
    stable_sort(order.begin(), order.end(), [](int a, int b) {
        if (own[a].empty() != own[b].empty())
            return !own[a].empty();
        return reach[a] < reach[b];
    });
    int count = 0;
    for (int b : order)
        // marks are cleared only after a success: when a search fails the
        // matching stays as it was, so the debts it saw still lead nowhere
        if (augment(b)) {
            count++;
            seen.assign(nd, 0);
            iota(skipTo.begin(), skipTo.end(), 0);
        }
    return count;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<int> country(n);
    vector<long long> money(n);
    map<int, vector<int>> banks;
    for (int b = 0; b < n; b++) {
        if (scanf("%d %lld", &country[b], &money[b]) != 2)
            return 0;
        banks[country[b]].push_back(b);
    }
    int m;
    if (scanf("%d", &m) != 1)
        return 0;
    map<int, vector<Debt>> byCountry;
    for (int i = 0; i < m; i++) {
        Debt d;
        if (scanf("%d %d", &d.creditor, &d.debtor) != 2 || scanf("%lld", &d.amount) != 1)
            return 0;
        d.creditor--, d.debtor--;
        byCountry[country[d.debtor]].push_back(d);
    }
    int total = 0;
    for (const auto &[c, group] : banks)
        total += mostResponsible(group, byCountry[c], money);
    printf("%d\n", total);
}
