#include <iostream>
#include <set>
#include <string>

int main() {
    std::string first, line;
    std::cin >> first;
    std::set<std::string> names = {first};
    while (std::cin >> line && line != "#") {
        size_t dash = line.find('-');
        names.insert(line.substr(0, dash));
        names.insert(line.substr(dash + 1));
    }
    // every other compartment must be emptied through one opened partition,
    // and the partitions of a tree towards the airlock are enough
    std::cout << names.size() - 1 << "\n";
}
