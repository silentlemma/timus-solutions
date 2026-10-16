#include <algorithm>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>

// times in tenths of a second; starts are 30 seconds apart
const int TENTHS_PER_MINUTE = 600, TENTHS_PER_SECOND = 10, GAP = 300;

int tenths(const std::string &text) {
    size_t colon = text.find(':'), dot = text.find('.');
    return std::stoi(text.substr(0, colon)) * TENTHS_PER_MINUTE +
           std::stoi(text.substr(colon + 1, dot - colon - 1)) * TENTHS_PER_SECOND +
           std::stoi(text.substr(dot + 1));
}

int main() {
    int n;
    if (!(std::cin >> n)) return 0;
    std::vector<std::tuple<int, int, std::string>> finishes;
    for (int i = 0; i < n; i++) {
        std::string name, time;
        std::cin >> name >> time;
        int run = tenths(time);
        finishes.emplace_back(i * GAP + run, run, name);
    }
    std::sort(finishes.begin(), finishes.end());
    // replay the finishes in order; the board changes on every new best run
    std::vector<std::string> leaders;
    int best = -1;
    for (const auto &[at, run, name] : finishes) {
        if (best < 0 || run < best) {
            best = run;
            leaders.push_back(name);
        }
    }
    std::sort(leaders.begin(), leaders.end());
    std::cout << leaders.size() << "\n";
    for (const auto &name : leaders) std::cout << name << "\n";
    return 0;
}
