#include <cstdio>
#include <cstring>

const int TEAMS = 12;
const int PER_MEDAL = 4;
const int MAX_NAME = 30;
const int MAX_MEDAL = 6;
const int PRIZE = 5;
const char *MEDALS[] = {"gold", "silver", "bronze"};

int main() {
    // names have at most 30 characters and medals at most 6, plus a terminator.
    char teams[TEAMS][MAX_NAME + 1];
    for (int i = 0; i < TEAMS; ++i)
        scanf("%30s", teams[i]);
    int n, best = -1, winners = 0;
    scanf("%d", &n);
    while (n--) {
        int k, right = 0;
        scanf("%d", &k);
        while (k--) {
            char team[MAX_NAME + 1], kind[MAX_MEDAL + 1];
            scanf("%30s : %6s", team, kind);
            for (int i = 0; i < TEAMS; ++i)
                if (strcmp(team, teams[i]) == 0 && strcmp(kind, MEDALS[i / PER_MEDAL]) == 0)
                    ++right;
        }
        if (right > best) {
            best = right;
            winners = 1;
        } else if (right == best)
            ++winners;
    }
    printf("%d\n", PRIZE * winners);
}
