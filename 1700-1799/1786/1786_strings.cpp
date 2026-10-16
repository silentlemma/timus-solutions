#include <cctype>
#include <iostream>
#include <string>

const std::string NAME = "Sandro";
const int COINS = 5;

int main() {
    std::string text;
    if (!(std::cin >> text)) return 0;
    int best = -1;
    for (size_t start = 0; start + NAME.size() <= text.size(); start++) {
        int cost = 0;
        for (size_t k = 0; k < NAME.size(); k++) {
            char a = text[start + k], b = NAME[k];
            // one fee for the wrong case, one for the wrong letter
            if (!std::isupper(a) != !std::isupper(b)) cost += COINS;
            if (std::tolower(a) != std::tolower(b)) cost += COINS;
        }
        if (best < 0 || cost < best) best = cost;
    }
    std::cout << best << "\n";
    return 0;
}
