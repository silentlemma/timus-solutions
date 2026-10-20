#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;
using Coordinate = long long;
constexpr int FULL_TURN = 4;
constexpr int THREE_QUARTERS = FULL_TURN - 1;

struct Event {
    Coordinate x, low, high;
    int index, sign;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<Coordinate, Coordinate>> points(n);
    vector<Coordinate> ys;
    for (auto &point : points) {
        cin >> point.first >> point.second;
        ys.push_back(point.second);
    }
    sort(points.begin(), points.end());
    sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());
    int q, orientation = 0;
    Coordinate tx = 0, ty = 0;
    cin >> q;
    vector<Event> events;
    vector<int> answers;
    while (q--) {
        string command;
        Coordinate x, y;
        cin >> command >> x >> y;
        if (command != "ask") {
            int turns = command == "r90" ? 1 : command == "r180" ? 2 : THREE_QUARTERS;
            Coordinate dx = tx - x, dy = ty - y;
            for (int step = 0; step < turns; ++step) {
                Coordinate next = -dy;
                dy = dx;
                dx = next;
            }
            tx = x + dx;
            ty = y + dy;
            orientation = (orientation + turns) % FULL_TURN;
        } else {
            Coordinate xx, yy;
            cin >> xx >> yy;
            x -= tx;
            y -= ty;
            xx -= tx;
            yy -= ty;
            // Undo the global transform on two opposite corners.
            for (int step = 0; step < orientation; ++step) {
                Coordinate next = y;
                y = -x;
                x = next;
                next = yy;
                yy = -xx;
                xx = next;
            }
            if (x > xx)
                swap(x, xx);
            if (y > yy)
                swap(y, yy);
            int index = static_cast<int>(answers.size());
            answers.push_back(0);
            events.push_back({xx, y, yy, index, 1});
            events.push_back({x - 1, y, yy, index, -1});
        }
    }
    sort(events.begin(), events.end(), [](const Event &a, const Event &b) { return a.x < b.x; });
    vector<int> tree(ys.size() + 1);
    auto prefix = [&](int index) {
        int sum = 0;
        for (; index > 0; index -= index & -index)
            sum += tree[index];
        return sum;
    };
    size_t inserted = 0;
    int size = static_cast<int>(ys.size());
    for (const auto &event : events) {
        while (inserted < points.size() && points[inserted].first <= event.x) {
            int index =
                static_cast<int>(lower_bound(ys.begin(), ys.end(), points[inserted].second) -
                                 ys.begin()) +
                1;
            for (; index <= size; index += index & -index)
                ++tree[index];
            ++inserted;
        }
        int low = static_cast<int>(lower_bound(ys.begin(), ys.end(), event.low) - ys.begin());
        int high = static_cast<int>(upper_bound(ys.begin(), ys.end(), event.high) - ys.begin());
        answers[event.index] += event.sign * (prefix(high) - prefix(low));
    }
    for (int answer : answers)
        cout << answer << '\n';
}
