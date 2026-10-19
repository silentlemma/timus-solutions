#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

constexpr int HEALTHY = 3;
constexpr int TEAM_SIZE = 4;
constexpr int TRIPLE_SIZE = TEAM_SIZE - 1;

class DisjointSets {
    std::vector<int> parent;

  public:
    explicit DisjointSets(int count) : parent(count) {
        for (int i = 0; i < count; ++i) {
            parent[i] = i;
        }
    }

    int find(int player) {
        while (parent[player] != player) {
            parent[player] = parent[parent[player]];
            player = parent[player];
        }
        return player;
    }

    void unite(int first, int second) {
        first = find(first);
        second = find(second);
        if (first > second) {
            std::swap(first, second);
        }
        parent[second] = first;
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count;
    if (!(std::cin >> count)) {
        return 0;
    }
    std::vector<std::string> names(count);
    std::unordered_map<std::string, int> index;
    for (int i = 0; i < count; ++i) {
        std::cin >> names[i];
        index[names[i]] = i;
    }
    DisjointSets sets(count);
    std::vector<int> health(count, HEALTHY);
    int events;
    std::cin >> events;
    for (int i = 0; i < events; ++i) {
        std::string actorName, action, targetName;
        std::cin >> actorName >> action >> targetName;
        int actor = index.at(actorName);
        if (health[actor] < 2) {
            std::cout << "FAKE\n";
            return 0;
        }
        if (action == "USES") {
            health[actor] = HEALTHY;
            continue;
        }
        int target = index.at(targetName);
        if (action == "HIT") {
            std::string preposition, location;
            std::cin >> preposition >> location;
            int damage = location == "HEAD" ? 2 : 1;
            health[target] = std::max(0, health[target] - damage);
        } else {
            if (health[target] != 1) {
                std::cout << "FAKE\n";
                return 0;
            }
            health[target] = 2;
            sets.unite(actor, target);
        }
    }

    std::vector<std::vector<int>> groups(count);
    for (int i = 0; i < count; ++i) {
        groups[sets.find(i)].push_back(i);
    }
    std::array<std::vector<std::vector<int>>, TEAM_SIZE + 1> buckets;
    for (const auto &group : groups) {
        if (group.size() > TEAM_SIZE) {
            std::cout << "FAKE\n";
            return 0;
        }
        if (!group.empty()) {
            buckets[group.size()].push_back(group);
        }
    }
    if (buckets[1].size() < buckets[TRIPLE_SIZE].size()) {
        std::cout << "FAKE\n";
        return 0;
    }

    std::vector<std::vector<int>> teams = buckets[TEAM_SIZE];
    std::size_t single = 0;
    for (auto group : buckets[TRIPLE_SIZE]) {
        group.push_back(buckets[1][single++][0]);
        teams.push_back(group);
    }
    std::size_t pair = 0;
    while (pair + 1 < buckets[2].size()) {
        auto group = buckets[2][pair++];
        const auto &other = buckets[2][pair++];
        group.insert(group.end(), other.begin(), other.end());
        teams.push_back(group);
    }
    if (pair < buckets[2].size()) {
        auto group = buckets[2][pair];
        group.push_back(buckets[1][single++][0]);
        group.push_back(buckets[1][single++][0]);
        teams.push_back(group);
    }
    // After filling triples, divisibility by the team size guarantees enough singles.
    while (single < buckets[1].size()) {
        std::vector<int> group;
        for (int i = 0; i < TEAM_SIZE; ++i) {
            group.push_back(buckets[1][single++][0]);
        }
        teams.push_back(group);
    }
    std::cout << "CORRECT\n";
    for (const auto &team : teams) {
        for (int i = 0; i < TEAM_SIZE; ++i) {
            if (i != 0) {
                std::cout << ' ';
            }
            std::cout << names[team[i]];
        }
        std::cout << '\n';
    }
}
