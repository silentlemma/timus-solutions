#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int BASE = 10;

// the decimal text times 10^d, as an integer
long long scaled(const string &text, int d) {
    long long whole = 0, frac = 0;
    size_t dot = text.find('.');
    for (size_t i = 0; i < min(dot, text.size()); i++)
        whole = whole * BASE + (text[i] - '0');
    for (int i = 0; i < d; i++) {
        size_t at = dot == string::npos ? text.size() : dot + 1 + i;
        frac = frac * BASE + (at < text.size() ? text[at] - '0' : 0);
    }
    long long one = 1;
    for (int i = 0; i < d; i++)
        one *= BASE;
    return whole * one + frac;
}

int main() {
    int d, n;
    cin >> d >> n;
    long long one = 1;
    for (int i = 0; i < d; i++)
        one *= BASE;
    // only the fractional parts matter, and a whole number fits any group
    vector<long long> values;
    for (int i = 0; i < n; i++) {
        string text;
        cin >> text;
        long long v = scaled(text, d) % one;
        if (v != 0 && find(values.begin(), values.end(), v) == values.end())
            values.push_back(v);
    }
    long long den = 2 * one;
    // an average v (times 10^d) over q goblins comes from a total p when
    // (2v - 1) q <= den p < (2v + 1) q; q = 10^d always works, as the
    // interval is then at least 1 long
    for (long long q = 1; q <= one; q++) {
        bool fits = true;
        for (size_t i = 0; i < values.size() && fits; i++) {
            long long v = values[i];
            long long low = ((2 * v - 1) * q + den - 1) / den; // the smallest total allowed
            if (low * den >= (2 * v + 1) * q) {
                // the average that failed is likely to fail again: try it first
                rotate(values.begin(), values.begin() + i, values.begin() + i + 1);
                fits = false;
            }
        }
        if (fits) {
            cout << q << "\n";
            return 0;
        }
    }
}
