#include <algorithm>
#include <cstdio>
#include <cstring>

const int WEEK = 7;
const int MONTHS = 4;
const int WORD = 16;
const int INPUT_FIELDS = 5;
const char *const DAYS[WEEK] = {"Monday", "Tuesday",  "Wednesday", "Thursday",
                                "Friday", "Saturday", "Sunday"};
const char *const NAMES[MONTHS] = {"September", "October", "November", "December"};
// Days elapsed from September 1 through the preceding month.
const int MONTH_START[MONTHS] = {0, 30, 61, 91};

int main() {
    char weekday[WORD], month[WORD];
    int date, minimum, maximum;
    if (scanf("%15s %15s %d %d %d", weekday, month, &date, &minimum, &maximum) != INPUT_FIELDS)
        return 0;
    int start = 0;
    while (strcmp(DAYS[start], weekday) != 0)
        ++start;
    int period = 0;
    while (strcmp(NAMES[period], month) != 0)
        ++period;
    int days = MONTH_START[period] + date - 2;
    int regular = days / WEEK, extra = days % WEEK;
    // The first extra weekdays occur once more than all the others.
    for (int count = 1; count <= WEEK; ++count) {
        int low = std::max(count - (WEEK - extra), minimum - count * regular);
        int high = std::min(count, std::min(extra, maximum - count * regular));
        int heavy = std::max(0, low);
        if (heavy > high)
            continue;
        printf("%d\n", count);
        for (int i = 0; i < heavy; ++i)
            puts(DAYS[(start + 1 + i) % WEEK]);
        for (int i = 0; i < count - heavy; ++i)
            puts(DAYS[(start + 1 + extra + i) % WEEK]);
        return 0;
    }
    puts("Impossible");
}
