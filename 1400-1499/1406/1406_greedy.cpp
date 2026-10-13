#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

const int DIGIT = 9; // the largest digit

int main() {
    string s;
    cin >> s;
    int k = s.size(), after = 0; // after: the sum of the digits after position i
    // the rightmost digit that can grow by one while the digits after it give
    // one back; the smallest such change gives the next number
    for (int i = k - 1; i >= 0; i--) {
        int d = s[i] - '0';
        if (d < DIGIT && after > 0) {
            s[i]++;
            int rest = after - 1;
            // the smallest tail with this sum: the digits pushed to the right
            for (int j = k - 1; j > i; j--) {
                int put = min(DIGIT, rest);
                s[j] = char('0' + put);
                rest -= put;
            }
            cout << s << endl;
            return 0;
        }
        after += d;
    }
    cout << -1 << endl;
}
