#include <cstdio>
#include <utility>

constexpr int MOST = 30;
constexpr int LINE_SIZE = 256, VENUE_SIZE = 8;

int main() {
    int tests;
    scanf("%d\n", &tests);
    for (int test = 0; test < tests; ++test) {
        char line[LINE_SIZE], where[VENUE_SIZE];
        int x, y;
        fgets(line, sizeof(line), stdin);
        sscanf(line, "The Machinegunners played %7s game, scored %d goals, and conceded %d goals.",
               where, &x, &y);
        bool home = where[0] == 'h';
        int lowest = -1, highest = -1;
        for (int goals = 0; goals <= MOST; ++goals) {
            auto ours = std::make_pair(x + goals, home ? goals : x);
            // Opponents' zero and thirty goals are the two extreme outcomes.
            if (lowest < 0 && ours >= std::make_pair(y, home ? y : 0))
                lowest = goals;
            if (ours <= std::make_pair(y + MOST, home ? y : MOST))
                highest = goals;
        }
        printf("%d %d\n", lowest, highest);
    }
}
