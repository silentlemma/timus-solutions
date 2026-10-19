#include <iostream>

constexpr int TOTAL_TASKS = 12;
constexpr int FIRST_HOUR_MINUTES = 60;
constexpr int MINUTES_PER_TASK = 45;
constexpr int CONTEST_MINUTES = 300;

bool solve(int first_hour) {
    return FIRST_HOUR_MINUTES + (TOTAL_TASKS - first_hour) * MINUTES_PER_TASK <= CONTEST_MINUTES;
}

int main() {
    int first_hour;
    std::cin >> first_hour;
    std::cout << (solve(first_hour) ? "YES" : "NO") << '\n';
}
