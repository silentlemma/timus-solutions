#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

const string DIGITS[] = {"._.|.||_|", ".....|..|", "._.._||_.", "._.._|._|", "...|_|..|",
                         "._.|_.._|", "._.|_.|_|", "._...|..|", "._.|_||_|", "._.|_|._|"};
constexpr int COLUMNS[] = {0, 4, 10, 14};  // where the four digits start
constexpr int WIDTH = 3;
constexpr int SECONDS = 60;  // MM:SS runs from 00:00 to 59:59
constexpr int COUNT = 4;     // digits on the dial

// every lit segment must belong to the digit
bool fits(const string& shown, int digit) {
    for (int i = 0; i < WIDTH * WIDTH; i++)
        if (shown[i] != '.' && shown[i] != DIGITS[digit][i]) return false;
    return true;
}

int main() {
    int n;
    cin >> n;
    int previous = SECONDS * SECONDS;
    for (int r = 0; r < n; r++) {
        string rows[WIDTH];
        for (string& row : rows) cin >> row;
        bool ok[COUNT][10];
        for (int k = 0; k < COUNT; k++) {
            string cell;
            for (const string& row : rows) cell += row.substr(COLUMNS[k], WIDTH);
            for (int d = 0; d < 10; d++) ok[k][d] = fits(cell, d);
        }
        // the largest time that fits and stays below the previous one leaves the
        // most room for the rest, so it never spoils a solution
        int value = previous - 1, m, s;
        for (;; value--) {
            m = value / SECONDS, s = value % SECONDS;
            int digits[COUNT] = {m / 10, m % 10, s / 10, s % 10};
            bool all = true;
            for (int k = 0; k < COUNT; k++) all = all && ok[k][digits[k]];
            if (all) break;
        }
        printf("%02d:%02d\n", m, s);
        previous = value;
    }
}
