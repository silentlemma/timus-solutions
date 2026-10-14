#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const long long BASE_SCORE = 1000000;
enum { PERFECT, GREAT, GOOD, BOO, MISS, MARKS };
const char *NAMES[MARKS] = {"Perfect", "Great", "Good", "Boo", "Miss"};
const long long SCORE[MARKS] = {10, 5, 0, 0, 0};  // p
const long long COMBO[MARKS] = {55, 33, 0, 0, 0}; // q
const int DANCE[MARKS] = {2, 1, 0, -4, -5};       // dance points
const int PERCENT = 100;
// level bonuses: share of the most dance points needed, in percent
const int SHARES[] = {80, 64, 50};
const long long SHARE_BONUS[] = {100000, 10000, 1000};
const long long ALL_PERFECT = 10000000, ALL_GREAT = 1000000, LOW = 100;
const int SLOWEST = 1000; // ms per beat on Easy, halved on each harder level
const int TENTHS = 10;
const int PERFECT_TENTHS = 4; // under 40 % of the period
const int GREAT_TENTHS = 7;   // under 70 %
const string LEVELS[] = {"Easy", "Medium", "Hard"};
const char *SEPARATOR = "--------------------";

int main() {
    string duration, level, beats;
    cin >> duration >> level >> beats;
    int index = find(begin(LEVELS), end(LEVELS), level) - begin(LEVELS);
    int diff = index + 1, period = SLOWEST >> index;
    vector<pair<int, char>> log;
    int t;
    char key;
    while (cin >> t >> key)
        log.push_back({t, key});
    sort(log.begin(), log.end());
    long long steps = count_if(beats.begin(), beats.end(), [](char b) { return b != 'N'; });
    long long unit = diff * BASE_SCORE / (steps * (steps + 1) / 2); // B div S
    long long counts[MARKS] = {}, stage = 0, comboBonus = 0, combo = 0, n = 0;
    int points = 0;
    bool wentNegative = false;
    size_t k = 0; // the first logged press not before the current beat
    for (size_t i = 0; i < beats.size(); i++) {
        int start = i * period, end = start + period;
        while (k < log.size() && log[k].first < start)
            k++;
        if (beats[i] == 'N')
            continue;
        n++;
        // only the first press within the beat counts
        int mark;
        if (k == log.size() || log[k].first >= end)
            mark = BOO;
        else if (log[k].second != beats[i])
            mark = MISS;
        else {
            int elapsed = log[k].first - start;
            mark = TENTHS * elapsed < PERFECT_TENTHS * period ? PERFECT
                   : TENTHS * elapsed < GREAT_TENTHS * period ? GREAT
                                                              : GOOD;
        }
        counts[mark]++;
        stage += SCORE[mark] * n * unit;
        combo = mark <= GOOD ? combo + 1 : 0;
        comboBonus += COMBO[mark] * combo;
        points += DANCE[mark];
        wentNegative = wentNegative || points < 0;
    }
    long long most = DANCE[PERFECT] * steps, bonus = LOW;
    if (wentNegative)
        bonus = 0;
    else if (counts[PERFECT] == steps)
        bonus = ALL_PERFECT;
    else if (counts[PERFECT] + counts[GREAT] == steps)
        bonus = ALL_GREAT;
    else
        for (int i = 2; i >= 0; i--)
            if ((long long)PERCENT * points >= SHARES[i] * most)
                bonus = SHARE_BONUS[i];
    for (int i = 0; i < MARKS; i++)
        printf("%s: %lld\n", NAMES[i], counts[i]);
    printf("%s\n", SEPARATOR);
    printf("Stage Score: %lld\nCombo Bonus: %lld\n", stage, comboBonus);
    printf("Dance Level Bonus: %lld\nTotal Score: %lld\n", bonus, stage + comboBonus + bonus);
}
