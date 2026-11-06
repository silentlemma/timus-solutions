#include <iostream>
#include <string>
#include <utility>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count, programs;
    if (!(std::cin >> count >> programs))
        return 0;
    // Each command allocates at most one node or one entity.
    // Nodes grow from the front and entity heads grow from the back.
    const int end = count + 2;
    std::vector<std::pair<int, int>> arena(end);
    int used = 0, entities = 1;
    std::string command;
    for (int step = 0; step < count; ++step) {
        int entity;
        std::cin >> command >> entity;
        auto &heads = arena[end - entity];
        const auto [learned, undone] = heads;
        if (command == "learn") {
            int program;
            std::cin >> program;
            arena[++used] = {program, learned};
            heads = {used, 0};
        } else if (command == "rollback") {
            const auto [program, previous] = arena[learned];
            arena[++used] = {program, undone};
            heads = {previous, used};
        } else if (command == "relearn") {
            const auto [program, previous] = arena[undone];
            arena[++used] = {program, learned};
            heads = {used, previous};
        } else if (command == "clone") {
            arena[end - ++entities] = heads;
        } else if (learned == 0) {
            std::cout << "basic\n";
        } else {
            std::cout << arena[learned].first << '\n';
        }
    }
}
