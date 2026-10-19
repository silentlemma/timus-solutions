#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

constexpr int SECONDS_PER_MINUTE = 60;
constexpr int SECONDS_PER_HOUR = SECONDS_PER_MINUTE * SECONDS_PER_MINUTE;
constexpr int MAX_INTERVAL = 500;

int read_time() {
    string text;
    cin >> text;
    istringstream input(text);
    int hour, minute, second;
    char separator;
    input >> hour >> separator >> minute >> separator >> second;
    return hour * SECONDS_PER_HOUR + minute * SECONDS_PER_MINUTE + second;
}

void print_time(int seconds) {
    int hour = seconds / SECONDS_PER_HOUR;
    int minute = seconds / SECONDS_PER_MINUTE % SECONDS_PER_MINUTE;
    int second = seconds % SECONDS_PER_MINUTE;
    cout << setfill('0') << setw(2) << hour << ':' << setw(2) << minute << ':' << setw(2)
         << second << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int take_take, take_land, land_take, land_land;
    cin >> take_take >> take_land >> land_take >> land_land;
    int n, m;
    cin >> n;
    vector<int> departures(n), take_result;
    for (int& arrival : departures) arrival = read_time();
    cin >> m;
    vector<int> landings(m), land_result;
    for (int& arrival : landings) arrival = read_time();
    int take_index = 0, land_index = 0;
    int last_take = -MAX_INTERVAL, last_land = -MAX_INTERVAL;
    while (take_index < n || land_index < m) {
        int ready = 0;
        if (take_index < n) {
            ready = max({departures[take_index], last_take + take_take, last_land + land_take});
        }
        if (land_index < m && (take_index == n || landings[land_index] <= ready)) {
            last_land = max({landings[land_index], last_take + take_land, last_land + land_land});
            land_result.push_back(last_land);
            ++land_index;
        } else {
            last_take = ready;
            take_result.push_back(last_take);
            ++take_index;
        }
    }
    for (int time : take_result) print_time(time);
    for (int time : land_result) print_time(time);
}
