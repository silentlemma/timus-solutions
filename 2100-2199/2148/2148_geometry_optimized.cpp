#include <cmath>
#include <cstdio>

const long long DECIMAL_SCALE = 1000000000;
const int FRACTION_DIGITS = 9;
const int DIAMETER_SQUARED_FACTOR = 4;
const int OUTPUT_SIZE = 64;
const int INTEGER_DIGITS = 32;

void appendCoordinate(char *&out, double value) {
    long long scaled = std::llround(value * DECIMAL_SCALE);
    if (scaled < 0) {
        *out++ = '-';
        scaled = -scaled;
    }
    long long whole = scaled / DECIMAL_SCALE;
    char digits[INTEGER_DIGITS];
    int count = 0;
    do {
        digits[count++] = char('0' + whole % 10);
        whole /= 10;
    } while (whole);
    while (count)
        *out++ = digits[--count];
    *out++ = '.';
    long long fraction = scaled % DECIMAL_SCALE;
    long long divisor = DECIMAL_SCALE / 10;
    for (int i = 0; i < FRACTION_DIGITS; ++i) {
        *out++ = char('0' + fraction / divisor);
        fraction %= divisor;
        divisor /= 10;
    }
}

int main() {
    long long cx, cy, radius, ax, ay, bx, by;
    scanf("%lld %lld %lld %lld %lld %lld %lld", &cx, &cy, &radius, &ax, &ay, &bx, &by);
    long long wx = ax + bx - 2 * cx, wy = ay + by - 2 * cy;
    long long norm = wx * wx + wy * wy;
    // Equal centre distances give (A-C).w = |w|²/2; exclude tangency strictly.
    if (norm <= DIAMETER_SQUARED_FACTOR * radius * radius) {
        puts("No way");
        return 0;
    }
    double scale = radius / std::sqrt(double(norm));
    char output[OUTPUT_SIZE], *out = output;
    appendCoordinate(out, cx + wx * scale);
    *out++ = ' ';
    appendCoordinate(out, cy + wy * scale);
    *out++ = '\n';
    fwrite(output, 1, out - output, stdout);
}
