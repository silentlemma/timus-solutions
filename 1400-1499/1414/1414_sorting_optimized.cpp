#include <cstdio>
#include <set>
#include <string>

constexpr int LIMIT = 20, MAX_NAME = 20;

int main() {
    std::set<std::string> names = {"sun"};
    char line[MAX_NAME + 2];
    while (scanf("%21s", line) == 1) {
        std::string argument = line + 1;
        if (line[0] == '+') {
            names.insert(argument);
            continue;
        }
        // Stream each query; retaining all answers would cost megabytes.
        puts(argument.c_str());
        int shown = 0;
        for (auto it = names.lower_bound(argument); it != names.end() && shown < LIMIT; ++it) {
            if (it->compare(0, argument.size(), argument) != 0)
                break;
            printf("  %s\n", it->c_str());
            ++shown;
        }
    }
}
