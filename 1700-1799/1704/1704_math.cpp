#include <cmath>
#include <cstdio>
#include <string>
#include <vector>

const int BITS = 8;  // bits of a character, the lowest first
const int ONE_FREQ = 2;  // a one is sin(2 pi k / t), a zero sin(4 pi k / t)
const int ZERO_FREQ = 4;

int main() {
    int n, t;
    scanf("%d %d", &n, &t);
    std::vector<double> samples(n);
    for (double& x : samples) {
        scanf("%lf", &x);
    }
    // over a whole number of periods sin(2 pi k / t) and sin(4 pi k / t) are
    // orthogonal to each other and to a constant, so the correlation of a bit's
    // samples with each wave picks the wave that was sent
    const double PI = std::acos(-1.0);
    std::vector<int> bits;
    for (int start = 0; start < n; start += t) {
        double one = 0, zero = 0;
        for (int k = 0; k < t; k++) {
            one += samples[start + k] * std::sin(ONE_FREQ * PI * k / t);
            zero += samples[start + k] * std::sin(ZERO_FREQ * PI * k / t);
        }
        bits.push_back(one > zero);
    }
    std::string text;
    for (size_t start = 0; start < bits.size(); start += BITS) {
        int c = 0;
        for (int j = 0; j < BITS; j++) {
            c |= bits[start + j] << j;
        }
        text += (char)c;
    }
    printf("%s\n", text.c_str());
}
