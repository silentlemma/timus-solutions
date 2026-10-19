#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

constexpr double HALF = 0.5;
constexpr int BOUNDARIES_PER_EVENT = 3;
constexpr int OUTPUT_PRECISION = 17;

struct Event {
    int time, first, second;
    bool enforce;
};

class EnergyTree {
    const vector<int> &coordinates;
    vector<double> total, low, high;
    vector<unsigned char> cleared;

    void apply(int node, int length, double first, double last) {
        total[node] += (first + last) * HALF * length;
        low[node] += first;
        high[node] += last;
    }

    void push(int node, int left, int middle, int right) {
        int child = node + 1, other = node + 2 * (middle - left);
        if (cleared[node]) {
            total[child] = low[child] = high[child] = 0;
            total[other] = low[other] = high[other] = 0;
            cleared[child] = cleared[other] = 1;
            cleared[node] = 0;
        }
        double first = low[node], last = high[node];
        if (first == 0 && last == 0)
            return;
        int length = coordinates[right] - coordinates[left];
        int leftLength = coordinates[middle] - coordinates[left];
        int rightLength = length - leftLength;
        if (first == last) {
            apply(child, leftLength, first, first);
            apply(other, rightLength, first, first);
        } else {
            double denominator = length - 1;
            double leftLast = (first * rightLength + last * (leftLength - 1)) / denominator;
            double rightFirst = (first * (rightLength - 1) + last * leftLength) / denominator;
            apply(child, leftLength, first, leftLast);
            apply(other, rightLength, rightFirst, last);
        }
        low[node] = high[node] = 0;
    }

  public:
    explicit EnergyTree(const vector<int> &xs)
        : coordinates(xs), total(2 * (xs.size() - 1) - 1), low(total.size()), high(total.size()),
          cleared(total.size()) {}

    void grow(double amount, int length) {
        total[0] += amount * length;
        low[0] += amount;
        high[0] += amount;
    }

    void add(int node, int left, int right, int begin, int end, int origin, int direction,
             double scale) {
        if (begin <= left && right <= end) {
            double first = scale * (origin + direction * coordinates[left]);
            double last = scale * (origin + direction * (coordinates[right] - 1));
            apply(node, coordinates[right] - coordinates[left], first, last);
            return;
        }
        int middle = (left + right) / 2;
        push(node, left, middle, right);
        if (begin < middle)
            add(node + 1, left, middle, begin, end, origin, direction, scale);
        int other = node + 2 * (middle - left);
        if (end > middle)
            add(other, middle, right, begin, end, origin, direction, scale);
        total[node] = total[node + 1] + total[other];
    }

    double take(int node, int left, int right, int begin, int end) {
        if (begin <= left && right <= end) {
            double answer = total[node];
            total[node] = low[node] = high[node] = 0;
            cleared[node] = 1;
            return answer;
        }
        int middle = (left + right) / 2;
        push(node, left, middle, right);
        double answer = 0;
        if (begin < middle)
            answer += take(node + 1, left, middle, begin, end);
        int other = node + 2 * (middle - left);
        if (end > middle)
            answer += take(other, middle, right, begin, end);
        total[node] = total[node + 1] + total[other];
        return answer;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int length, rate, count;
    if (!(cin >> length >> rate >> count))
        return 0;
    vector<Event> events(count);
    vector<int> coordinates = {1, length + 1};
    coordinates.reserve(BOUNDARIES_PER_EVENT * count + 2);
    for (Event &event : events) {
        string kind;
        cin >> event.time >> kind >> event.first >> event.second;
        event.enforce = kind == "enforce";
        if (event.enforce) {
            coordinates.push_back(event.first - event.second + 1);
            coordinates.push_back(event.first + 1);
            coordinates.push_back(event.first + event.second);
        } else {
            coordinates.push_back(event.first);
            coordinates.push_back(event.second + 1);
        }
    }
    sort(coordinates.begin(), coordinates.end());
    coordinates.erase(unique(coordinates.begin(), coordinates.end()), coordinates.end());
    auto index = [&](int position) {
        return int(lower_bound(coordinates.begin(), coordinates.end(), position) -
                   coordinates.begin());
    };
    EnergyTree tree(coordinates);
    int leaves = int(coordinates.size()) - 1, previous = 0;
    double reserve = 0;
    cout << setprecision(OUTPUT_PRECISION);
    for (const Event &event : events) {
        double growth = double(rate) * (event.time - previous);
        if (growth != 0)
            tree.grow(growth, length);
        previous = event.time;
        if (event.enforce) {
            if (reserve == 0)
                continue;
            int begin = event.first - event.second + 1;
            int middle = event.first + 1;
            int end = event.first + event.second;
            int a = index(begin), b = index(middle), c = index(end);
            double scale = reserve / (double(event.second) * event.second);
            tree.add(0, 0, leaves, a, b, 1 - begin, 1, scale);
            if (b < c)
                tree.add(0, 0, leaves, b, c, end, -1, scale);
            reserve = 0;
        } else {
            reserve += tree.take(0, 0, leaves, index(event.first), index(event.second + 1));
            cout << reserve << '\n';
        }
    }
}
