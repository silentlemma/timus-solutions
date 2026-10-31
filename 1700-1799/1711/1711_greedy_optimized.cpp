#include <cstdio>
#include <cstring>

constexpr int MAX_PROBLEMS = 16;
constexpr int CHOICES = 3;
constexpr int MAX_NAME = 20;

int main() {
    int n;
    scanf("%d", &n);
    // there are at most 16 triples of 20 letters, plus a terminator per name.
    char names[MAX_PROBLEMS][CHOICES][MAX_NAME + 1];
    int order[MAX_PROBLEMS];
    const char *chosen[MAX_PROBLEMS];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < CHOICES; j++)
            scanf("%20s", names[i][j]);
    for (int i = 0; i < n; i++)
        scanf("%d", &order[i]);
    const char *last = "";
    for (int i = 0; i < n; i++) {
        const char *best = nullptr;
        for (const char *name : names[order[i] - 1])
            if (strcmp(name, last) > 0 && (best == nullptr || strcmp(name, best) < 0))
                best = name;
        if (best == nullptr) {
            puts("IMPOSSIBLE");
            return 0;
        }
        chosen[i] = last = best;
    }
    for (int i = 0; i < n; i++)
        puts(chosen[i]);
}
