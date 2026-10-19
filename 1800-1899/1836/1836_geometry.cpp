#include <cstdio>
#include <string>

const int CORNERS = 4;
const double TETRAHEDRON = 6;  // a corner with legs a, b, c cuts off abc/6
const int BUFFER = 64;

std::string fixed(double v) {
    char buf[BUFFER];
    snprintf(buf, sizeof buf, "%.6f", v);
    return buf;
}

std::string volume(long long side, const long long h[]) {
    // the surface is a plane, so the levels at opposite corners add up to
    // the same sum; a sensor reads max(0, level), and 0 hides the level
    int dry = 0, at = -1;
    long long diagonal[2] = {0, 0}, total = 0;
    bool hidden[2] = {false, false};
    for (int i = 0; i < CORNERS; i++) {
        diagonal[i % 2] += h[i];
        total += h[i];
        if (h[i] == 0) {
            dry++;
            at = i;
            hidden[i % 2] = true;
        }
    }
    double area = double(side) * side;
    if (dry == CORNERS) return fixed(0);
    if (dry == 0) {
        if (diagonal[0] != diagonal[1]) return "error";
        return fixed(area * total / CORNERS);
    }
    if (dry == 1) {
        long long left = h[(at + 1) % CORNERS], far = h[(at + 2) % CORNERS];
        long long right = h[(at + CORNERS - 1) % CORNERS], x = left + right - far;
        if (x > 0) return "error";
        // the plane dips below the bottom at the dry corner in a tetrahedron
        // with legs -x up and -x/(left - x), -x/(right - x) along the edges,
        // so that much negative water is added back
        double dip = -double(x);
        double level = double(total + x) / CORNERS +
                       dip * dip * dip / (TETRAHEDRON * double(left - x) * double(right - x));
        return fixed(area * level);
    }
    // two or more hidden levels: they only have to be at most 0 and keep
    // the two diagonal sums equal, and when that is possible they can move
    if (hidden[0] && hidden[1]) return "ambiguous";
    int low = hidden[0] ? 0 : 1;
    return diagonal[1 - low] > diagonal[low] ? "error" : "ambiguous";
}

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    std::string out;
    while (t--) {
        long long side, h[CORNERS];
        scanf("%lld", &side);
        for (auto &v : h) scanf("%lld", &v);
        out += volume(side, h) + "\n";
    }
    fputs(out.c_str(), stdout);
    return 0;
}
