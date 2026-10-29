#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>

const std::string CHAMPION = "Isenbaev";
const int TEAM = 3;

int main() {
    int teams;
    if (!(std::cin >> teams))
        return 0;
    std::map<std::string, std::set<std::string>> mates;
    for (int t = 0; t < teams; t++) {
        std::string team[TEAM];
        for (auto &name : team)
            std::cin >> name;
        for (auto &name : team)
            mates[name].insert(team, team + TEAM);
    }
    // breadth-first search from the champion over shared teams
    std::map<std::string, int> number;
    if (mates.count(CHAMPION)) {
        number[CHAMPION] = 0;
        std::queue<std::string> queue;
        queue.push(CHAMPION);
        while (!queue.empty()) {
            std::string name = queue.front();
            queue.pop();
            for (const auto &mate : mates[name]) {
                if (!number.count(mate)) {
                    number[mate] = number[name] + 1;
                    queue.push(mate);
                }
            }
        }
    }
    for (const auto &entry : mates) {
        auto it = number.find(entry.first);
        std::cout << entry.first << " "
                  << (it == number.end() ? "undefined" : std::to_string(it->second)) << "\n";
    }
    return 0;
}
