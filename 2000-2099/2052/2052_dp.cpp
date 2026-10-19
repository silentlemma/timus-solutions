#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

constexpr int DECIMAL_BASE = 10;
constexpr int MAX_DIGIT = DECIMAL_BASE - 1;
using Integer = long long;
using Tables = std::vector<std::vector<Integer>>;

Tables build_tables(int digits) {
    int maximum = MAX_DIGIT * digits;
    std::vector<Integer> ways(maximum + 1);
    ways[0] = 1;
    Tables prefix;
    for (int length = 0; length < digits; ++length) {
        std::vector<Integer> row(maximum + 1);
        Integer running = 0;
        for (int total = 0; total <= maximum; ++total) {
            running += ways[total];
            row[total] = running;
        }
        prefix.push_back(row);
        if (length + 1 == digits)
            break;
        std::vector<Integer> next_ways(maximum + 1);
        Integer window = 0;
        for (int total = 0; total <= maximum; ++total) {
            window += ways[total];
            if (total >= DECIMAL_BASE)
                window -= ways[total - DECIMAL_BASE];
            next_ways[total] = window;
        }
        ways = next_ways;
    }
    return prefix;
}

Integer count_leq(Integer value, int target, const Tables &prefix) {
    std::string digits = std::to_string(value);
    int maximum = static_cast<int>(prefix[0].size()) - 1, remaining = target;
    Integer result = 0;
    for (std::size_t position = 0; position < digits.size(); ++position) {
        int digit = digits[position] - '0';
        const auto &row = prefix[digits.size() - position - 1];
        if (digit && remaining >= 0) {
            result += row[std::min(maximum, remaining)];
            if (remaining >= digit)
                result -= row[std::min(maximum, remaining - digit)];
        }
        remaining -= digit;
        if (remaining < 0)
            return result;
    }
    return result + (remaining == 0);
}

int digit_sum(Integer value) {
    int total = 0;
    while (value) {
        total += static_cast<int>(value % DECIMAL_BASE);
        value /= DECIMAL_BASE;
    }
    return total;
}

int solve(Integer number) {
    int digits = static_cast<int>(std::to_string(number).size());
    Tables prefix = build_tables(digits);
    Integer lower = 0;
    int answer = 0;
    for (int target = 1; target <= MAX_DIGIT * digits; ++target) {
        Integer count = count_leq(number, target, prefix);
        if (count == 0)
            continue;
        Integer start = lower + 1, left = start, right = lower + count;
        while (left <= right) {
            Integer middle = (left + right) / 2;
            if (middle - count_leq(middle, target, prefix) <= lower)
                left = middle + 1;
            else
                right = middle - 1;
        }
        if (right >= start && digit_sum(right) == target &&
            right - count_leq(right, target, prefix) == lower)
            ++answer;
        lower += count;
    }
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    Integer number;
    std::cin >> number;
    std::cout << solve(number) << '\n';
}
