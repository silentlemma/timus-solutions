#include <algorithm>
#include <cmath>
#include <iostream>

const double GRAVITY = 9.81, CENTIMETRES = 100, SECONDS = 60;
const int STEPS = 100, TURN = 4;
const double PI = std::acos(-1.0);

double half, top, omega;

// the height of the lowest end of the toast at time t
double gap(double t) {
    return top - GRAVITY * t * t / 2 - half * std::fabs(std::sin(omega * t));
}

// d gap / dt in quarter k, where the angle within the half turn is
// omega*t - (k / 2)*pi
double slope(double t, int k) {
    return -GRAVITY * t - half * omega * std::cos(omega * t - (k / 2) * PI);
}

// d slope / dt, falling through an odd quarter
double bend(double t, int k) {
    return -GRAVITY + half * omega * omega * std::sin(omega * t - (k / 2) * PI);
}

int main() {
    int length, height, turns;
    if (!(std::cin >> length >> height >> turns)) return 0;
    half = length / CENTIMETRES / 2;
    top = height / CENTIMETRES;
    omega = turns * 2 * PI / SECONDS;
    double quarter = PI / 2 / omega;
    int k = 0;
    while (true) {
        double a = k * quarter, b = (k + 1) * quarter, lowest = gap(b);
        if (k % 2 == 1) {
            // the end rises again here: the slope of the gap is concave, so
            // find its peak; where it turns positive, the gap has a minimum
            double lo = a, hi = b;
            for (int i = 0; i < STEPS; i++) {
                double mid = (lo + hi) / 2;
                if (bend(mid, k) > 0) {
                    lo = mid;
                } else {
                    hi = mid;
                }
            }
            if (slope(lo, k) > 0) {
                hi = lo;
                lo = a;
                for (int i = 0; i < STEPS; i++) {
                    double mid = (lo + hi) / 2;
                    if (slope(mid, k) < 0) {
                        lo = mid;
                    } else {
                        hi = mid;
                    }
                }
                lowest = std::min(lowest, gap(lo));
            }
        }
        if (lowest <= 0) break;
        k++;
    }
    // in quarters 0 and 3 of a turn the butter faces down
    int inTurn = k % TURN;
    std::cout << (inTurn == 0 || inTurn == TURN - 1 ? "butter" : "bread") << "\n";
    return 0;
}
