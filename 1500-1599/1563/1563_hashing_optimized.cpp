#include <cstdio>
#include <string>
#include <unordered_set>

int main() {
    constexpr int MAX_NAME = 30;
    // each name, at most 30 characters, is read with getchar into a fixed buffer
    char name[MAX_NAME + 1];
    int count;
    std::scanf("%d", &count);
    int ch;
    while ((ch = std::getchar()) != '\n' && ch != EOF) {
    }
    std::unordered_set<std::string> seen;
    // the set is sized for all names at once, so it never rehashes
    seen.reserve(count);
    int repeats = 0;
    for (int i = 0; i < count; ++i) {
        // a name is the whole line, spaces included; only the line end goes
        int length = 0;
        while ((ch = std::getchar()) != '\n' && ch != EOF) {
            if (ch != '\r')
                name[length++] = static_cast<char>(ch);
        }
        // the set compares whole names, spaces included, even on equal hashes
        if (!seen.emplace(name, length).second)
            ++repeats;
    }
    std::printf("%d\n", repeats);
}
