#include <algorithm>
#include <cstdio>
#include <string>

const char *NAMES[] = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"};
const int LENGTHS[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
const int MONTHS = 12, WEEK = 7, YEAR = 365, CELL = 5, WIDE = 16;
const int LEAP = 4, CENTURY = 100, ERA = 400;

int main() {
    int d, m, y, lengths[MONTHS];
    scanf("%d %d %d", &d, &m, &y);
    std::copy(LENGTHS, LENGTHS + MONTHS, lengths);
    if (y % LEAP == 0 && (y % CENTURY != 0 || y % ERA == 0)) {
        lengths[1]++;
    }
    // days from 1 January of year 1, a Monday, to the first of the month
    int past = y - 1;
    int before = YEAR * past + past / LEAP - past / CENTURY + past / ERA;
    for (int i = 0; i < m - 1; i++) {
        before += lengths[i];
    }
    int first = before % WEEK, days = lengths[m - 1];
    int cols = (first + days + WEEK - 1) / WEEK;
    for (int row = 0; row < WEEK; row++) {
        std::string line = NAMES[row];
        char cell[WIDE];
        for (int col = 0; col < cols; col++) {
            int day = col * WEEK + row - first + 1;
            bool last = col == cols - 1;
            // every column is five characters wide, the last one four,
            // unless the bracketed date sits in it
            if (day == d) {
                snprintf(cell, sizeof cell, " [%2d]", day);
            } else if (day >= 1 && day <= days) {
                snprintf(cell, sizeof cell, last ? "  %2d" : "  %2d ", day);
            } else {
                snprintf(cell, sizeof cell, "%*s", CELL - last, "");
            }
            line += cell;
        }
        printf("%s\n", line.c_str());
    }
}
