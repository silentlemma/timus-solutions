#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

struct Schedule {
    int busy;
    vector<pair<int, int>> starts;
};

Schedule solve(int window, int capacity, const vector<int>& deadlines) {
    int n = static_cast<int>(deadlines.size());
    int width = n + 1, state_count = width * width, target = state_count - 1;
    int infinity = deadlines.back() + 1;
    vector<int> releases(n);
    for (int i = 0; i < n; ++i) releases[i] = max(0, deadlines[i] - window);
    vector<vector<int>> layers(1, vector<int>(state_count, infinity)), parents(1);
    layers[0][0] = -1;
    vector<int> active{0};
    for (int busy = 1; busy <= 2 * n; ++busy) {
        vector<int> following(state_count, infinity), previous(state_count, -1), next_active;
        for (int state : active) {
            int first_done = state / width, second_done = state % width;
            int earliest = layers.back()[state] + 1;
            for (int new_first = 0; new_first <= min(capacity, n - first_done); ++new_first) {
                int new_second = min(capacity - new_first, first_done - second_done);
                if (new_first + new_second == 0) continue;
                int ni = first_done + new_first, nj = second_done + new_second;
                int minute = new_first ? max(earliest, releases[ni - 1]) : earliest;
                if (new_second && minute >= deadlines[second_done]) continue;
                if (nj < n) {
                    int remaining_sides = nj < ni ? 1 : 2;
                    if (minute + 1 + remaining_sides > deadlines[nj]) continue;
                }
                int destination = ni * width + nj;
                if (minute < following[destination]) {
                    if (following[destination] == infinity) next_active.push_back(destination);
                    following[destination] = minute;
                    previous[destination] = state;
                }
            }
        }
        layers.push_back(move(following));
        parents.push_back(move(previous));
        if (layers.back()[target] != infinity) {
            vector<pair<int, int>> starts(n);
            int state = target;
            for (int used = busy; used > 0; --used) {
                int old_state = parents[used][state];
                int ni = state / width, nj = state % width;
                int oi = old_state / width, oj = old_state % width;
                int minute = layers[used][state];
                for (int job = oi; job < ni; ++job) starts[job].first = minute;
                for (int job = oj; job < nj; ++job) starts[job].second = minute;
                state = old_state;
            }
            return {busy, move(starts)};
        }
        if (next_active.empty()) return {-1, {}};
        active = move(next_active);
    }
    return {-1, {}};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int window, capacity, n;
    cin >> window >> capacity >> n;
    vector<int> deadlines(n);
    for (int& deadline : deadlines) cin >> deadline;
    auto answer = solve(window, capacity, deadlines);
    cout << answer.busy << '\n';
    for (auto [first, second] : answer.starts) cout << first << ' ' << second << '\n';
}
