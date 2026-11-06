#include <algorithm>
#include <cstdio>

constexpr int DATE_FIELDS = 3;
constexpr int MONTHS = 12;
constexpr int COMMON_MONTH_LENGTHS[MONTHS] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
constexpr int WEEK = 7;
constexpr int YEAR = 365;
constexpr int LEAP = 4;
constexpr int CENTURY = 100;
constexpr int ERA = 400;
constexpr int CELL = 5;
constexpr int MAX_WEEKS = 6;
constexpr int NAME_SIZE = 3;
constexpr const char *NAMES[] = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"};

int main() {
    int day, month, year;
    if (std::scanf("%d%d%d", &day, &month, &year) != DATE_FIELDS) {
        return 0;
    }
    int lengths[MONTHS];
    std::copy_n(COMMON_MONTH_LENGTHS, MONTHS, lengths);
    if (year % LEAP == 0 && (year % CENTURY != 0 || year % ERA == 0)) {
        ++lengths[1];
    }
    const int past = year - 1;
    int before = YEAR * past + past / LEAP - past / CENTURY + past / ERA;
    for (int i = 0; i < month - 1; ++i) {
        before += lengths[i];
    }
    const int first = before % WEEK;
    const int days = lengths[month - 1];
    const int cols = (first + days + WEEK - 1) / WEEK;
    for (int row = 0; row < WEEK; ++row) {
        char line[NAME_SIZE + MAX_WEEKS * CELL + 1];
        char *out = std::copy_n(NAMES[row], NAME_SIZE, line);
        for (int col = 0; col < cols; ++col) {
            const int current = col * WEEK + row - first + 1;
            const bool selected = current == day;
            const bool last = col + 1 == cols;
            if (current < 1 || current > days) {
                out = std::fill_n(out, CELL - last, ' ');
                continue;
            }
            *out++ = ' ';
            *out++ = selected ? '[' : ' ';
            *out++ = current < 10 ? ' ' : static_cast<char>('0' + current / 10);
            *out++ = static_cast<char>('0' + current % 10);
            if (selected || !last) {
                *out++ = selected ? ']' : ' ';
            }
        }
        *out++ = '\n';
        std::fwrite(line, 1, out - line, stdout);
    }
}
