#include <cstdio>
#include <string>
#include <vector>
using namespace std;

typedef long long ll;
const int DIGITS = 10;
const ll PAIR = DIGITS * (DIGITS - 1); // two free mirrored digits that differ

// lucky numbers of this length that start with these digits
ll complete(const vector<int> &prefix, int length) {
    ll ways = 1;
    int fixed = prefix.size();
    for (int i = 0; i < (length + 1) / 2; i++) {
        int j = length - 1 - i;
        if (i == j)
            ways *= i < fixed ? 1 : DIGITS;
        else if (j < fixed) {
            if (prefix[i] == prefix[j])
                return 0;
        } else if (i < fixed)
            ways *= DIGITS - 1; // the partner must differ from the fixed digit
        else
            ways *= PAIR;
    }
    return ways;
}

// lucky tickets numbered 1 .. n
ll luckyUpTo(ll n) {
    if (n <= 0)
        return 0;
    string s = to_string(n);
    int length = s.size();
    vector<int> digits;
    for (char c : s)
        digits.push_back(c - '0');
    ll total = 0;
    // all shorter numbers, by their first digit
    for (int k = 1; k < length; k++)
        for (int d = 1; d < DIGITS; d++)
            total += complete({d}, k);
    // same length: the first position where the number drops below n
    for (int k = 0; k < length; k++) {
        vector<int> prefix(digits.begin(), digits.begin() + k);
        prefix.push_back(0);
        for (int d = k == 0 ? 1 : 0; d < digits[k]; d++) {
            prefix.back() = d;
            total += complete(prefix, length);
        }
    }
    return total + complete(digits, length);
}

int main() {
    ll a, b;
    if (scanf("%lld %lld", &a, &b) != 2)
        return 0;
    printf("%lld\n", luckyUpTo(b) - luckyUpTo(a - 1));
}
