#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <utility>
#include <vector>

constexpr int TEAM_COUNT = 4;
constexpr int WIN_POINTS = 3;
constexpr int OUTCOME_COUNT = 3;
constexpr int ORDER_COUNT = 24;
using Integer = std::int64_t;
using Order = std::array<int, TEAM_COUNT>;

struct Match {
    int a, b, c, d;
};
struct Row {
    std::vector<Integer> coefficients;
    Integer bound;
};

Integer floorDivide(Integer value, Integer divisor) {
    Integer quotient = value / divisor;
    if (value % divisor < 0)
        --quotient;
    return quotient;
}

bool simplify(std::vector<Row> &rows) {
    std::map<std::vector<Integer>, Integer> unique;
    for (const auto &row : rows) {
        Integer divisor = 0;
        for (Integer value : row.coefficients)
            divisor = std::gcd(divisor, value);
        if (divisor == 0) {
            if (row.bound < 0)
                return false;
            continue;
        }
        auto coefficients = row.coefficients;
        for (auto &value : coefficients)
            value /= divisor;
        const Integer bound = floorDivide(row.bound, divisor);
        auto found = unique.find(coefficients);
        if (found == unique.end())
            unique.emplace(std::move(coefficients), bound);
        else
            found->second = std::min(found->second, bound);
    }
    rows.clear();
    for (const auto &entry : unique)
        rows.push_back({entry.first, entry.second});
    return true;
}

bool integerFeasible(std::vector<Row> rows) {
    if (!simplify(rows))
        return false;
    while (!rows.empty()) {
        const int dimension = static_cast<int>(rows.front().coefficients.size());
        int column = -1, bestCost = std::numeric_limits<int>::max();
        for (int i = 0; i < dimension; ++i) {
            int positive = 0, negative = 0;
            bool unitUpper = true, unitLower = true;
            for (const auto &row : rows) {
                const auto value = row.coefficients[i];
                if (value > 0) {
                    ++positive;
                    unitUpper = unitUpper && value == 1;
                }
                if (value < 0) {
                    ++negative;
                    unitLower = unitLower && value == -1;
                }
            }
            if ((unitUpper || unitLower) && positive * negative < bestCost) {
                column = i;
                bestCost = positive * negative;
            }
        }
        std::vector<Row> projected;
        for (const auto &row : rows) {
            if (row.coefficients[column] == 0) {
                auto copy = row;
                copy.coefficients.erase(copy.coefficients.begin() + column);
                projected.push_back(std::move(copy));
            }
        }
        for (const auto &lower : rows)
            if (lower.coefficients[column] < 0) {
                for (const auto &upper : rows)
                    if (upper.coefficients[column] > 0) {
                        Row combined;
                        for (int i = 0; i < dimension; ++i)
                            if (i != column) {
                                combined.coefficients.push_back(
                                    upper.coefficients[column] * lower.coefficients[i] -
                                    lower.coefficients[column] * upper.coefficients[i]);
                            }
                        combined.bound = upper.coefficients[column] * lower.bound -
                                         lower.coefficients[column] * upper.bound;
                        projected.push_back(std::move(combined));
                    }
            }
        rows = std::move(projected);
        if (!simplify(rows))
            return false;
    }
    return true;
}

std::vector<Order> possibleOrders(const std::vector<Match> &matches) {
    std::array<int, TEAM_COUNT> initialPoints{};
    std::array<Integer, TEAM_COUNT> initialDifference{};
    std::array<std::array<bool, TEAM_COUNT>, TEAM_COUNT> played{};
    for (const auto &m : matches) {
        played[m.a][m.b] = true;
        initialDifference[m.a] += m.c - m.d;
        initialDifference[m.b] += m.d - m.c;
        if (m.c == m.d) {
            ++initialPoints[m.a];
            ++initialPoints[m.b];
        } else
            initialPoints[m.c > m.d ? m.a : m.b] += WIN_POINTS;
    }
    std::vector<std::pair<int, int>> remaining;
    for (int a = 0; a < TEAM_COUNT; ++a)
        for (int b = a + 1; b < TEAM_COUNT; ++b) {
            if (!played[a][b])
                remaining.emplace_back(a, b);
        }
    Order permutation{};
    std::iota(permutation.begin(), permutation.end(), 0);
    std::vector<Order> orders;
    do {
        orders.push_back(permutation);
    } while (std::next_permutation(permutation.begin(), permutation.end()));
    std::array<bool, ORDER_COUNT> found{};
    int foundCount = 0, patternCount = 1;
    for (std::size_t i = 0; i < remaining.size(); ++i)
        patternCount *= OUTCOME_COUNT;
    for (int pattern = 0; pattern < patternCount && foundCount < ORDER_COUNT; ++pattern) {
        int code = pattern;
        auto points = initialPoints;
        auto difference = initialDifference;
        std::vector<std::pair<int, int>> edges;
        for (auto pair : remaining) {
            const int outcome = code % OUTCOME_COUNT;
            code /= OUTCOME_COUNT;
            if (outcome == 0) {
                ++points[pair.first];
                ++points[pair.second];
            } else {
                const int winner = outcome == 1 ? pair.first : pair.second;
                const int loser = outcome == 1 ? pair.second : pair.first;
                points[winner] += WIN_POINTS;
                ++difference[winner];
                --difference[loser];
                edges.emplace_back(winner, loser);
            }
        }
        for (int index = 0; index < ORDER_COUNT; ++index) {
            if (found[index])
                continue;
            const auto &order = orders[index];
            bool compatible = true;
            for (int i = 0; i + 1 < TEAM_COUNT; ++i) {
                if (points[order[i]] < points[order[i + 1]])
                    compatible = false;
            }
            if (!compatible)
                continue;
            std::vector<Row> rows;
            for (std::size_t column = 0; column < edges.size(); ++column) {
                Row row{std::vector<Integer>(edges.size()), 0};
                row.coefficients[column] = -1;
                rows.push_back(std::move(row));
            }
            for (int i = 0; i + 1 < TEAM_COUNT; ++i) {
                const int a = order[i], b = order[i + 1];
                if (points[a] != points[b])
                    continue;
                Row row;
                for (auto edge : edges)
                    row.coefficients.push_back((edge.first == b) - (edge.second == b) -
                                               (edge.first == a) + (edge.second == a));
                row.bound = difference[a] - difference[b];
                rows.push_back(std::move(row));
            }
            if (integerFeasible(std::move(rows))) {
                found[index] = true;
                ++foundCount;
            }
        }
    }
    std::vector<Order> result;
    for (int i = 0; i < ORDER_COUNT; ++i)
        if (found[i])
            result.push_back(orders[i]);
    return result;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    if (!(std::cin >> n))
        return 0;
    std::vector<Match> matches(n);
    for (auto &m : matches) {
        std::cin >> m.a >> m.b >> m.c >> m.d;
        --m.a;
        --m.b;
    }
    const auto orders = possibleOrders(matches);
    std::cout << orders.size() << '\n';
    for (const auto &order : orders) {
        for (int i = 0; i < TEAM_COUNT; ++i)
            std::cout << order[i] + 1 << (i + 1 == TEAM_COUNT ? '\n' : ' ');
    }
}
