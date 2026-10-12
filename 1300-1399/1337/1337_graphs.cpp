#include <algorithm>
#include <cstdio>
#include <map>
#include <utility>
#include <vector>
using namespace std;

const int INF = 1 << 30;
const int WORD = 64; // documents per word of a set

vector<int> listed() {
    vector<int> items;
    int value = 0;
    while (scanf("%d", &value) == 1 && value != 0)
        items.push_back(value);
    return items;
}

int m, week;
vector<int> off, tail, topo;
vector<vector<int>> pre, succ;
vector<int> waiting;
vector<bool> done;
int bestDay;
vector<int> bestPlan, path;
map<pair<unsigned long long, unsigned long long>, int> seen;

// the first day from t on when the official of v receives
int firstDay(int t, int v) { return t + ((off[v] - t) % week + week) % week; }

// no plan from day t on can fetch the last document earlier
int lowerBound(int t) {
    vector<int> earliest(m, 0);
    vector<vector<pair<int, int>>> bySlot(week);
    for (int v : topo) {
        if (done[v])
            continue;
        int base = t;
        for (int p : pre[v])
            if (!done[p])
                base = max(base, earliest[p] + 1);
        earliest[v] = firstDay(base, v);
        bySlot[off[v]].push_back({earliest[v], tail[v]});
    }
    // k documents of one reception day that cannot come before day r
    // take k such days from r on, and the last still has a tail ahead
    int bound = 0;
    for (auto &here : bySlot) {
        sort(here.rbegin(), here.rend());
        int count = 0, shortest = INF;
        for (auto [first, after] : here) {
            count++;
            shortest = min(shortest, after);
            bound = max(bound, first + (count - 1) * week + shortest);
        }
    }
    return bound;
}

// the first day with a document to fetch, and those documents
int choices(int t, const vector<int> &wait, const vector<bool> &taken, vector<int> &cands) {
    int day = INF;
    cands.clear();
    for (int v = 0; v < m; v++) {
        if (taken[v] || wait[v] != 0)
            continue;
        int d = firstDay(t, v);
        if (d < day) {
            day = d;
            cands.clear();
        }
        if (d == day)
            cands.push_back(v);
    }
    sort(cands.begin(), cands.end(),
         [](int a, int b) { return tail[a] != tail[b] ? tail[a] > tail[b] : a < b; });
    return day;
}

// fetch the document with the longest chain behind it each time
int greedy(int t, int count, vector<int> &plan) {
    vector<int> wait = waiting, cands;
    vector<bool> taken = done;
    int last = t - 1;
    plan.clear();
    for (int i = 0; i < count; i++) {
        last = choices(t, wait, taken, cands);
        int v = cands[0];
        taken[v] = true;
        plan.push_back(v);
        for (int u : succ[v])
            wait[u]--;
        t = last + 1;
    }
    return last;
}

void search(int t, pair<unsigned long long, unsigned long long> mask, int count) {
    if (count == 0) {
        if (t - 1 < bestDay) {
            bestDay = t - 1;
            bestPlan = path;
        }
        return;
    }
    // the same documents in hand by an earlier day were already tried
    auto it = seen.find(mask);
    if (it != seen.end() && it->second <= t)
        return;
    seen[mask] = t;
    if (lowerBound(t) >= bestDay)
        return;
    // fetching nothing on a day when something can be fetched never helps
    vector<int> cands, rest;
    int day = choices(t, waiting, done, cands);
    for (int v : cands) {
        done[v] = true;
        for (int u : succ[v])
            waiting[u]--;
        path.push_back(v);
        int last = greedy(day + 1, count - 1, rest);
        if (last < bestDay) {
            bestDay = last;
            bestPlan = path;
            bestPlan.insert(bestPlan.end(), rest.begin(), rest.end());
        }
        if (day < bestDay) {
            auto next = mask;
            if (v < WORD)
                next.first |= 1ULL << v;
            else
                next.second |= 1ULL << (v - WORD);
            search(day + 1, next, count - 1);
        }
        path.pop_back();
        for (int u : succ[v])
            waiting[u]++;
        done[v] = false;
    }
}

int main() {
    int n = 0;
    if (scanf("%d %d", &n, &week) != 2)
        return 0;
    vector<int> dayOf(n + 1);
    for (int i = 1; i <= n; i++)
        if (scanf("%d", &dayOf[i]) != 1)
            return 0;
    vector<vector<int>> needs(n + 1);
    for (int i = 1; i <= n; i++)
        needs[i] = listed();
    int today = 0;
    if (scanf("%d", &today) != 1)
        return 0;
    vector<bool> held(n + 1, false), todo(n + 1, false);
    for (int d : listed())
        held[d] = true;
    // every document still to get: the wanted ones and, behind them, the
    // papers they need, stopping at papers already held
    vector<int> stack;
    for (int d : listed())
        if (!held[d])
            stack.push_back(d);
    while (!stack.empty()) {
        int doc = stack.back();
        stack.pop_back();
        if (todo[doc])
            continue;
        todo[doc] = true;
        for (int p : needs[doc])
            if (!held[p])
                stack.push_back(p);
    }
    vector<int> docs, index(n + 1, -1);
    for (int d = 1; d <= n; d++)
        if (todo[d]) {
            index[d] = docs.size();
            docs.push_back(d);
        }
    m = docs.size();
    pre.assign(m, {});
    succ.assign(m, {});
    off.assign(m, 0);
    for (int v = 0; v < m; v++) {
        for (int p : needs[docs[v]])
            if (todo[p]) {
                pre[v].push_back(index[p]);
                succ[index[p]].push_back(v);
            }
        // day t (today is day 0) belongs to an official when t = off mod week
        off[v] = ((dayOf[docs[v]] - today) % week + week) % week;
    }
    // a cycle among them makes the set impossible to get
    waiting.assign(m, 0);
    for (int v = 0; v < m; v++)
        waiting[v] = pre[v].size();
    vector<int> left = waiting;
    for (int v = 0; v < m; v++)
        if (left[v] == 0)
            topo.push_back(v);
    for (size_t i = 0; i < topo.size(); i++)
        for (int u : succ[topo[i]])
            if (--left[u] == 0)
                topo.push_back(u);
    if ((int)topo.size() < m) {
        printf("No Solution\n");
        return 0;
    }
    // tail[v]: days that must pass after v is fetched, along its longest chain
    tail.assign(m, 0);
    for (int i = m - 1; i >= 0; i--) {
        int v = topo[i];
        for (int u : succ[v]) {
            int gap = ((off[u] - off[v]) % week + week) % week;
            if (gap == 0)
                gap = week;
            tail[v] = max(tail[v], gap + tail[u]);
        }
    }
    done.assign(m, false);
    if (m == 0) {
        printf("0\n\n");
        return 0;
    }
    bestDay = greedy(0, m, bestPlan);
    search(0, {0, 0}, m);
    printf("%d\n", bestDay);
    for (size_t i = 0; i < bestPlan.size(); i++)
        printf(i ? " %d" : "%d", docs[bestPlan[i]]);
    printf("\n");
}
