#include <iostream>
#include <string>

using namespace std;

const int DIGITS = 4; // lengths are given to a tenth of a millimetre

// a length in tenths of a millimetre, read exactly
long long tenths(const string &text) {
    size_t dot = text.find('.');
    string whole = text.substr(0, dot);
    string frac = dot == string::npos ? "" : text.substr(dot + 1);
    frac = (frac + string(DIGITS, '0')).substr(0, DIGITS);
    long long scale = 1;
    for (int i = 0; i < DIGITS; i++)
        scale *= 10;
    return (whole.empty() ? 0 : stoll(whole)) * scale + stoll(frac);
}

int main() {
    long long n;
    string s_text, rail_text;
    cin >> n >> s_text >> rail_text;
    long long s = tenths(s_text), rail = tenths(rail_text);
    long long full = s / rail, rest = s % rail;
    if (rest == 0) {
        cout << n * full << "\n";
        return 0;
    }
    // each line takes its full rails and a short piece; a rail holds rail / rest such pieces
    long long per_rail = rail / rest;
    cout << n * full + (n + per_rail - 1) / per_rail << "\n";
}
