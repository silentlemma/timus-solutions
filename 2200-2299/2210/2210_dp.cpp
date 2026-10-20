#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using Integer = long long;

constexpr int MAX_VALUE = 100;

struct Line {
    Integer slope;
    Integer intercept;
};

struct RichState {
    int day;
    int income;
    Integer money;
};

std::vector<Line> make_hull(std::vector<Line> lines) {
    std::sort(lines.begin(), lines.end(), [](const Line &a, const Line &b) {
        return std::make_pair(a.slope, a.intercept) < std::make_pair(b.slope, b.intercept);
    });
    std::vector<Line> hull;
    for (const Line &line : lines) {
        if (!hull.empty() && hull.back().slope == line.slope) {
            if (hull.back().intercept >= line.intercept) {
                continue;
            }
            hull.pop_back();
        }
        while (hull.size() >= 2) {
            const Line &a = hull[hull.size() - 2];
            const Line &b = hull.back();
            if ((a.intercept - b.intercept) * (line.slope - b.slope) <
                (b.intercept - line.intercept) * (b.slope - a.slope)) {
                break;
            }
            hull.pop_back();
        }
        hull.push_back(line);
    }
    return hull;
}

Integer maximum(const std::vector<Line> &hull, Integer day) {
    int left = 0;
    int right = static_cast<int>(hull.size()) - 1;
    while (left < right) {
        int middle = (left + right) / 2;
        const Line &a = hull[middle];
        const Line &b = hull[middle + 1];
        if (a.slope * day + a.intercept <= b.slope * day + b.intercept) {
            left = middle + 1;
        } else {
            right = middle;
        }
    }
    return hull[left].slope * day + hull[left].intercept;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count;
    std::cin >> count;
    std::vector<int> best(MAX_VALUE + 1, 0);
    for (int index = 0; index < count; ++index) {
        int cost, income;
        std::cin >> cost >> income;
        best[cost] = std::max(best[cost], income);
    }

    std::vector<std::pair<int, int>> options;
    int peak = 0;
    for (int cost = 1; cost <= MAX_VALUE; ++cost) {
        if (best[cost] > peak) {
            peak = best[cost];
            options.emplace_back(cost, peak);
        }
    }
    int cap = options.back().first;
    int top_income = options.back().second;
    int length = cap + 1;
    int state_count = cap + 2 * top_income + 1;
    std::vector<Integer> current(state_count, -1);
    current[0] = 0;
    std::vector<std::vector<Line>> work_events;
    std::vector<RichState> rich;
    int day = 0;
    while (std::any_of(current.begin(), current.end(), [](Integer money) { return money >= 0; })) {
        std::vector<Integer> following(state_count, -1);
        std::vector<Line> events;
        Integer greatest = -1;
        for (int income = state_count - 1; income >= 0; --income) {
            Integer money = current[income];
            if (money <= greatest) {
                continue;
            }
            greatest = money;
            if (income >= cap && money >= cap) {
                rich.push_back({day, income, money});
                continue;
            }
            Integer slope = income + 1;
            events.push_back({slope, money - slope * day});
            // Once every price is affordable, move the next purchase before any work.
            if (money < cap) {
                following[income] = std::max(following[income], money + income + 1);
            }
            for (const auto &option : options) {
                int cost = option.first;
                int extra = option.second;
                if (cost > money) {
                    break;
                }
                int target = income + extra;
                following[target] = std::max(following[target], money - cost + income);
            }
        }
        work_events.push_back(std::move(events));
        current = std::move(following);
        ++day;
    }

    int limit = static_cast<int>(work_events.size()) - 1 + length;
    std::vector<Integer> suffix(limit + 1, 0);
    for (int remaining = 0; remaining < limit; ++remaining) {
        Integer gain = 1;
        for (const auto &option : options) {
            gain = std::max(gain, static_cast<Integer>(option.second) * remaining - option.first);
        }
        suffix[remaining + 1] = suffix[remaining] + gain;
    }
    Integer correction =
        suffix[length] - static_cast<Integer>(top_income) * length * (length - 1) / 2;
    correction += static_cast<Integer>(cap) * length;

    std::vector<Integer> answers(limit + 1, 0);
    std::vector<Integer> work_best(state_count, 0);
    std::vector<bool> work_seen(state_count, false);
    for (int horizon = 0; horizon <= limit; ++horizon) {
        if (horizon < static_cast<int>(work_events.size())) {
            for (const Line &line : work_events[horizon]) {
                int slope = static_cast<int>(line.slope);
                if (!work_seen[slope] || line.intercept > work_best[slope]) {
                    work_seen[slope] = true;
                    work_best[slope] = line.intercept;
                }
            }
        }
        for (int slope = 0; slope < state_count; ++slope) {
            if (work_seen[slope]) {
                answers[horizon] =
                    std::max(answers[horizon], slope * Integer(horizon) + work_best[slope]);
            }
        }
    }

    std::vector<Line> lines;
    for (const RichState &state : rich) {
        for (int remaining = 0; remaining <= limit - state.day; ++remaining) {
            int horizon = state.day + remaining;
            Integer candidate = state.money + static_cast<Integer>(state.income) * remaining;
            candidate += suffix[remaining];
            answers[horizon] = std::max(answers[horizon], candidate);
        }
        Integer start = state.day;
        Integer slope = state.income - top_income * start;
        Integer intercept = state.money - state.income * start;
        intercept += top_income * start * (start + 1) / 2 + cap * start + correction;
        lines.push_back({slope, intercept});
    }
    std::vector<Line> rich_hull = make_hull(std::move(lines));
    lines.clear();
    for (int slope = 0; slope < state_count; ++slope) {
        if (work_seen[slope]) {
            lines.push_back({slope, work_best[slope]});
        }
    }
    std::vector<Line> work_hull = make_hull(std::move(lines));

    std::cin >> count;
    for (int index = 0; index < count; ++index) {
        Integer horizon;
        std::cin >> horizon;
        Integer answer;
        if (horizon <= limit) {
            answer = answers[horizon];
        } else {
            Integer common = top_income * horizon * (horizon - 1) / 2 - cap * horizon;
            answer = std::max(maximum(work_hull, horizon), common + maximum(rich_hull, horizon));
        }
        std::cout << answer << '\n';
    }
}
