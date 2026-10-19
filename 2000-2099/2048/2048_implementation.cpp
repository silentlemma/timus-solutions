#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

constexpr int CYCLE = 400, CENTURY = 100, LEAP_STEP = 4;
constexpr int WEEK = 7, FRIDAY = 4, TARGET_DAY = 13;
constexpr int MONTHS = 12, BUCKETS = MONTHS + 1;
constexpr std::array<int, MONTHS> MONTH_LENGTHS = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
using Histogram = std::array<std::int64_t, BUCKETS>;

std::vector<int> calendar_types() {
    int weekday = 0;
    std::vector<int> types;
    for (int year = 1; year <= CYCLE; ++year) {
        bool leap = year % CYCLE == 0 || (year % LEAP_STEP == 0 && year % CENTURY != 0);
        int count = 0;
        for (int month = 0; month < MONTHS; ++month) {
            count += (weekday + TARGET_DAY - 1) % WEEK == FRIDAY;
            weekday = (weekday + MONTH_LENGTHS[month] + (month == 1 && leap)) % WEEK;
        }
        types.push_back(count);
    }
    return types;
}

Histogram prefix(std::int64_t year, const std::vector<int> &types, const Histogram &cycle_counts) {
    Histogram answer{};
    for (int k = 0; k < BUCKETS; ++k)
        answer[k] = year / CYCLE * cycle_counts[k];
    for (int i = 0; i < year % CYCLE; ++i)
        ++answer[types[i]];
    return answer;
}

Histogram solve(std::int64_t first, std::int64_t last, const std::vector<int> &types,
                const Histogram &cycle_counts) {
    auto high = prefix(last, types, cycle_counts);
    auto low = prefix(first - 1, types, cycle_counts);
    for (int k = 0; k < BUCKETS; ++k)
        high[k] -= low[k];
    return high;
}

int main() {
    std::int64_t first, last;
    std::cin >> first >> last;
    auto types = calendar_types();
    Histogram cycle_counts{};
    for (int count : types)
        ++cycle_counts[count];
    auto answer = solve(first, last, types, cycle_counts);
    for (int k = 0; k < BUCKETS; ++k)
        std::cout << k << ": " << answer[k] << '\n';
}
