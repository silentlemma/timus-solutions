#include <cstdio>
#include <tuple>
#include <vector>

const int MINUTES = 60, FIRST_HOUR = 7, WITH_LEONID = 13, ALREADY_IN = 42;

int n, m;
std::vector<std::vector<int>> order, place;
std::vector<std::pair<int, int>> buses;
int chosenStart, chosen;

// whether a passenger waiting at src for dst takes the chosen bus: no bus
// seen by Leonid serves the trip and comes to src sooner, or at the same
// minute reaching dst sooner, or as soon with a smaller route
bool picked(int src, int dst) {
    const std::vector<int> &here = place[chosen];
    if (here[src] < 0 || here[dst] < 0 || here[src] >= here[dst]) return false;
    auto mine = std::make_tuple(chosenStart + here[src], chosenStart + here[dst], chosen);
    for (auto [start, route] : buses) {
        const std::vector<int> &there = place[route];
        if (start < 0 || there[src] < 0 || there[dst] < 0 || there[src] >= there[dst]) continue;
        if (std::make_tuple(start + there[src], start + there[dst], route) < mine) return false;
    }
    return true;
}

int main() {
    if (scanf("%d %d", &n, &m) != 2) return 0;
    order.resize(m);
    place.assign(m, std::vector<int>(n + 1, -1));
    for (int r = 0; r < m; r++) {
        for (int s; scanf("%d", &s) == 1 && s != -1;) {
            place[r][s] = order[r].size();
            order[r].push_back(s);
        }
    }
    int k;
    scanf("%d", &k);
    for (int i = 0; i < k; i++) {
        int hh, mm, route;
        scanf("%d:%d %d", &hh, &mm, &route);
        route--;
        // the minute this bus left the first stop of its route
        buses.push_back({(hh - FIRST_HOUR) * MINUTES + mm - place[route][1], route});
    }
    chosenStart = buses.back().first;
    chosen = buses.back().second;
    // buses not seen at stop 1 either come to a stop before it later than the
    // chosen bus, or need not run at all
    const std::vector<int> &stops = order[chosen];
    int one = place[chosen][1], two = place[chosen][2], len = stops.size();
    bool leaveNew = false, stayNew = false, leaveOld = false, stayOld = false;
    for (int d = one + 1; d < len; d++) {
        bool early = d < two;
        if (picked(1, stops[d])) (early ? leaveNew : stayNew) = true;
        for (int s = 0; s < one; s++) {
            if (picked(stops[s], stops[d])) (early ? leaveOld : stayOld) = true;
        }
    }
    // each group can all ride to a stop of one kind, so the counts are all or
    // nothing for the 13 who got on with Leonid and the 42 already inside
    int low = WITH_LEONID * !leaveNew + ALREADY_IN * !leaveOld;
    int high = WITH_LEONID * stayNew + ALREADY_IN * stayOld;
    printf("%d %d\n", low, high);
    return 0;
}
