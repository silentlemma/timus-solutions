#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count, programs;
    std::cin >> count >> programs;
    std::vector<int> value(count + 2), previous(count + 2), learned(count + 2), redo(count + 2);
    int used = 0, entities = 1;
    std::string output;
    for (int step = 0; step < count; ++step) {
        std::string command;
        int entity;
        std::cin >> command >> entity;
        if (command == "learn") {
            int program;
            std::cin >> program;
            ++used;
            value[used] = program;
            previous[used] = learned[entity];
            learned[entity] = used;
            redo[entity] = 0;
        } else if (command == "rollback") {
            const int head = learned[entity];
            ++used;
            value[used] = value[head];
            previous[used] = redo[entity];
            learned[entity] = previous[head];
            redo[entity] = used;
        } else if (command == "relearn") {
            const int head = redo[entity];
            ++used;
            value[used] = value[head];
            previous[used] = learned[entity];
            redo[entity] = previous[head];
            learned[entity] = used;
        } else if (command == "clone") {
            ++entities;
            learned[entities] = learned[entity];
            redo[entities] = redo[entity];
        } else {
            const int head = learned[entity];
            output += head == 0 ? "basic" : std::to_string(value[head]);
            output += '\n';
        }
    }
    std::cout << output;
}
