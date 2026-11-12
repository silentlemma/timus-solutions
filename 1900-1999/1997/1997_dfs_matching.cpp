#include <iostream>
#include <vector>

bool augment(int arrival, const std::vector<std::vector<int>> &choices, std::vector<int> &owner,
             std::vector<bool> &seen) {
    for (int departure : choices[arrival]) {
        if (seen[departure]) {
            continue;
        }
        seen[departure] = true;
        if (owner[departure] == -1 || augment(owner[departure], choices, owner, seen)) {
            owner[departure] = arrival;
            return true;
        }
    }
    return false;
}

int main() {
    int longStay, shortStay, events;
    std::cin >> longStay >> shortStay >> events;
    std::vector<int> arrivals, departures;
    for (int i = 0; i < events; ++i) {
        int time, direction;
        std::cin >> time >> direction;
        (direction == 0 ? arrivals : departures).push_back(time);
    }
    if (arrivals.size() != departures.size()) {
        std::cout << "Liar\n";
        return 0;
    }

    int count = static_cast<int>(arrivals.size());
    std::vector<std::vector<int>> choices(count);
    for (int arrival = 0; arrival < count; ++arrival) {
        for (int departure = 0; departure < count; ++departure) {
            int duration = departures[departure] - arrivals[arrival];
            if (duration > 0 && (duration <= shortStay || duration >= longStay)) {
                choices[arrival].push_back(departure);
            }
        }
    }

    std::vector<int> owner(count, -1);
    for (int arrival = 0; arrival < count; ++arrival) {
        std::vector<bool> seen(count);
        if (!augment(arrival, choices, owner, seen)) {
            std::cout << "Liar\n";
            return 0;
        }
    }

    std::cout << "No reason\n";
    for (int departure = 0; departure < count; ++departure) {
        std::cout << arrivals[owner[departure]] << ' ' << departures[departure] << '\n';
    }
}
