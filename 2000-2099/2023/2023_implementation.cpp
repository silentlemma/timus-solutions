#include <cstdlib>
#include <iostream>
#include <map>
#include <string>

const int CABINET_COUNT = 3, NAMES_PER_CABINET = 9;
// the three cabinets from left to right, with the names from the statement
const char *CABINETS[CABINET_COUNT][NAMES_PER_CABINET] = {
    {"Alice", "Ariel", "Aurora", "Phil", "Peter", "Olaf", "Phoebus", "Ralph", "Robin"},
    {"Bambi", "Belle", "Bolt", "Mulan", "Mowgli", "Mickey", "Silver", "Simba", "Stitch"},
    {"Dumbo", "Genie", "Jiminy", "Kuzko", "Kida", "Kenai", "Tarzan", "Tiana", "Winnie"},
};

int main() {
    std::map<std::string, int> cabinet;
    for (int i = 0; i < CABINET_COUNT; i++)
        for (const char *name : CABINETS[i])
            cabinet[name] = i;
    int n, position = 0, steps = 0;
    std::cin >> n;
    for (int k = 0; k < n; k++) {
        std::string name;
        std::cin >> name;
        steps += std::abs(cabinet[name] - position);
        position = cabinet[name];
    }
    std::cout << steps << "\n";
}
