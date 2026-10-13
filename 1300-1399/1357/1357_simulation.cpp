#include <cstdio>
#include <deque>
#include <vector>

typedef long long ll;

const ll SPECIFIC_HEAT = 4190; // J/(kg K)
const ll PORTION_GRAMS = 200;
const ll COLD = 20, BOILING = 100; // degrees
const ll POWER = 400;              // W

// heating one portion takes C m dT / P seconds; with m in grams this is
// exactly the number of milliseconds, 167 600
const ll PORTION_MS = SPECIFIC_HEAT * PORTION_GRAMS * (BOILING - COLD) / POWER;
const size_t CAPACITY = 5; // portions in a full teakettle
const ll MS = 1000;
const int TIME_FIELDS = 3; // hours, minutes and seconds
const ll MINUTE = 60, HOUR = MINUTE * MINUTE, DAY = 24 * HOUR;

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<ll> wake(n), ready(n, 0);
    for (int i = 0; i < n; i++) {
        int h = 0, m = 0, s = 0;
        if (scanf("%d:%d:%d", &h, &m, &s) != TIME_FIELDS)
            return 0;
        wake[i] = (h * HOUR + m * MINUTE + s) * MS;
    }
    std::vector<int> kettle;
    std::deque<int> waiting;
    ll boil = 0; // the moment the water in the kettle boils, in milliseconds
    int i = 0;
    while (i < n || !kettle.empty()) {
        // water that boils exactly when someone wakes up is poured out first
        if (!kettle.empty() && (i == n || wake[i] >= boil)) {
            for (int j : kettle)
                ready[j] = boil;
            kettle.clear();
            while (!waiting.empty() && kettle.size() < CAPACITY) {
                kettle.push_back(waiting.front());
                waiting.pop_front();
            }
            boil += PORTION_MS * (ll)kettle.size();
            continue;
        }
        if (kettle.empty()) {
            kettle.push_back(i);
            boil = wake[i] + PORTION_MS;
        } else if (kettle.size() < CAPACITY) {
            // the heat still missing grows by one portion's worth
            kettle.push_back(i);
            boil += PORTION_MS;
        } else {
            waiting.push_back(i);
        }
        i++;
    }
    for (int j = 0; j < n; j++) {
        ll sec = (ready[j] + MS - 1) / MS % DAY; // rounded up, past midnight from 00:00:00
        printf("%02lld:%02lld:%02lld\n", sec / HOUR, sec / MINUTE % MINUTE, sec % MINUTE);
    }
    return 0;
}
