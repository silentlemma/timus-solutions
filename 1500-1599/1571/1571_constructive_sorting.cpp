#include <algorithm>
#include <cstdio>
#include <cstring>

constexpr int MAX_TEAMS = 100, NAME_CAPACITY = 11, ALPHABET = 26;
constexpr int SHORT_NAMES = ALPHABET + ALPHABET * ALPHABET;
struct Name {
    char text[NAME_CAPACITY];
};
Name names[MAX_TEAMS];
bool occupied[SHORT_NAMES];

int short_id(const char *name) {
    if (name[1] == 0)
        return name[0] - 'a';
    if (name[2] == 0)
        return ALPHABET + (name[0] - 'a') * ALPHABET + name[1] - 'a';
    return -1;
}

int main() {
    int n;
    if (std::scanf("%d", &n) != 1)
        return 0;
    for (int i = 0; i < n; ++i)
        std::scanf("%10s", names[i].text);
    std::sort(names, names + n,
              [](const Name &a, const Name &b) { return std::strcmp(a.text, b.text) < 0; });
    bool duplicate = false;
    for (int i = 1; i < n; ++i)
        duplicate |= std::strcmp(names[i - 1].text, names[i].text) == 0;
    if (duplicate || n == 1) {
        std::puts(duplicate && n > 2 ? "Impossible" : "0");
        return 0;
    }
    if (n == 2) {
        std::printf("1\n%s-%s\n", names[0].text, names[1].text);
        return 0;
    }
    for (int i = 0; i < n; ++i) {
        int id = short_id(names[i].text);
        if (id >= 0)
            occupied[id] = true;
    }
    int id = 0;
    while (occupied[id])
        ++id;
    constexpr int HUB_CAPACITY = 3;
    char hub[HUB_CAPACITY] = {};
    if (id < ALPHABET)
        hub[0] = char('a' + id);
    else {
        id -= ALPHABET;
        hub[0] = char('a' + id / ALPHABET);
        hub[1] = char('a' + id % ALPHABET);
    }
    std::printf("%d\n", n);
    for (int i = 0; i < n; ++i)
        std::printf("%s-%s\n", names[i].text, hub);
}
