#include <algorithm>
#include <iostream>
#include <tuple>
#include <vector>

using namespace std;

using Count = unsigned __int128;
using Integer = long long;

constexpr int MAX_CARDS = 100;
constexpr Integer MOD = 1'000'000'007;

Integer power(Integer base, Integer exponent) {
    Integer result = 1;
    while (exponent > 0) {
        if (exponent % 2 == 1) {
            result = result * base % MOD;
        }
        base = base * base % MOD;
        exponent /= 2;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int colors, drawn;
    if (!(cin >> colors >> drawn)) {
        return 0;
    }
    vector<int> total(colors + 1), shown(colors + 1), remaining(colors + 1);
    for (int &value : total) {
        cin >> value;
    }
    int unseen = 0;
    for (int color = 0; color <= colors; ++color) {
        cin >> shown[color];
        remaining[color] = total[color] - shown[color];
        unseen += remaining[color];
    }
    int required, revealed;
    cin >> required >> revealed;
    const int deck = unseen - drawn;

    vector<vector<Count>> choose(MAX_CARDS + 1, vector<Count>(MAX_CARDS + 1));
    vector<vector<Integer>> binomial(MAX_CARDS + 1, vector<Integer>(MAX_CARDS + 1));
    for (int n = 0; n <= MAX_CARDS; ++n) {
        choose[n][0] = 1;
        binomial[n][0] = 1;
        for (int r = 1; r <= n; ++r) {
            choose[n][r] = choose[n - 1][r - 1] + choose[n - 1][r];
            binomial[n][r] = static_cast<Integer>(choose[n][r] % MOD);
        }
    }

    vector<vector<Count>> ways(deck + 1, vector<Count>(revealed + 1));
    for (int matching = 0; matching <= deck; ++matching) {
        Count prefix = 0;
        for (int limit = 0; limit <= revealed; ++limit) {
            prefix += choose[matching][limit] * choose[deck - matching][revealed - limit];
            ways[matching][limit] = prefix;
        }
    }

    Integer answer = 0;
    const int other = unseen - remaining[0];
    const int first = max(0, drawn - other);
    const int last = min(remaining[0], drawn);
    for (int wild = first; wild <= last; ++wild) {
        const int need = drawn - wild;
        auto score = [&](int color, int count) -> Count {
            const int hand = shown[0] + wild + shown[color] + count;
            const int matching = total[0] + total[color] - hand;
            if (matching > deck || hand < required) {
                return 0;
            }
            return ways[matching][min(revealed, hand - required)];
        };

        Count baseline = 0;
        for (int color = 1; color <= colors; ++color) {
            baseline = max(baseline, score(color, 0));
        }
        vector<tuple<Count, int, int>> events;
        for (int color = 1; color <= colors; ++color) {
            for (int count = 1; count <= min(remaining[color], need); ++count) {
                events.emplace_back(max(baseline, score(color, count)), color, count);
            }
        }
        sort(events.begin(), events.end());

        vector<Integer> dp(need + 1), quotient(need + 1);
        vector<int> cap(colors + 1);
        dp[0] = 1;
        Integer weighted = static_cast<Integer>(baseline % MOD) * dp[need] % MOD;
        for (const auto &[value, color, count] : events) {
            const Integer before = dp[need];
            const auto &factor = binomial[remaining[color]];
            // Divide out the old color factor, whose constant coefficient is one.
            for (int degree = 0; degree <= need - count; ++degree) {
                Integer coefficient = dp[degree];
                for (int part = 1; part <= min(cap[color], degree); ++part) {
                    coefficient -= factor[part] * quotient[degree - part] % MOD;
                    if (coefficient < 0) {
                        coefficient += MOD;
                    }
                }
                quotient[degree] = coefficient;
            }
            for (int degree = 0; degree <= need - count; ++degree) {
                dp[degree + count] += factor[count] * quotient[degree] % MOD;
                if (dp[degree + count] >= MOD) {
                    dp[degree + count] -= MOD;
                }
            }
            cap[color] = count;
            const Integer added = (dp[need] - before + MOD) % MOD;
            weighted += static_cast<Integer>(value % MOD) * added % MOD;
            if (weighted >= MOD) {
                weighted -= MOD;
            }
        }
        answer += binomial[remaining[0]][wild] * weighted % MOD;
        if (answer >= MOD) {
            answer -= MOD;
        }
    }

    const Integer denominator = binomial[unseen][drawn] * binomial[deck][revealed] % MOD;
    cout << answer * power(denominator, MOD - 2) % MOD << '\n';
}
