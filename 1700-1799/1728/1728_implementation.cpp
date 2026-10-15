#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>

const std::string LYOSHA = "Efremov";
const std::string VADIK = "Kantorov";

std::vector<std::string> team(std::vector<std::string> names) {
    std::sort(names.begin(), names.end());
    return names;
}

int main() {
    std::ios::sync_with_stdio(false);
    int n;
    std::cin >> n;
    std::set<std::vector<std::string>> played;
    for (int i = 0; i < n; i++) {
        int size;
        std::cin >> size;
        std::vector<std::string> names(size);
        for (auto &name : names) std::cin >> name;
        played.insert(team(names));
    }
    int lyosha, vadik, m;
    std::cin >> lyosha >> vadik >> m;
    int best = -1;
    std::string chosen;
    for (int i = 0; i < m; i++) {
        std::string name;
        int rating, strength;
        std::cin >> name >> rating;
        // Lyosha stays away from a team that has played before, and the
        // pair left over must then be new, or the team is out
        if (!played.count(team({LYOSHA, VADIK, name}))) {
            strength = lyosha + vadik + rating;
        } else if (!played.count(team({VADIK, name}))) {
            strength = vadik + rating;
        } else {
            continue;
        }
        if (strength > best) {
            best = strength;
            chosen = name;
        }
    }
    if (best < 0) {
        std::cout << "Fail\n";
    } else {
        std::cout << "Win\n" << chosen << "\n";
    }
}
