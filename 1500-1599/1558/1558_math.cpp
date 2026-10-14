#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

// the digits of the line, without the brackets
string digitsOf(const string &line) {
    string s;
    for (char c : line)
        if (isdigit((unsigned char)c))
            s += c;
    return s;
}

// x as k digits, the least significant first
string lowFirst(long long x, int k) {
    string s;
    for (int i = 0; i < k; i++, x /= 10)
        s += char('0' + x % 10);
    return s;
}

int main() {
    string lines[2], line;
    for (int i = 0; i < 2 && getline(cin, line);)
        if (!digitsOf(line).empty())
            lines[i++] = digitsOf(line);
    int k = lines[0].size();
    long long top = 1;
    for (int i = 0; i < k; i++)
        top *= 10;
    long long total = stoll(lines[0]) + stoll(lines[1]);
    // without a carry every block is the plain sum; with one, the lowest block
    // sends a carry on, and every block above it gets the carry and sends one
    string p, digits;
    if (total < top)
        p = digits = lowFirst(total, k);
    else {
        p = lowFirst(total + 1 - top, k);
        digits = lowFirst(total - top, k) + p;
    }
    // the shortest period of the repeated block, then the shortest tail after
    // which every digit repeats the digit that period further up
    int d = 1;
    while (k % d != 0 || p != p.substr(d) + p.substr(0, d))
        d++;
    digits += p + p;
    int start = digits.size() - 2 * k;
    while (start > 0 && digits[start - 1] == digits[start - 1 + d])
        start--;
    string period = digits.substr(start, d), tail = digits.substr(0, start);
    reverse(period.begin(), period.end());
    reverse(tail.begin(), tail.end());
    cout << "(" << period << ")" << tail << endl;
}
