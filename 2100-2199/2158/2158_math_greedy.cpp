#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using Value = long long;
using Sequence = std::vector<Value>;
using Answer = std::pair<Sequence, Sequence>;

constexpr int MAX_GEOMETRIC = 30;
constexpr int SEED_LIMIT = MAX_GEOMETRIC + 2;
constexpr int MAJORITY_SIZE = 2 * (2 * MAX_GEOMETRIC + 1);

bool is_arithmetic(const Sequence &values) {
    for (std::size_t i = 2; i < values.size(); ++i) {
        if (values[i] - values[i - 1] != values[1] - values[0]) {
            return false;
        }
    }
    return true;
}

bool is_geometric(const Sequence &values) {
    if (values.empty()) {
        return false;
    }
    if (values[0] == 0) {
        return values.back() == 0;
    }
    for (std::size_t i = 2; i < values.size(); ++i) {
        if (values[i] * values[0] != values[i - 1] * values[1]) {
            return false;
        }
    }
    return true;
}

Answer extract(const Sequence &values, Value start, Value step) {
    Sequence arithmetic;
    Sequence geometric;
    arithmetic.reserve(values.size());
    geometric.reserve(MAX_GEOMETRIC + 2);
    Value expected = start;
    for (Value value : values) {
        if (value == expected) {
            arithmetic.push_back(value);
            expected += step;
        } else {
            geometric.push_back(value);
            if (geometric.size() > MAX_GEOMETRIC) {
                return {};
            }
        }
    }
    // Three distinct geometric terms cannot form an arithmetic progression.
    for (int removed = 0; removed <= 2; ++removed) {
        if (!arithmetic.empty() && is_geometric(geometric)) {
            return {std::move(arithmetic), std::move(geometric)};
        }
        if (removed == 2 || arithmetic.size() <= 1) {
            break;
        }
        Value value = arithmetic.back();
        arithmetic.pop_back();
        geometric.insert(std::upper_bound(geometric.begin(), geometric.end(), value), value);
    }
    return {};
}

Answer solve(Sequence &values) {
    std::sort(values.begin(), values.end());
    Sequence distinct;
    Sequence repeated;
    for (std::size_t i = 0; i < values.size(); ++i) {
        if (i == 0 || values[i] != values[i - 1]) {
            distinct.push_back(values[i]);
        } else if (i == 1 || values[i] != values[i - 2]) {
            repeated.push_back(values[i]);
        }
    }
    if (distinct.size() == 1) {
        return {Sequence(values.begin(), values.begin() + 1),
                Sequence(values.begin() + 1, values.end())};
    }
    if (distinct.size() == 2) {
        auto cut = std::upper_bound(values.begin(), values.end(), values[0]);
        return {Sequence(values.begin(), cut), Sequence(cut, values.end())};
    }
    if (repeated.size() == 1) {
        Value constant = repeated[0];
        int copies = 0;
        Sequence other;
        for (Value value : values) {
            if (value == constant) {
                ++copies;
            } else {
                other.push_back(value);
            }
        }
        for (int moved = 0; moved < 2; ++moved) {
            Sequence rest = other;
            if (moved != 0) {
                rest.insert(std::upper_bound(rest.begin(), rest.end(), constant), constant);
            }
            Sequence equal(copies - moved, constant);
            if (is_geometric(rest)) {
                return {std::move(equal), std::move(rest)};
            }
            if (is_arithmetic(rest)) {
                return {std::move(rest), std::move(equal)};
            }
        }
    }
    if (values.size() <= MAX_GEOMETRIC + 1) {
        for (std::size_t i = 0; i < values.size(); ++i) {
            Sequence rest = values;
            rest.erase(rest.begin() + i);
            if (is_geometric(rest)) {
                return {{values[i]}, std::move(rest)};
            }
        }
    }
    if (values.size() >= MAJORITY_SIZE) {
        Sequence gaps;
        gaps.reserve(values.size() - 1);
        for (std::size_t i = 1; i < values.size(); ++i) {
            gaps.push_back(values[i] - values[i - 1]);
        }
        std::sort(gaps.begin(), gaps.end());
        Value step = gaps[gaps.size() / 2];
        if (step != 0) {
            for (int i = 0; i <= MAX_GEOMETRIC; ++i) {
                Answer answer = extract(values, values[i], step);
                if (!answer.first.empty()) {
                    return answer;
                }
            }
        }
    } else {
        int limit = std::min(static_cast<int>(values.size()), SEED_LIMIT);
        for (int i = 0; i < limit; ++i) {
            for (int j = i + 1; j < limit; ++j) {
                Value step = values[j] - values[i];
                if (step != 0) {
                    Answer answer = extract(values, values[i], step);
                    if (!answer.first.empty()) {
                        return answer;
                    }
                }
            }
        }
    }
    return {};
}

void print_sequence(const Sequence &values) {
    for (std::size_t i = 0; i < values.size(); ++i) {
        if (i != 0) {
            std::cout << ' ';
        }
        std::cout << values[i];
    }
    std::cout << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size;
    if (!(std::cin >> size)) {
        return 0;
    }
    Sequence values(size);
    for (Value &value : values) {
        std::cin >> value;
    }
    Answer answer = solve(values);
    if (answer.first.empty()) {
        std::cout << -1 << '\n';
        return 0;
    }
    std::cout << answer.first.size() << '\n';
    print_sequence(answer.first);
    print_sequence(answer.second);
}
