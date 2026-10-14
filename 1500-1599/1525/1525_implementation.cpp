#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

const int AXES = 3;

int main() {
    long long size[AXES];
    string program;
    cin >> size[0] >> size[1] >> size[2];
    cin >> program; // stays empty when there are no instructions
    // the moves along each axis: decrease, increase
    const string down = "ldb", up = "ruf";
    long long total = 1;
    for (int a = 0; a < AXES; a++) {
        // each move keeps neighbouring starts at most one apart and in order,
        // so the finishes fill the range between the extreme starts
        long long low = 1, high = size[a];
        for (char step : program)
            if (step == up[a])
                low = min(low + 1, size[a]), high = min(high + 1, size[a]);
            else if (step == down[a])
                low = max(low - 1, 1LL), high = max(high - 1, 1LL);
        total *= high - low + 1;
    }
    cout << total << "\n";
}
