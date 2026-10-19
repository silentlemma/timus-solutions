#include <algorithm>
#include <array>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <string>

constexpr int MONTH_COUNT = 12;
constexpr int LONG_MONTH = 31;
constexpr int SHORT_MONTH = 30;
constexpr int FEBRUARY = 28;
constexpr int SOLSTICE_DAY = 171;
constexpr int HOURS_PER_DAY = 24;
constexpr int HOURS_PER_YEAR = 8760;
constexpr int NOON = 12;
constexpr int HALF_TURN = 180;
constexpr int OUTPUT_DIGITS = 10;
constexpr double TILT_DEGREES = 23.439281;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    const std::array<std::string, MONTH_COUNT> months = {"jan", "feb", "mar", "apr", "may", "jun",
                                                         "jul", "aug", "sep", "oct", "nov", "dec"};
    const std::array<int, MONTH_COUNT> lengths = {
        LONG_MONTH, FEBRUARY,   LONG_MONTH,  SHORT_MONTH, LONG_MONTH,  SHORT_MONTH,
        LONG_MONTH, LONG_MONTH, SHORT_MONTH, LONG_MONTH,  SHORT_MONTH, LONG_MONTH};
    const double pi = std::acos(-1.0);
    const double radians = pi / HALF_TURN;
    double latitude;
    int count;
    std::cin >> latitude >> count;
    latitude *= radians;
    const double tilt = TILT_DEGREES * radians;
    const double equatorial = std::cos(latitude) * std::cos(tilt);
    const double transverse = std::cos(latitude);
    const double axial = std::sin(latitude) * std::sin(tilt);
    std::cout << std::fixed << std::setprecision(OUTPUT_DIGITS);
    while (count--) {
        int day, hour;
        std::string month;
        std::cin >> day >> month >> hour;
        int index = day - 1;
        for (int i = 0; months[i] != month; ++i)
            index += lengths[i];
        const int elapsed = (index - SOLSTICE_DAY) * HOURS_PER_DAY + hour - NOON;
        const double orbit = 2 * pi * elapsed / HOURS_PER_YEAR;
        const double spin = orbit + 2 * pi * (hour - NOON) / HOURS_PER_DAY;
        const double sine = equatorial * std::cos(spin) * std::cos(orbit) +
                            transverse * std::sin(spin) * std::sin(orbit) + axial * std::cos(orbit);
        std::cout << std::asin(std::clamp(sine, 0.0, 1.0)) / radians << '\n';
    }
}
