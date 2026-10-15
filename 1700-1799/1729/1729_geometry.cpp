#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>

const long long SCALE = 1000;
const long long HALF_TURN = 180 * SCALE;
const long long FULL_TURN = 2 * HALF_TURN;
const int DIGITS = 3;
const double PI = std::acos(-1.0);

// the angle in thousandths of a degree, read exactly from the text
long long thousandths(const std::string &text) {
    size_t dot = text.find('.');
    std::string whole = text.substr(0, dot);
    std::string part = dot == std::string::npos ? "" : text.substr(dot + 1);
    part = (part + "000").substr(0, DIGITS);
    return (whole.empty() ? 0 : std::stoll(whole)) * SCALE + std::stoll(part);
}

int main() {
    double r;
    std::string angle;
    std::cin >> r >> angle;
    long long a = thousandths(angle);
    // each shore point shows an arc of 2a, so the walk along the shore
    // covers 360 - 2a degrees; chords grow slower than their angles, so
    // it is shortest as full 2a chords and one short chord for the rest
    long long steps = HALF_TURN / a;
    long long rest = FULL_TURN - steps * 2 * a;
    auto chord = [&](long long t) { return 2 * r * std::sin(t * PI / FULL_TURN); };
    printf("%.7f\n", r + (steps - 1) * chord(2 * a) + chord(rest));
}
