#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

const int CHOICES = 3;  // names offered for every problem

int main() {
    int n;
    std::cin >> n;
    std::vector<std::vector<std::string>> names(n, std::vector<std::string>(CHOICES));
    for (auto& options : names) {
        for (std::string& name : options) {
            std::cin >> name;
        }
        std::sort(options.begin(), options.end());
    }
    // in the given order, the least name above the previous one leaves the
    // most room for the problems still to come
    std::vector<std::string> chosen;
    std::string last;
    for (int i = 0; i < n; i++) {
        int p;
        std::cin >> p;
        const std::vector<std::string>& options = names[p - 1];
        auto it = std::upper_bound(options.begin(), options.end(), last);
        if (it == options.end()) {
            std::cout << "IMPOSSIBLE\n";
            return 0;
        }
        last = *it;
        chosen.push_back(last);
    }
    for (const std::string& name : chosen) {
        std::cout << name << "\n";
    }
}
