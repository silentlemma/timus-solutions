#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

const vector<string> DAYS = {"Monday", "Tuesday",  "Wednesday", "Thursday",
                             "Friday", "Saturday", "Sunday"};
// days from September 1 to the first day of each month
const map<string, int> MONTHS = {
    {"September", 0}, {"October", 30}, {"November", 61}, {"December", 91}};

int main() {
    string first, month;
    int day, a, b;
    cin >> first >> month >> day >> a >> b;
    int week = DAYS.size(), start = 0;
    while (DAYS[start] != first)
        start++;
    int match = MONTHS.at(month) + day - 1; // September 1 is day 0
    vector<int> count(week, 0); // training days from September 2 to the eve of the match
    for (int i = 1; i < match; i++)
        count[(start + i) % week]++;
    for (int mask = 1; mask < 1 << week; mask++) {
        vector<int> chosen;
        int total = 0;
        for (int d = 0; d < week; d++)
            if (mask >> d & 1) {
                chosen.push_back(d);
                total += count[d];
            }
        if (a <= total && total <= b) {
            cout << chosen.size() << "\n";
            for (int d : chosen)
                cout << DAYS[d] << "\n";
            return 0;
        }
    }
    cout << "Impossible\n";
}
