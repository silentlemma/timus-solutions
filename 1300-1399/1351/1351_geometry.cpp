#include <cstdio>
#include <string>

const int FIELDS = 5;

int main() {
    long long reach = 0, rx = 0, ry = 0, lx = 0, ly = 0;
    int n = 0;
    if (scanf("%lld %lld %lld %lld %lld", &reach, &rx, &ry, &lx, &ly) != FIELDS ||
        scanf("%d", &n) != 1)
        return 0;
    std::string out;
    for (int i = 0; i < n; i++) {
        long long x = 0, y = 0;
        if (scanf("%lld %lld", &x, &y) != 2)
            return 0;
        // inside the sector means left of the right border and right of the
        // left one, borders included; the sector is narrower than a half turn
        long long right = rx * y - ry * x, left = x * ly - y * lx;
        bool inside = right >= 0 && left >= 0;
        // a border's extension behind the gun is out; for a sector of zero
        // width, both borders along one ray, no other test rejects it
        bool behind = (right == 0 && rx * x + ry * y < 0) || (left == 0 && lx * x + ly * y < 0);
        out += inside && !behind && x * x + y * y <= reach * reach ? "YES\n" : "NO\n";
    }
    fputs(out.c_str(), stdout);
    return 0;
}
