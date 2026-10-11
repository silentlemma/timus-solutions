#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

typedef long long ll;

const ll SIGNAL = 1000000; // signal values are read in millionths
const ll FACTOR = 1000;    // A has at most three decimals
const int SIGNAL_DIGITS = 6, FACTOR_DIGITS = 3;
const ll WALL = 95, LOW = 35;
const int CHANNELS = 2;
const int WORD = 64; // longer than any number in the input

// a non-negative decimal as an exact multiple of 1 / 10^digits
ll scaled(const std::string &token, int digits) {
    size_t dot = token.find('.');
    std::string whole = token.substr(0, dot),
                frac = dot == std::string::npos ? "" : token.substr(dot + 1);
    frac = (frac + std::string(digits, '0')).substr(0, digits);
    ll scale = 1;
    for (int i = 0; i < digits; i++)
        scale *= 10;
    return (whole.empty() ? 0 : std::stoll(whole)) * scale + std::stoll(frac);
}

std::string word() {
    char buf[WORD];
    scanf("%63s", buf);
    return buf;
}

int main() {
    int n, d, s[CHANNELS], e[CHANNELS], level[CHANNELS];
    scanf("%d %d %d %d %d %d %d %d", &n, &d, &s[0], &e[0], &level[0], &s[1], &e[1], &level[1]);
    ll a = scaled(word(), FACTOR_DIGITS);
    std::vector<ll> raw(n);
    for (ll &x : raw)
        x = scaled(word(), SIGNAL_DIGITS);
    ll unit = SIGNAL * FACTOR;
    // the front wall: the first value of 95 or more after a value of 35 or less
    int surface = -1;
    bool low = false;
    for (int i = 0; i < n && surface < 0; i++) {
        if (low && raw[i] >= WALL * SIGNAL)
            surface = i;
        low = low || raw[i] <= LOW * SIGNAL;
    }
    if (surface < 0) {
        printf("No surface.\n");
        return 0;
    }
    printf("Surface found at %d.\n", surface + 1);
    // after the wall every value is multiplied by 1 + (m - f) A, here in
    // units of 1 / (SIGNAL * FACTOR)
    std::vector<ll> value(n);
    for (int i = 0; i < n; i++)
        value[i] = raw[i] * (i <= surface ? FACTOR : FACTOR + (i - surface) * a);
    int bottom = -1;
    low = false;
    for (int i = surface + 1; i < n && bottom < 0; i++) {
        if (low && i - surface >= d && value[i] >= WALL * unit)
            bottom = i;
        low = low || value[i] <= LOW * unit;
    }
    if (bottom < 0)
        printf("No bottom.\n");
    else
        printf("Bottom found at %d.\n", bottom - surface);
    int end = bottom >= 0 ? bottom - 1 : n - 1;
    for (int c = 0; c < CHANNELS; c++) {
        int lo = surface + s[c], hi = std::min(surface + e[c], end);
        if (lo > hi) {
            printf("Channel %d: No search.\n", c + 1);
            continue;
        }
        int best = lo;
        for (int i = lo + 1; i <= hi; i++)
            if (value[i] > value[best])
                best = i;
        if (value[best] >= level[c] * unit)
            printf("Channel %d: Object at %d.\n", c + 1, best - surface);
        else
            printf("Channel %d: No object.\n", c + 1);
    }
}
