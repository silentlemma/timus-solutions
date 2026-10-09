#include <cstdio>
#include <cstdlib>

const int HOUR = 60;
const int DAY = 24 * HOUR;
const int LONGEST = 6 * HOUR;
const int SPREAD = 10;
const int MAX_SHIFT = 5;

int clock_minutes() {
    int h = 0, m = 0;
    if (scanf("%d.%d", &h, &m) != 2)
        exit(0);
    return h * HOUR + m;
}

int main() {
    int out1 = clock_minutes(), in1 = clock_minutes();
    int out2 = clock_minutes(), in2 = clock_minutes();
    // when the second airport is k hours ahead, the real durations are the clock
    // differences minus and plus k hours, taken around the day
    for (int k = -MAX_SHIFT; k <= MAX_SHIFT; k++) {
        int t1 = ((in1 - out1 - k * HOUR) % DAY + DAY) % DAY;
        int t2 = ((in2 - out2 + k * HOUR) % DAY + DAY) % DAY;
        if (t1 <= LONGEST && t2 <= LONGEST && std::abs(t1 - t2) <= SPREAD) {
            printf("%d\n", std::abs(k));
            return 0;
        }
    }
}
