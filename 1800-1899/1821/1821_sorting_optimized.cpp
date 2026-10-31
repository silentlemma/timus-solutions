#include <algorithm>
#include <cstdio>
#include <cstring>

const int MAX_RACERS = 100, MAX_NAME = 20;
// times in tenths of a second; starts are 30 seconds apart
const int TENTHS_PER_MINUTE = 600, GAP = 300;
struct Finish {
    int at, run;
    char name[MAX_NAME + 1];
};
// the statement limits the race to 100 names of at most 20 letters.
Finish racers[MAX_RACERS];
const char *leaders[MAX_RACERS];
int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    for (int i = 0; i < n; i++) {
        int minutes, seconds, tenth;
        scanf("%20s %d:%d.%d", racers[i].name, &minutes, &seconds, &tenth);
        racers[i].run = minutes * TENTHS_PER_MINUTE + seconds * 10 + tenth;
        racers[i].at = racers[i].run + i * GAP;
    }
    std::sort(racers, racers + n, [](const Finish &a, const Finish &b) { return a.at < b.at; });
    // replay the finishes in order; the board changes on every new best run
    int best = -1, count = 0;
    for (int i = 0; i < n; i++) {
        if (best < 0 || racers[i].run < best) {
            best = racers[i].run;
            leaders[count++] = racers[i].name;
        }
    }
    std::sort(leaders, leaders + count,
              [](const char *a, const char *b) { return strcmp(a, b) < 0; });
    printf("%d\n", count);
    for (int i = 0; i < count; i++)
        puts(leaders[i]);
}
