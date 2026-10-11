#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>

// the distance along one axis once the room is mirrored at each hit
long long unfolded(int start, int end, int size, char low, const std::string &hits) {
    if (hits.empty())
        return std::abs(end - start);
    int first = hits.front() == low ? start : size - start;
    int last = hits.back() == low ? end : size - end;
    return first + (long long)(hits.size() - 1) * size + last;
}

int main() {
    int w, d, x0, y0, x1, y1;
    scanf("%d %d %d %d %d %d", &w, &d, &x0, &y0, &x1, &y1);
    std::string side, ends;
    for (int c; (c = getchar()) != EOF;) {
        if (c == 'L' || c == 'R')
            side += char(c);
        if (c == 'F' || c == 'B')
            ends += char(c);
    }
    long long dx = unfolded(x0, x1, w, 'L', side), dy = unfolded(y0, y1, d, 'F', ends);
    printf("%.4f\n", std::sqrt(double(dx * dx + dy * dy)));
}
