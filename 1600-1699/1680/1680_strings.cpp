#include <cctype>
#include <iostream>
#include <set>
#include <sstream>
#include <string>

std::string trim(const std::string& s) {
    size_t from = s.find_first_not_of(" \r\t");
    if (from == std::string::npos) {
        return "";
    }
    return s.substr(from, s.find_last_not_of(" \r\t") - from + 1);
}

int main() {
    std::string line;
    std::getline(std::cin, line);
    int year, n;
    size_t q;
    std::istringstream(line) >> year >> n >> q;
    std::set<std::string> taken;
    for (int i = 0; i < n && std::getline(std::cin, line); i++) {
        std::string team = trim(line);
        // the university is everything before " #k"; names differing only
        // in letter case are the same university
        size_t hash = team.rfind('#');
        std::string university = trim(hash == std::string::npos ? team : team.substr(0, hash));
        for (char& c : university) {
            c = std::tolower(static_cast<unsigned char>(c));
        }
        if (taken.count(university)) {
            continue;
        }
        if (taken.size() == q) {
            std::cout << team << "\n";
            return 0;
        }
        taken.insert(university);
    }
}
