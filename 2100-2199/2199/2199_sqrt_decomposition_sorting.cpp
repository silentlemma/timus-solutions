#include <algorithm>
#include <cmath>
#include <iostream>
#include <numeric>
#include <set>
#include <tuple>
#include <unordered_map>
#include <vector>

using namespace std;

constexpr int VALUE_LIMIT = 1000000000;
constexpr int INFINITY_SCORE = 2 * VALUE_LIMIT + 1;

struct Answer {
    int score = INFINITY_SCORE;
    int first = 0;
    int second = 0;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> days(n), order(n), ranks(n), values(n), potential(n, INFINITY_SCORE);
    for (int &value : days)
        cin >> value;
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(),
         [&](int a, int b) { return make_pair(abs(days[a]), a) < make_pair(abs(days[b]), b); });
    vector<pair<int, int>> numeric;
    for (int rank = 0; rank < n; ++rank) {
        ranks[order[rank]] = rank;
        values[rank] = days[order[rank]];
        numeric.emplace_back(values[rank], rank);
    }
    sort(numeric.begin(), numeric.end());
    for (int rank = 0; rank < n; ++rank) {
        int pos = lower_bound(numeric.begin(), numeric.end(), make_pair(-values[rank], -1)) -
                  numeric.begin();
        for (int other = max(0, pos - 2); other < min(n, pos + 2); ++other)
            if (numeric[other].second != rank)
                potential[rank] = min(potential[rank], abs(values[rank] + numeric[other].first));
    }
    int block_size = max(1, 2 * n / max(1, static_cast<int>(sqrt(q))));
    vector<vector<tuple<int, int, int>>> buckets((n + block_size - 1) / block_size);
    unordered_map<long long, int> last;
    vector<pair<int, int>> global_pairs(n), answers(q);
    pair<int, int> global_pair = {-1, -1};
    int global_score = *min_element(potential.begin(), potential.end());
    for (int day = 0; day < n; ++day) {
        for (long long target :
             {-1LL * days[day] - global_score, -1LL * days[day] + global_score}) {
            auto found = last.find(target);
            if (found != last.end() && found->second > global_pair.first)
                global_pair = {found->second, day};
        }
        global_pairs[day] = global_pair;
        last[days[day]] = day;
    }
    for (int id = 0; id < q; ++id) {
        int left, right;
        cin >> left >> right;
        --left;
        auto [first, second] = global_pairs[right - 1];
        if (first >= left)
            answers[id] = {first + 1, second + 1};
        else
            buckets[left / block_size].emplace_back(right, left, id);
    }
    for (int block = 0; block < static_cast<int>(buckets.size()); ++block) {
        auto &queries = buckets[block];
        sort(queries.begin(), queries.end());
        int boundary = min(n, (block + 1) * block_size);
        int end = boundary;
        set<int> active;
        Answer core_best;
        auto add = [&](int rank, Answer &best) {
            // The global bound remains valid as the best score decreases.
            if (potential[rank] >= best.score)
                return false;
            auto next = active.lower_bound(rank);
            auto consider = [&](int other) {
                int score = abs(values[rank] + values[other]);
                if (score < best.score)
                    best = {score, order[rank], order[other]};
            };
            if (next != active.begin())
                consider(*prev(next));
            if (next != active.end())
                consider(*next);
            active.insert(next, rank);
            return true;
        };
        int start = block * block_size;
        vector<Answer> suffix_best(boundary - start + 1);
        Answer fringe_best;
        for (int day = boundary - 1; day >= start; --day) {
            add(ranks[day], fringe_best);
            suffix_best[day - start] = fringe_best;
        }
        active.clear();
        for (auto [right, left, id] : queries) {
            while (end < right && core_best.score != 0)
                add(ranks[end++], core_best);
            Answer best = core_best;
            if (right <= boundary) {
                for (int day = left; day < right; ++day)
                    add(ranks[day], best);
                active.clear();
            } else {
                if (suffix_best[left - start].score < best.score)
                    best = suffix_best[left - start];
                // Internal fringe pairs are precomputed; only cross pairs remain.
                for (int day = left; day < boundary; ++day) {
                    int rank = ranks[day];
                    if (potential[rank] >= best.score)
                        continue;
                    auto next = active.lower_bound(rank);
                    auto consider = [&](int other) {
                        int score = abs(values[rank] + values[other]);
                        if (score < best.score)
                            best = {score, order[rank], order[other]};
                    };
                    if (next != active.begin())
                        consider(*prev(next));
                    if (next != active.end())
                        consider(*next);
                }
            }
            answers[id] = minmax(best.first + 1, best.second + 1);
        }
    }
    for (auto [first, second] : answers)
        cout << first << ' ' << second << '\n';
}
