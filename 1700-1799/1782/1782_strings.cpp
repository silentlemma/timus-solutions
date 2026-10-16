#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

const int MOST = 100;
// how many letters may be taken off each end before undoing a doubling
const int EDGE = 5;

struct Plan {
    int cost, front, back;  // front < 0: the letters one by one
};

std::unordered_map<std::string, Plan> best;

// the word whose doubling is core, or an empty string if core is no double
std::string halve(const std::string &core) {
    std::string half;
    for (size_t i = 0; i < core.size(); i += 2) {
        if (core[i] == core[i + 1]) return "";
        half += core[i];
    }
    return half;
}

// the fewest phrases that build s: either all letters one by one, or a few
// letters at each end around the double of a shorter word; a word free of
// these repeats always has that shape with short ends
Plan plan(const std::string &s) {
    auto found = best.find(s);
    if (found != best.end()) return found->second;
    int n = s.size();
    Plan result = {n, -1, 0};
    for (int a = 0; a <= EDGE && a <= n; a++) {
        for (int b = 0; b <= EDGE && a + b <= n; b++) {
            int len = n - a - b;
            if (len < 2 || len % 2) continue;
            std::string half = halve(s.substr(a, len));
            if (half.empty()) continue;
            int cost = a + b + 1 + plan(half).cost;
            if (cost < result.cost) result = {cost, a, b};
        }
    }
    return best[s] = result;
}

void phrases(const std::string &s, std::vector<std::string> &out) {
    Plan p = plan(s);
    if (p.front < 0) {
        for (char c : s) out.push_back(std::string("back ") + c);
        return;
    }
    int n = s.size();
    phrases(halve(s.substr(p.front, n - p.front - p.back)), out);
    out.push_back("double");
    for (int i = p.front - 1; i >= 0; i--) out.push_back(std::string("front ") + s[i]);
    for (int i = n - p.back; i < n; i++) out.push_back(std::string("back ") + s[i]);
}

int main() {
    std::string word;
    std::cin >> word;
    if (plan(word).cost > MOST) {
        std::cout << -1 << "\n";
        return 0;
    }
    std::vector<std::string> out;
    phrases(word, out);
    std::cout << out.size() << "\n";
    for (const std::string &line : out) std::cout << line << "\n";
    return 0;
}
