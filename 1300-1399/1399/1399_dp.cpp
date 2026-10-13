#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>

using namespace std;

const int ROUNDS = 300000; // large neighbourhood search rounds
const int SHARE = 50;      // the first threshold is the first cost over this
const int MOST = 8;        // at most this many random items removed at once

const int KINDS = 3;          // removal kinds: random items, a whole trip, one client
const int UNREACHED = 0xFFFF; // no path yet in the subset table
const int OBJECTS = 21;       // the depot and up to 20 clients

// xorshift64 from a fixed seed: the same numbers in every language
const uint64_t SEED = 88172645463325252ULL;
const int SHIFT_A = 13, SHIFT_B = 7, SHIFT_C = 17;

int m, n, cap;
int dist[OBJECTS][OBJECTS];
vector<int> weight, client;
vector<uint16_t> path; // path[S * m + j]: shortest walk from the depot through S ending at j
vector<int> tour;      // tour[S]: shortest round trip from the depot through S

uint64_t rngState = SEED;

uint64_t nextRandom() {
    rngState ^= rngState << SHIFT_A;
    rngState ^= rngState >> SHIFT_B;
    rngState ^= rngState << SHIFT_C;
    return rngState;
}

int randomBelow(int k) { return (int)(nextRandom() % (uint64_t)k); }

vector<int> trip, load, clients; // trip of each item; per trip the load and the client set
vector<vector<int>> perClient;   // perClient[t][c]: items of client c in trip t
long long cost = 0;

void put(int i, int t) {
    if (t == (int)load.size()) {
        load.push_back(0);
        clients.push_back(0);
        perClient.push_back(vector<int>(m, 0));
    }
    cost -= tour[clients[t]];
    trip[i] = t;
    load[t] += weight[i];
    if (perClient[t][client[i]]++ == 0)
        clients[t] |= 1 << client[i];
    cost += tour[clients[t]];
}

void take(int i) {
    int t = trip[i];
    cost -= tour[clients[t]];
    load[t] -= weight[i];
    if (--perClient[t][client[i]] == 0)
        clients[t] &= ~(1 << client[i]);
    cost += tour[clients[t]];
    trip[i] = -1;
}

// the cheapest place for item i: an existing trip or a new one, the first
// trip that costs no more than a new one so that emptied trips are reused
void insertBest(int i) {
    int fresh = (int)load.size(), best = fresh, extra = tour[1 << client[i]];
    for (int t = 0; t < (int)load.size(); t++) {
        if (load[t] + weight[i] > cap)
            continue;
        int d = tour[clients[t] | 1 << client[i]] - tour[clients[t]];
        if (d < extra || (d == extra && best == fresh)) {
            extra = d;
            best = t;
        }
    }
    put(i, best);
}

int main() {
    scanf("%d %d %d", &m, &n, &cap);
    for (int i = 0; i <= m; i++)
        for (int j = 0; j <= m; j++)
            scanf("%d", &dist[i][j]);
    weight.resize(n);
    client.resize(n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &weight[i], &client[i]);
        client[i]--;
    }
    // Held-Karp over the clients: shortest walks from the depot through every subset
    int full = 1 << m;
    path.assign((size_t)full * m, UNREACHED);
    tour.assign(full, 0);
    for (int j = 0; j < m; j++)
        path[(size_t)(1 << j) * m + j] = dist[0][j + 1];
    for (int s = 1; s < full; s++) {
        int best = UNREACHED;
        // only the clients in s can end the walk, only the others can come next
        for (int js = s; js; js &= js - 1) {
            int j = __builtin_ctz(js), here = path[(size_t)s * m + j];
            best = min(best, here + dist[j + 1][0]);
            for (int ks = ~s & (full - 1); ks; ks &= ks - 1) {
                int k = __builtin_ctz(ks);
                uint16_t &to = path[(size_t)(s | 1 << k) * m + k];
                to = min<int>(to, here + dist[j + 1][k + 1]);
            }
        }
        tour[s] = best;
    }
    // a first plan by cheapest insertion; then rounds of removing some items
    // and putting them back in the cheapest places, undone when the cost grows
    // by more than a threshold that falls to zero
    trip.assign(n, -1);
    for (int i = 0; i < n; i++)
        insertBest(i);
    vector<int> bestTrip = trip, removed, oldTrip;
    long long bestCost = cost, start = cost;
    for (int round = 0; round < ROUNDS; round++) {
        long long before = cost;
        removed.clear();
        oldTrip.clear();
        int kind = randomBelow(KINDS), count = 1 + randomBelow(min(n, MOST));
        int pick = randomBelow(n), target = kind == 1 ? trip[pick] : client[pick];
        for (int i = 0; i < n; i++) {
            bool chosen = kind == 1 ? trip[i] == target : kind == 2 && client[i] == target;
            if (chosen) {
                removed.push_back(i);
                oldTrip.push_back(trip[i]);
            }
        }
        for (int k = 0; kind == 0 && k < count; k++) {
            int i = randomBelow(n);
            if (find(removed.begin(), removed.end(), i) == removed.end()) {
                removed.push_back(i);
                oldTrip.push_back(trip[i]);
            }
        }
        for (int i : removed)
            take(i);
        for (int k = (int)removed.size() - 1; k > 0; k--) {
            int r = randomBelow(k + 1);
            swap(removed[k], removed[r]);
            swap(oldTrip[k], oldTrip[r]);
        }
        for (int i : removed)
            insertBest(i);
        long long threshold = start * (ROUNDS - round) / ROUNDS / SHARE;
        if (cost > before + threshold) {
            for (int i : removed)
                take(i);
            for (size_t k = 0; k < removed.size(); k++)
                put(removed[k], oldTrip[k]);
        }
        if (cost < bestCost) {
            bestCost = cost;
            bestTrip = trip;
        }
    }
    // rebuild the best plan and print its non-empty trips, each route
    // recovered from the subset table
    int trips = *max_element(bestTrip.begin(), bestTrip.end()) + 1;
    load.assign(trips, 0);
    clients.assign(trips, 0);
    perClient.assign(trips, vector<int>(m, 0));
    cost = 0;
    for (int i = 0; i < n; i++)
        put(i, bestTrip[i]);
    vector<int> used;
    for (int t = 0; t < trips; t++)
        if (clients[t])
            used.push_back(t);
    printf("%d\n\n", (int)used.size());
    long long total = 0;
    for (int t : used) {
        bool first = true;
        for (int i = 0; i < n; i++)
            if (trip[i] == t) {
                printf(first ? "%d" : " %d", i + 1);
                first = false;
            }
        printf("\n%d\n", load[t]);
        int s = clients[t], length = tour[s], last = -1;
        for (int j = 0; j < m && last < 0; j++)
            if (s >> j & 1 && path[(size_t)s * m + j] + dist[j + 1][0] == length)
                last = j;
        vector<int> route;
        while (s) {
            route.push_back(last + 1);
            int prev = -1, rest = s & ~(1 << last);
            for (int j = 0; j < m && rest && prev < 0; j++)
                if (rest >> j & 1 && path[(size_t)rest * m + j] + dist[j + 1][last + 1] ==
                                         path[(size_t)s * m + last])
                    prev = j;
            s = rest;
            last = prev;
        }
        printf("0");
        for (int k = (int)route.size() - 1; k >= 0; k--)
            printf(" %d", route[k]);
        printf(" 0\n%d\n\n", length);
        total += length;
    }
    printf("%lld\n", total);
}
