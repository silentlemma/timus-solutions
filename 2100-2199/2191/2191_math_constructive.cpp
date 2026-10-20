#include <cstdio>
#include <string>
#include <vector>

constexpr int DIGITS = 18;

// Appends a nonnegative fraction with at most DIGITS decimals, truncated.
void number(std::string &out, long long numerator, long long denominator) {
    out += std::to_string(numerator / denominator);
    long long rest = numerator % denominator;
    if (rest == 0) return;
    out += '.';
    for (int i = 0; i < DIGITS; i++) {
        rest *= 10;
        out += static_cast<char>('0' + rest / denominator);
        rest %= denominator;
    }
    while (out.back() == '0') out.pop_back();
    if (out.back() == '.') out.pop_back();
}

int main() {
    int n;
    scanf("%d", &n);
    std::vector<long long> xs(n), ys(n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &xs[i], &ys[i]);
    std::string out;

    // Writes c |x - root| with c = numerator / denominator as one term.
    auto term = [&](long long numerator, long long denominator, long long root, bool constant) {
        if (numerator < 0) {
            out += '-';
            numerator = -numerator;
        } else if (!out.empty()) {
            out += '+';
        }
        out += '|';
        if (constant) {
            out += "0x+";
            number(out, numerator, denominator);
        } else {
            long long shift = numerator * root;
            number(out, numerator, denominator);
            out += shift >= 0 ? "x-" : "x+";
            number(out, shift >= 0 ? shift : -shift, denominator);
        }
        out += '|';
    };

    // A kink at x_i where the slope turns from s to t is (t - s) / 2 |x - x_i|.
    for (int i = 1; i + 1 < n; i++) {
        long long left_dx = xs[i] - xs[i - 1], left_dy = ys[i] - ys[i - 1];
        long long right_dx = xs[i + 1] - xs[i], right_dy = ys[i + 1] - ys[i];
        term(right_dy * left_dx - left_dy * right_dx, 2 * left_dx * right_dx, xs[i], false);
    }

    long long first_dx = xs[1] - xs[0], first_dy = ys[1] - ys[0];
    long long last_dx = xs[n - 1] - xs[n - 2], last_dy = ys[n - 1] - ys[n - 2];
    // On [x_1, x_N] the kinks add (t - s) / 2 times x - x_i; the term at x_1
    // restores the first slope and a constant fixes the value at x_1.
    term(first_dy * last_dx + last_dy * first_dx, 2 * first_dx * last_dx, xs[0], false);
    long long span = xs[n - 2] - xs[0];
    term(2 * ys[0] * last_dx - last_dy * span + (ys[n - 2] - ys[0]) * last_dx, 2 * last_dx, 0,
         true);
    out += '\n';
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
