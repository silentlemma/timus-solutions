#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

constexpr int PERCENT = 100;
constexpr long long OUTPUT_SCALE = 1000000000;
constexpr double HALF = 0.5;
constexpr int MIN_DECIMALS = 3;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int seat_count;
    int vacancy_percent;
    std::string seats;
    std::cin >> seat_count >> vacancy_percent >> seats;

    int left = 0;
    int right = 0;
    int occupied_left = 0;
    bool before_own_seat = true;
    for (char seat : seats) {
        if (seat == '2') {
            before_own_seat = false;
        } else if (seat == '0') {
            if (before_own_seat) {
                ++left;
            } else {
                ++right;
            }
        } else if (before_own_seat) {
            ++occupied_left;
        }
    }

    const int empty = left + right;
    std::vector<double> step(empty + 1);
    std::vector<double> expected(empty + 1);
    double arrival = 0;
    double remaining = 0;
    // Observed arrivals update the distribution of the final audience size.
    for (int count = 1; count <= empty; ++count) {
        const double weight = static_cast<double>(count * (PERCENT - vacancy_percent));
        arrival = weight / (weight + static_cast<double>((empty - count + 1) * vacancy_percent) *
                                         (1 - arrival));
        remaining = arrival * (1 + remaining);
        step[count] = arrival / count;
        expected[count] = remaining / count;
    }

    std::vector<double> best(right + 1);
    // The current cell compares sitting now with waiting for the next arrival.
    for (int l = 1; l <= left; ++l) {
        for (int r = 1; r <= right; ++r) {
            const int count = l + r;
            const double stop = r * expected[count];
            const double wait = step[count] * (l * (1 + best[r]) + r * best[r - 1]);
            best[r] = std::min(stop, wait);
        }
    }

    const double answer = occupied_left + best[right];
    const auto rounded = static_cast<long long>(std::floor(answer * OUTPUT_SCALE + HALF));
    std::string fraction = std::to_string(rounded % OUTPUT_SCALE + OUTPUT_SCALE).substr(1);
    while (fraction.size() > MIN_DECIMALS && fraction.back() == '0') {
        fraction.pop_back();
    }
    std::cout << rounded / OUTPUT_SCALE << '.' << fraction << '\n';
}
