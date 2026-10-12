#include <iostream>
#include <set>
#include <string>
#include <vector>

std::set<std::string> readSet(std::istream &in) {
    int count = 0;
    in >> count;
    std::set<std::string> items;
    for (int i = 0; i < count; i++) {
        std::string name;
        in >> name;
        items.insert(name);
    }
    return items;
}

int main() {
    std::set<std::string> menu = readSet(std::cin);
    int k = 0, m = 0;
    std::cin >> k;
    std::vector<std::set<std::string>> blocks;
    for (int i = 0; i <= k; i++)
        blocks.push_back(readSet(std::cin));
    std::cin >> m;
    // the first student was fine, so the meal is m products of the rest
    std::set<std::string> safe;
    for (const std::string &p : menu) {
        if (!blocks[0].count(p))
            safe.insert(p);
    }
    for (int i = 1; i <= k; i++) {
        int risky = 0;
        for (const std::string &p : safe)
            risky += blocks[i].count(p);
        int harmless = (int)safe.size() - risky;
        if (m == 0 || risky == 0)
            std::cout << "YES\n";
        else if (harmless < m)
            std::cout << "NO\n"; // every possible meal holds a dangerous product
        else
            std::cout << "MAYBE\n";
    }
    return 0;
}
