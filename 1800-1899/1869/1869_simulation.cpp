#include <algorithm>
#include <cstdio>

const int MAX_STATIONS = 100, SEATS = 36;
int east[MAX_STATIONS], west[MAX_STATIONS];

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            int people;
            if (scanf("%d", &people) != 1)
                return 0;
            if (people == 0)
                continue;
            int *load = i < j ? east : west;
            for (int leg = std::min(i, j); leg < std::max(i, j); leg++)
                load[leg] += people;
        }
    int peak = 0;
    for (int leg = 0; leg < n - 1; leg++)
        peak = std::max({peak, east[leg], west[leg]});
    printf("%d\n", (peak + SEATS - 1) / SEATS);
}
