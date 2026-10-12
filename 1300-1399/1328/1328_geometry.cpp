#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <vector>

const int FIELDS = 7;
const double HALF_TURN = 180.0;

long long w, h, bx, by;

// the mirror images of B that a straight line from A reaches after the
// given number of bounces: i walls across, j walls up
std::pair<long long, long long> image(int i, int j) {
    return {i * w + (std::abs(i) % 2 == 0 ? bx : w - bx),
            j * h + (std::abs(j) % 2 == 0 ? by : h - by)};
}

std::vector<std::pair<long long, long long>> images(int bounces) {
    std::vector<std::pair<long long, long long>> found;
    for (int i = -bounces; i <= bounces; i++) {
        int rest = bounces - std::abs(i);
        found.push_back(image(i, rest));
        if (rest != 0)
            found.push_back(image(i, -rest));
    }
    return found;
}

int main() {
    long long n = 0, ax = 0, ay = 0;
    if (scanf("%lld %lld %lld %lld %lld %lld %lld", &w, &h, &n, &ax, &ay, &bx, &by) != FIELDS)
        return 0;
    bool found = false;
    long long bestLength = 0;
    double bestAngle = 0;
    for (auto &p : images((int)n)) {
        long long dx = p.first - ax, dy = p.second - ay, length = dx * dx + dy * dy;
        double angle = std::atan2((double)dy, (double)dx) * HALF_TURN / std::acos(-1.0);
        if (angle < 0)
            angle += 2 * HALF_TURN;
        if (!found || length < bestLength || (length == bestLength && angle < bestAngle)) {
            found = true;
            bestLength = length;
            bestAngle = angle;
        }
    }
    printf("%.2f\n", bestAngle);
    return 0;
}
