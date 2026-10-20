#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

constexpr int HORIZON = 25;
constexpr int ALPHABET_SIZE = 2;

class Solver {
    vector<int> text;
    vector<int> border{0};
    vector<int> rank{0};
    array<int, HORIZON + 1> answer{};
    int split;

    int append(int symbol) {
        int length = static_cast<int>(text.size());
        int matched = border[length];
        while (matched > 0 && text[matched] != symbol) {
            matched = border[matched];
        }
        if (length > 0 && text[matched] == symbol) {
            ++matched;
        }
        text.push_back(symbol);
        border.push_back(matched);
        int period = length + 1 - matched;
        int previous_period = matched - border[matched];
        // Equal minimal periods are consecutive along the border chain.
        rank.push_back(rank[matched] + (period != previous_period));
        return rank[matched];
    }

    void solve_tail(int score) {
        int length = static_cast<int>(text.size());
        int remaining = HORIZON - split;
        vector<array<int, ALPHABET_SIZE>> transition(length);
        for (int state = 0; state < length; ++state) {
            for (int symbol = 0; symbol < ALPHABET_SIZE; ++symbol) {
                if (text[state] == symbol) {
                    transition[state][symbol] = state + 1;
                } else if (state > 0) {
                    transition[state][symbol] = transition[border[state]][symbol];
                }
            }
        }

        vector<int> periods;
        int state = border[length];
        while (length - state <= remaining) {
            periods.push_back(length - state);
            if (state == 0) {
                break;
            }
            state = border[state];
        }

        vector<vector<pair<int, int>>> seeds(remaining + 1);
        // A border reaching the fixed prefix forces a short periodic continuation.
        for (int period : periods) {
            int path_score = score;
            for (int step = 1; step <= remaining; ++step) {
                int symbol = text[(length + step - 1) % period];
                int matched = border.back();
                if (matched >= length) {
                    int other = 1 - symbol;
                    while (matched >= length && text[matched] != other) {
                        matched = border[matched];
                    }
                    if (matched < length) {
                        matched = transition[matched][other];
                    } else {
                        ++matched;
                    }
                    if (matched < length) {
                        seeds[step].emplace_back(matched, path_score + rank[matched]);
                    }
                }
                path_score += append(symbol);
                answer[split + step] = max(answer[split + step], path_score);
            }
            text.resize(length);
            border.resize(length + 1);
            rank.resize(length + 1);
        }

        vector<int> best(length, -1);
        vector<int> next(length, -1);
        vector<int> active{border[length]};
        vector<int> next_active;
        best[border[length]] = score;
        for (int step = 1; step <= remaining; ++step) {
            next_active.clear();
            auto relax = [&](int target, int value) {
                if (next[target] < 0) {
                    next_active.push_back(target);
                }
                next[target] = max(next[target], value);
            };
            for (int current : active) {
                for (int symbol = 0; symbol < ALPHABET_SIZE; ++symbol) {
                    int target = transition[current][symbol];
                    if (target < length) {
                        relax(target, best[current] + rank[target]);
                    }
                }
            }
            for (const auto &seed : seeds[step]) {
                relax(seed.first, seed.second);
            }
            for (int current : active) {
                best[current] = -1;
            }
            best.swap(next);
            active.swap(next_active);
            for (int current : active) {
                answer[split + step] = max(answer[split + step], best[current]);
            }
        }
    }

    void search(int depth, int score) {
        if (depth == split) {
            solve_tail(score);
            return;
        }
        for (int symbol = 0; symbol < ALPHABET_SIZE; ++symbol) {
            int next_score = score + append(symbol);
            answer[depth + 1] = max(answer[depth + 1], next_score);
            search(depth + 1, next_score);
            text.pop_back();
            border.pop_back();
            rank.pop_back();
        }
    }

  public:
    void run(const string &input) {
        int score = 0;
        for (char symbol : input) {
            if (symbol == 'X' || symbol == '.') {
                score += append(symbol == 'X');
            }
        }
        int length = static_cast<int>(text.size());
        split = max(0, (HORIZON - length + 1) / 2);
        search(0, score);
        for (int step = 1; step <= HORIZON; ++step) {
            cout << answer[step] << '\n';
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string input;
    getline(cin, input);
    Solver solver;
    solver.run(input);
    return 0;
}
