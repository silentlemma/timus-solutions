#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>

int main() {
    std::ios::sync_with_stdio(false);
    std::string line;
    std::getline(std::cin, line);
    int n = std::stoi(line);
    std::map<std::string, std::set<std::string>> known;
    for (int i = 0; i < n; i++) {
        std::getline(std::cin, line);
        size_t colon = line.find(':');
        std::istringstream words(line.substr(colon + 1));
        std::set<std::string>& associations = known[line.substr(0, colon)];
        for (std::string w; words >> w;) {
            associations.insert(w);
        }
    }
    std::getline(std::cin, line);
    int m = std::stoi(line);
    std::string out;
    for (int i = 0; i < m; i++) {
        std::getline(std::cin, line);
        std::istringstream names(line);
        std::string name;
        names >> name;
        // the common associations are the intersection of the sets
        std::set<std::string> common = known[name];
        while (names >> name) {
            const std::set<std::string>& other = known[name];
            for (auto it = common.begin(); it != common.end();) {
                it = other.count(*it) ? std::next(it) : common.erase(it);
            }
        }
        if (common.empty()) {
            out += "No solution.\n";
            continue;
        }
        std::string joined;
        for (const std::string& w : common) {
            joined += (joined.empty() ? "" : " ") + w;
        }
        out += joined + "\n";
    }
    std::cout << out;
}
