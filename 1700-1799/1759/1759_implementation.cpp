#include <cstdio>

const int YEAR = 365, LEAP = 4, CENTURY = 100, LEAP_CENTURY = 400;
const int MARCH = 3, MONTHS = 12;
// the five months from March to July hold 153 days, and so do August to
// December, which makes the days before a month a simple formula
const int SPAN_DAYS = 153, SPAN_MONTHS = 5;

// days from a fixed origin, counting years from March so that the leap
// day comes last
long dayNumber(int d, int m, int y) {
    if (m < MARCH) {
        y--;
        m += MONTHS;
    }
    long leaps = y / LEAP - y / CENTURY + y / LEAP_CENTURY;
    return (long)YEAR * y + leaps + (SPAN_DAYS * (m - MARCH) + 2) / SPAN_MONTHS + d;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    long best = -1;
    int answer = 0;
    for (int i = 1; i <= n; i++) {
        int d1, m1, y1, d2, m2, y2, d3, m3, y3;
        scanf("%d.%d.%d %d.%d.%d %d.%d.%d", &d1, &m1, &y1, &d2, &m2, &y2, &d3, &m3, &y3);
        long life = dayNumber(d3, m3, y3) - dayNumber(d1, m1, y1) + 1;
        // the list goes in order of death, so the first record holder died first
        if (life > best) {
            best = life;
            answer = i;
        }
    }
    printf("%d\n", answer);
    return 0;
}
