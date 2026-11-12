#include <cstdio>
#include <cstring>
#include <string>
#include <unordered_set>

const char *LYOSHA = "Efremov";
const char *VADIK = "Kantorov";
const int FULL_TEAM = 3;
const int NAME_LIMIT = 50;

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::unordered_set<std::string> full, pairs;
    for (int i = 0; i < n; ++i) {
        int size = 0;
        scanf("%d", &size);
        for (int j = 0; j < size; ++j) {
            char name[NAME_LIMIT + 1];
            scanf("%50s", name);
            if (std::strcmp(name, LYOSHA) && std::strcmp(name, VADIK)) {
                if (size == FULL_TEAM)
                    full.insert(name);
                else
                    pairs.insert(name);
            }
        }
    }
    int lyosha = 0, vadik = 0, m = 0;
    scanf("%d %d %d", &lyosha, &vadik, &m);
    int best = -1;
    std::string chosen;
    for (int i = 0; i < m; ++i) {
        char name[NAME_LIMIT + 1];
        int rating = 0;
        scanf("%50s %d", name, &rating);
        int strength = vadik + rating;
        if (!full.count(name))
            strength += lyosha;
        else if (pairs.count(name))
            continue;
        if (strength > best) {
            best = strength;
            chosen = name;
        }
    }
    if (best < 0)
        puts("Fail");
    else
        printf("Win\n%s\n", chosen.c_str());
}
