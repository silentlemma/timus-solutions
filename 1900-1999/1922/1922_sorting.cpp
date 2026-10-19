#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

std::vector<std::vector<int>> reliableTeams(const std::vector<int> &values) {
    int count = static_cast<int>(values.size());
    std::vector<std::pair<int, int>> ordered;
    for (int index = 0; index < count; ++index) {
        ordered.emplace_back(values[index], index + 1);
    }
    std::sort(ordered.begin(), ordered.end());
    std::vector<std::vector<int>> teams;
    std::vector<int> members;
    for (int size = 1; size <= count; ++size) {
        members.push_back(ordered[size - 1].second);
        if (ordered[size - 1].first <= size && (size == count || ordered[size].first > size + 1)) {
            teams.push_back(members);
        }
    }
    return teams;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::cin >> count;
    std::vector<int> values(count);
    for (int &value : values) {
        std::cin >> value;
    }
    auto teams = reliableTeams(values);
    std::cout << teams.size() << '\n';
    for (const auto &team : teams) {
        std::cout << team.size();
        for (int member : team) {
            std::cout << ' ' << member;
        }
        std::cout << '\n';
    }
    return 0;
}
