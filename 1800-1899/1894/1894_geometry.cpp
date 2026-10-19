#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;
using int64 = long long;

constexpr int SNAPSHOT_AGE = 60;

struct Point {
    int64 x, y;
};

void rotate_polygon(vector<Point>& points) {
    auto first = min_element(points.begin(), points.end(), [](Point a, Point b) {
        return a.y < b.y || (a.y == b.y && a.x < b.x);
    });
    rotate(points.begin(), first, points.end());
    points.push_back(points.front());
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<Point> airport(n), cloud(m);
    for (auto& point : airport) cin >> point.x >> point.y;
    for (auto& point : cloud) {
        cin >> point.x >> point.y;
        point.x = -point.x;
        point.y = -point.y;
    }
    rotate_polygon(airport);
    rotate_polygon(cloud);
    int64 x = airport[0].x + cloud[0].x, y = airport[0].y + cloud[0].y;
    int i = 0, j = 0;
    double distance = numeric_limits<double>::infinity();
    while (i < n || j < m) {
        int64 ax = i < n ? airport[i + 1].x - airport[i].x : 0;
        int64 ay = i < n ? airport[i + 1].y - airport[i].y : 0;
        int64 bx = j < m ? cloud[j + 1].x - cloud[j].x : 0;
        int64 by = j < m ? cloud[j + 1].y - cloud[j].y : 0;
        int64 turn = ax * by - ay * bx;
        bool take_airport = i < n && (j == m || turn >= 0);
        bool take_cloud = j < m && (i == n || turn <= 0);
        int64 dx = ax * take_airport + bx * take_cloud;
        int64 dy = ay * take_airport + by * take_cloud;
        // The nearest supporting line gives the distance from an interior point.
        double candidate = (x * dy - y * dx) / hypot(static_cast<double>(dx), dy);
        distance = min(distance, candidate);
        x += dx;
        y += dy;
        i += take_airport;
        j += take_cloud;
    }
    cout << fixed << setprecision(10) << max(0.0, distance - SNAPSHOT_AGE) << '\n';
}
