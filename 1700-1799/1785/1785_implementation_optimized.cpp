#include <cstdio>

constexpr int LEGION_MIN = 1000;
constexpr int ZOUNDS_MIN = 500;
constexpr int SWARM_MIN = 250;
constexpr int THRONG_MIN = 100;
constexpr int HORDE_MIN = 50;
constexpr int LOTS_MIN = 20;
constexpr int SEVERAL_MIN = 5;
// the smallest number for each word, from the largest down
constexpr int FROM[] = {LEGION_MIN, ZOUNDS_MIN, SWARM_MIN,   THRONG_MIN, HORDE_MIN,
                        LOTS_MIN,   10,         SEVERAL_MIN, 1};
const char *const WORDS[] = {"legion", "zounds", "swarm",   "throng", "horde",
                             "lots",   "pack",   "several", "few"};

// scanf and puts instead of iostream
int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    int i = 0;
    while (n < FROM[i])
        ++i;
    puts(WORDS[i]);
    return 0;
}
