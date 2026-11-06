#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>

constexpr int MAX_RECORDS = 1000;
constexpr int REMOVED = 6;
constexpr int RENUMBERED = 7;

struct Record {
    std::size_t start;
    bool mandatory;
};

int token_start() {
    int ch = std::getchar();
    while (ch != EOF && ch <= ' ')
        ch = std::getchar();
    return ch;
}

int main() {
    int size;
    if (std::scanf("%d", &size) != 1)
        return 0;
    std::vector<char> names;
    Record records[MAX_RECORDS];
    int count = 0;
    for (int i = 0; i < size; ++i) {
        const auto start = names.size();
        for (int ch = token_start(); ch > ' '; ch = std::getchar())
            names.push_back(static_cast<char>(ch));
        names.push_back('\0');
        const int verdict = token_start();
        for (int ch = std::getchar(); ch > ' '; ch = std::getchar()) {
        }
        int test = 0;
        if (verdict != 'A' && verdict != 'C')
            std::scanf("%d", &test);
        if (verdict == 'A' || test == REMOVED || test == RENUMBERED)
            records[count++] = {start, test == RENUMBERED};
        else
            names.resize(start);
    }
    auto compare = [&](const Record &a, const Record &b) {
        return std::strcmp(names.data() + a.start, names.data() + b.start);
    };
    std::sort(records, records + count,
              [&](const Record &a, const Record &b) { return compare(a, b) < 0; });
    int least = 0, most = 0;
    for (int i = 0; i < count;) {
        bool mandatory = records[i].mandatory;
        int next = i + 1;
        while (next < count && compare(records[i], records[next]) == 0)
            mandatory |= records[next++].mandatory;
        least += mandatory;
        ++most;
        i = next;
    }
    std::printf("%d %d\n", least, most);
}
