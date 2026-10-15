#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

// two people can team up only if their ranks differ by exactly 2, so half
// the rank changes parity along every pair: the graph is bipartite
const int GAP = 2;
const int SIDES = 2;

struct Person {
    std::string name;
    bool writes, tests;
    int rank;
};

std::vector<std::vector<int>> adj;
std::vector<int> mateLeft, mateRight, dist;

bool layers(int left) {
    std::vector<int> queue;
    for (int u = 0; u < left; u++) {
        dist[u] = mateLeft[u] < 0 ? 0 : -1;
        if (mateLeft[u] < 0) queue.push_back(u);
    }
    bool found = false;
    for (size_t h = 0; h < queue.size(); h++) {
        int u = queue[h];
        for (int v : adj[u]) {
            int w = mateRight[v];
            if (w < 0) {
                found = true;
            } else if (dist[w] < 0) {
                dist[w] = dist[u] + 1;
                queue.push_back(w);
            }
        }
    }
    return found;
}

bool augment(int u) {
    for (int v : adj[u]) {
        int w = mateRight[v];
        if (w < 0 || (dist[w] == dist[u] + 1 && augment(w))) {
            mateLeft[u] = v;
            mateRight[v] = u;
            return true;
        }
    }
    dist[u] = -1;
    return false;
}

int main() {
    std::ios::sync_with_stdio(false);
    int n;
    if (!(std::cin >> n)) return 0;
    std::vector<Person> people(n);
    std::vector<int> side[SIDES];
    for (int i = 0; i < n; i++) {
        std::string k;
        std::cin >> people[i].name >> k >> people[i].rank;
        people[i].writes = k != "testdata";
        people[i].tests = k != "statements";
        side[people[i].rank / GAP % SIDES].push_back(i);
    }
    const std::vector<int> &left = side[0], &right = side[1];
    adj.assign(left.size(), {});
    for (size_t i = 0; i < left.size(); i++) {
        const Person &a = people[left[i]];
        for (size_t j = 0; j < right.size(); j++) {
            const Person &b = people[right[j]];
            bool close = a.rank - b.rank == GAP || b.rank - a.rank == GAP;
            if (close && ((a.writes && b.tests) || (b.writes && a.tests))) {
                adj[i].push_back(j);
            }
        }
    }
    mateLeft.assign(left.size(), -1);
    mateRight.assign(right.size(), -1);
    dist.assign(left.size(), -1);
    int total = 0;
    while (layers(left.size())) {
        for (size_t u = 0; u < left.size(); u++) {
            if (mateLeft[u] < 0 && augment(u)) total++;
        }
    }
    printf("%d\n", total);
    for (size_t u = 0; u < left.size(); u++) {
        if (mateLeft[u] < 0) continue;
        const Person &a = people[left[u]], &b = people[right[mateLeft[u]]];
        if (a.writes && b.tests) {
            printf("%s %s\n", a.name.c_str(), b.name.c_str());
        } else {
            printf("%s %s\n", b.name.c_str(), a.name.c_str());
        }
    }
}
