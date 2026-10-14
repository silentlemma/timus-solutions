#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

const long long HUNDRED = 100;        // times are kept in hundredths of a second, exactly
const long long STAND = 15 * HUNDRED; // the lift stands this long on the first floor
const long long BOARD = 5 * HUNDRED;  // getting into the lift
const int DIGITS = 2;

// a number with at most two decimals, as an exact integer of hundredths
long long hundredths(const string &word) {
    size_t dot = word.find('.');
    string whole = word.substr(0, dot), frac = dot == string::npos ? "" : word.substr(dot + 1);
    frac = (frac + "00").substr(0, DIGITS);
    return stoll(whole) * HUNDRED + stoll(frac);
}

int main() {
    long long n, k;
    string us, vs;
    if (!(cin >> n >> k >> us >> vs))
        return 0;
    long long u = hundredths(us), v = hundredths(vs);
    // walking all the way down needs no lift
    long long bestFloor = 1, bestTime = (n - 1) * u;
    long long ready = (k - 1) * v + STAND; // the lift may leave the first floor from then on
    for (long long f = 2; f <= n; f++) {
        // Petya calls the lift on reaching floor f; it comes up, waits for
        // the boarding and goes down again
        long long start = max(ready, (n - f) * u);
        long long total = start + (f - 1) * v + BOARD + (f - 1) * v;
        // a later floor means less walking, so ties go to it
        if (total <= bestTime) {
            bestFloor = f;
            bestTime = total;
        }
    }
    cout << bestFloor << "\n";
}
