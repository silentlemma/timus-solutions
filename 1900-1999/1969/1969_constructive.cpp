#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

constexpr int kSecondsPerMinute = 60;
constexpr int kMinutesPerHour = 60;
constexpr int kSecondsPerHour = kSecondsPerMinute * kMinutesPerHour;

struct Schedule {
    int duration, trips;
    std::vector<int> departures;
};

Schedule recover(int first, const std::vector<int> &passages) {
    int count = static_cast<int>(passages.size());
    int offset = passages[0] - first, last = passages.back();
    int totalSpan = last - first + offset;
    std::vector<bool> present(last + 1, false);
    std::vector<int> marked(last + 1, 0);
    for (int time : passages)
        present[time] = true;
    int epoch = 0;
    for (int index = 1; index <= count / 2; ++index) {
        int period = passages[index] - first + offset;
        if (period % 2 || period <= 2 * offset)
            continue;
        int trips = totalSpan / period;
        if (trips == 0 || count % (2 * trips))
            continue;
        int tramCount = count / (2 * trips), gap = period - 2 * offset;
        ++epoch;
        std::vector<int> departures;
        bool failed = false;
        for (int time : passages) {
            if (marked[time] == epoch)
                continue;
            int departure = time - offset;
            if (departure >= first + period || static_cast<int>(departures.size()) == tramCount) {
                failed = true;
                break;
            }
            int outward = time;
            for (int trip = 0; trip < trips; ++trip) {
                int returning = outward + gap;
                if (outward > last || returning > last || !present[outward] ||
                    !present[returning] || marked[outward] == epoch || marked[returning] == epoch) {
                    failed = true;
                    break;
                }
                marked[outward] = marked[returning] = epoch;
                outward += period;
            }
            if (failed)
                break;
            departures.push_back(departure);
        }
        if (!failed && static_cast<int>(departures.size()) == tramCount) {
            return {period / 2, trips, departures};
        }
    }
    throw std::runtime_error("The guaranteed schedule was not found");
}

int parseTime(const std::string &text) {
    std::istringstream input(text);
    int hours, minutes, seconds;
    char separator;
    input >> hours >> separator >> minutes >> separator >> seconds;
    return hours * kSecondsPerHour + minutes * kSecondsPerMinute + seconds;
}

std::string formatTime(int value) {
    std::ostringstream output;
    output << std::setfill('0') << std::setw(2) << value / kSecondsPerHour << ':' << std::setw(2)
           << value / kSecondsPerMinute % kMinutesPerHour << ':' << std::setw(2)
           << value % kSecondsPerMinute;
    return output.str();
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string text;
    std::cin >> text;
    int first = parseTime(text);
    std::vector<int> passages;
    while (std::cin >> text)
        passages.push_back(parseTime(text));
    auto schedule = recover(first, passages);
    for (int departure : schedule.departures) {
        for (int step = 0; step <= 2 * schedule.trips; ++step) {
            if (step)
                std::cout << ' ';
            std::cout << formatTime(departure + step * schedule.duration);
        }
        std::cout << '\n';
    }
}
