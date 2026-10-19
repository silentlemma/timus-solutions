#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

using namespace std;

// times in units of 1/50 s: a car (20 km/h) covers a metre in 9 units and
// Egor (5 km/h) crosses a 2 m lane in 72
const int METRE = 9;
const int LANE = 72;
const int CAR = 5;
const double UNITS = 50;

int main() {
    vector<pair<int, int>> blocked;
    // a car is on the crossing from METRE d to METRE (d + CAR); a start time
    // s is bad when Egor's time in the car's lane overlaps that
    for (int lane = 0; lane < 2; lane++) {
        int count;
        if (scanf("%d", &count) != 1) return 0;
        for (int i = 0; i < count; i++) {
            int d;
            scanf("%d", &d);
            int enter = lane * LANE;
            blocked.push_back({METRE * d - enter - LANE, METRE * (d + CAR) - enter});
        }
    }
    sort(blocked.begin(), blocked.end());
    int start = 0;
    for (auto [low, high] : blocked) {
        if (low >= start) break;
        start = max(start, high);
    }
    printf("%.6f\n", start / UNITS);
    return 0;
}
