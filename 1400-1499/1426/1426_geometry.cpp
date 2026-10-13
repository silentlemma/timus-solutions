#include <algorithm>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

const int POINTS = 4;
const double PAD = 1.0; // width given to a rectangle squeezed onto one line

long long px[POINTS], py[POINTS];
const int LINE = 256;
char buffer[LINE];

// the bounding box with sides along (dx, dy) if every point is on its border
bool frame(long long dx, long long dy, string &out) {
    long long us[POINTS], vs[POINTS];
    for (int i = 0; i < POINTS; i++) {
        us[i] = px[i] * dx + py[i] * dy; // exact integers in the turned frame
        vs[i] = py[i] * dx - px[i] * dy;
    }
    long long loU = *min_element(us, us + POINTS), hiU = *max_element(us, us + POINTS);
    long long loV = *min_element(vs, vs + POINTS), hiV = *max_element(vs, vs + POINTS);
    for (int i = 0; i < POINTS; i++)
        if (us[i] != loU && us[i] != hiU && vs[i] != loV && vs[i] != hiV)
            return false;
    double norm = hypot((double)dx, (double)dy);
    // back to real lengths; a flat box gets some width, still holding every point on a side
    double lu = loU / norm, hu = hiU / norm, lv = loV / norm, hv = hiV / norm;
    if (hiU == loU)
        hu += PAD;
    if (hiV == loV)
        hv += PAD;
    double ex = dx / norm, ey = dy / norm;
    double cu[POINTS] = {lu, hu, hu, lu}, cv[POINTS] = {lv, lv, hv, hv};
    out = "+";
    for (int i = 0; i < POINTS; i++) {
        snprintf(buffer, sizeof buffer, " %.9f %.9f", cu[i] * ex - cv[i] * ey,
                 cu[i] * ey + cv[i] * ex);
        out += buffer;
    }
    return true;
}

int main() {
    int n;
    scanf("%d", &n);
    string all;
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < POINTS; i++)
            scanf("%lld %lld", &px[i], &py[i]);
        // the valid turns form a closed set whose ends make two points tie,
        // so the directions between points are enough to try
        vector<pair<long long, long long>> dirs;
        for (int i = 0; i < POINTS; i++)
            for (int j = i + 1; j < POINTS; j++)
                if (px[i] != px[j] || py[i] != py[j])
                    dirs.push_back({px[j] - px[i], py[j] - py[i]});
        if (dirs.empty())
            dirs.push_back({1, 0});
        string line = "-";
        for (auto &d : dirs)
            if (frame(d.first, d.second, line))
                break;
        all += line + "\n";
    }
    fputs(all.c_str(), stdout);
}
