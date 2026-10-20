#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<long long> board(n * m);
    for (auto &v : board)
        cin >> v;
    string s;
    cin >> s;
    int length = static_cast<int>(s.size());
    vector<int> x(length + 1), y(length + 1);
    const string directions = "RDLU";
    const vector<int> dx = {0, 1, 0, -1}, dy = {1, 0, -1, 0};
    auto cell = [&](int row, int col) -> long long {
        if (row < 0 || row >= n || col < 0 || col >= m)
            return 0;
        return board[row * m + col];
    };
    vector<long long> cost(length + 1);
    cost[0] = cell(0, 0);
    for (int i = 0; i < length; ++i) {
        auto d = directions.find(s[i]);
        x[i + 1] = x[i] + dx[d];
        y[i + 1] = y[i] + dy[d];
        cost[i + 1] = cell(x[i + 1], y[i + 1]);
    }
    long long best = 0;
    int source = 0, target = 0;
    for (size_t d = 0; d < directions.size(); ++d) {
        long long left = 0, right = 0, left_max = 0, right_max = 0;
        int left_at = 0, right_at = -1;
        for (int i = 0; i < length; ++i) {
            // Moving a command changes only one translated interval of the path.
            if (left > left_max) {
                left_max = left;
                left_at = i;
            }
            left += cell(x[i] + dx[d], y[i] + dy[d]) - cost[i + 1];
            if (s[i] == directions[d] && left - left_max < best) {
                best = left - left_max;
                source = i;
                target = left_at;
            }
            if (s[i] == directions[d] && (right_at == -1 || right > right_max)) {
                right_max = right;
                right_at = i;
            }
            right += cell(x[i + 1] - dx[d], y[i + 1] - dy[d]) - cost[i];
            if (right_at != -1 && right - right_max < best) {
                best = right - right_max;
                source = right_at;
                target = i;
            }
        }
    }
    char moved = s[source];
    s.erase(source, 1);
    s.insert(target, 1, moved);
    cout << s << '\n';
}
