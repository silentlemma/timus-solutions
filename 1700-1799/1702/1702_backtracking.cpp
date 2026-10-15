#include <algorithm>
#include <cstdio>
#include <unordered_map>
#include <vector>

typedef unsigned long long u64;

const int FLOWS = 12;
const int MINUTES = 10;
const int NIBBLE = 4;  // a need is at most 10 minutes, four bits in the memo key

// the flows each flow crosses or merges with, read off the crossing: 1-3
// come from the south, 4-6 from the east, 7-9 from the north and 10-12 from
// the west, each turning right, going straight on and turning left
const std::vector<std::vector<int>> CROSSES = {
    {9, 11}, {4, 5, 6, 9, 11, 12}, {5, 6, 7, 8, 11, 12}, {2, 12}, {2, 3, 7, 8, 9, 12},
    {2, 3, 8, 9, 10, 11}, {3, 5}, {3, 5, 6, 10, 11, 12}, {1, 2, 5, 6, 11, 12},
    {6, 8}, {1, 2, 3, 6, 8, 9}, {2, 3, 4, 5, 8, 9}};

std::vector<std::vector<int>> sets;
size_t widest = 0;
std::unordered_map<u64, bool> memo;

// whether minutes green phases can serve every flow its need
bool fits(std::vector<int> need, int minutes) {
    int top = std::max_element(need.begin(), need.end()) - need.begin();
    int total = 0;
    u64 key = minutes;
    for (int x : need) {
        total += x;
        key = key << NIBBLE | x;
    }
    if (need[top] > minutes || total > (int)widest * minutes) {
        return false;
    }
    if (total == 0) {
        return true;
    }
    auto it = memo.find(key);
    if (it != memo.end()) {
        return it->second;
    }
    // some minute must open the flow that still needs the most
    bool ok = false;
    for (size_t s = 0; s < sets.size() && !ok; s++) {
        if (std::find(sets[s].begin(), sets[s].end(), top) == sets[s].end()) {
            continue;
        }
        std::vector<int> rest = need;
        for (int i : sets[s]) {
            rest[i] = std::max(rest[i] - 1, 0);
        }
        ok = fits(rest, minutes - 1);
    }
    memo[key] = ok;
    return ok;
}

int main() {
    std::vector<int> cars(FLOWS), speed(FLOWS);
    for (int& x : cars) {
        scanf("%d", &x);
    }
    for (int& x : speed) {
        scanf("%d", &x);
    }
    std::vector<int> conflict(FLOWS, 0);
    for (int flow = 0; flow < FLOWS; flow++) {
        for (int other : CROSSES[flow]) {
            conflict[flow] |= 1 << (other - 1);
        }
    }
    // a minute lets through a set of flows that cross nowhere; it never hurts
    // to open more, so only the maximal such sets matter
    for (int mask = 1; mask < 1 << FLOWS; mask++) {
        bool free = true, maximal = true;
        for (int i = 0; i < FLOWS; i++) {
            bool in = mask >> i & 1, crosses = conflict[i] & mask;
            free = free && !(in && crosses);
            maximal = maximal && (in || crosses);
        }
        if (free && maximal) {
            std::vector<int> flows;
            for (int i = 0; i < FLOWS; i++) {
                if (mask >> i & 1) {
                    flows.push_back(i);
                }
            }
            widest = std::max(widest, flows.size());
            sets.push_back(flows);
        }
    }
    int lo = 0, hi = *std::max_element(cars.begin(), cars.end());
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        std::vector<int> need(FLOWS);
        for (int i = 0; i < FLOWS; i++) {
            need[i] = std::max(0, (cars[i] - mid + speed[i] - 1) / speed[i]);
        }
        if (*std::max_element(need.begin(), need.end()) <= MINUTES && fits(need, MINUTES)) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    printf("%d\n", lo);
}
