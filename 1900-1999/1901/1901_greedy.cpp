#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

pair<int, vector<int>> arrange(vector<int> values, int capacity) {
    sort(values.begin(), values.end());
    vector<int> queue;
    queue.reserve(values.size());
    int left = 0, right = static_cast<int>(values.size()) - 1, trips = 0;
    while (left < right) {
        if (values[left] + values[right] > capacity) {
            // The largest value is also incompatible with every remaining value.
            queue.push_back(values[left++]);
            queue.push_back(values[right--]);
            trips += 2;
        } else {
            queue.push_back(values[left++]);
            queue.push_back(values[left++]);
            ++trips;
        }
    }
    if (left == right) {
        queue.push_back(values[left]);
        ++trips;
    }
    return {trips, move(queue)};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, capacity;
    cin >> n >> capacity;
    vector<int> values(n);
    for (int& value : values) cin >> value;
    auto result = arrange(move(values), capacity);
    cout << result.first << '\n';
    for (int i = 0; i < n; ++i) cout << (i ? " " : "") << result.second[i];
    cout << '\n';
}
