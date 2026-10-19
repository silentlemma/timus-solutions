#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

constexpr int TREE_FACTOR = 4;

std::pair<std::vector<int>, std::vector<int>> radii(const std::string &s, int odd_cap,
                                                    int even_cap) {
    int n = static_cast<int>(s.size());
    std::vector<int> odd(n), even(n);
    int left = 0, right = -1;
    for (int i = 0; i < n; ++i) {
        int d = i > right ? 1 : std::min(odd[left + right - i], right - i + 1);
        while (d < odd_cap && i >= d && i + d < n && s[i - d] == s[i + d])
            ++d;
        odd[i] = d;
        if (i + d - 1 > right) {
            left = i - d + 1;
            right = i + d - 1;
        }
    }
    left = 0;
    right = -1;
    for (int i = 0; i < n; ++i) {
        int d = i > right ? 0 : std::min(even[left + right - i + 1], right - i + 1);
        while (d < even_cap && i > d && i + d < n && s[i - d - 1] == s[i + d])
            ++d;
        even[i] = d;
        if (i + d - 1 > right) {
            left = i - d;
            right = i + d - 1;
        }
    }
    return {std::move(odd), std::move(even)};
}

struct Characters {
    int n;
    std::vector<char> tag;
    explicit Characters(const std::string &s)
        : n(static_cast<int>(s.size())), tag(TREE_FACTOR * n) {
        build(1, 0, n, s);
    }
    void build(int v, int a, int b, const std::string &s) {
        if (b - a == 1) {
            tag[v] = s[a];
            return;
        }
        int mid = (a + b) / 2;
        build(2 * v, a, mid, s);
        build(2 * v + 1, mid, b, s);
        if (tag[2 * v] == tag[2 * v + 1])
            tag[v] = tag[2 * v];
    }
    void assign(int v, int a, int b, int left, int right, char c) {
        if (left <= a && b <= right) {
            tag[v] = c;
            return;
        }
        int mid = (a + b) / 2;
        if (tag[v]) {
            tag[2 * v] = tag[2 * v + 1] = tag[v];
            tag[v] = 0;
        }
        if (left < mid)
            assign(2 * v, a, mid, left, right, c);
        if (mid < right)
            assign(2 * v + 1, mid, b, left, right, c);
        if (tag[2 * v] == tag[2 * v + 1])
            tag[v] = tag[2 * v];
    }
    void extract(int v, int a, int b, int left, int right, std::string &out) const {
        if (tag[v]) {
            out.append(std::min(b, right) - std::max(a, left), tag[v]);
            return;
        }
        int mid = (a + b) / 2;
        if (left < mid)
            extract(2 * v, a, mid, left, right, out);
        if (mid < right)
            extract(2 * v + 1, mid, b, left, right, out);
    }
    std::string extract(int left, int right) const {
        std::string out;
        out.reserve(right - left);
        extract(1, 0, n, left, right, out);
        return out;
    }
};

struct Counts {
    int n;
    std::vector<int> total;
    std::vector<std::uint8_t> tag;
    explicit Counts(const std::vector<int> &values)
        : n(static_cast<int>(values.size())), total(TREE_FACTOR * n), tag(TREE_FACTOR * n) {
        build(1, 0, n, values);
    }
    void build(int v, int a, int b, const std::vector<int> &values) {
        if (b - a == 1) {
            total[v] = values[a];
            tag[v] = values[a] + 1;
            return;
        }
        int mid = (a + b) / 2;
        build(2 * v, a, mid, values);
        build(2 * v + 1, mid, b, values);
        pull(v);
    }
    void pull(int v) {
        total[v] = total[2 * v] + total[2 * v + 1];
        tag[v] = tag[2 * v] == tag[2 * v + 1] ? tag[2 * v] : 0;
    }
    void replace(int v, int a, int b, int left, int right, int value,
                 const std::vector<int> &values) {
        if ((value >= 0 && left <= a && b <= right) || b - a == 1) {
            int chosen = value >= 0 ? value : values[a - left];
            total[v] = (b - a) * chosen;
            tag[v] = chosen + 1;
            return;
        }
        int mid = (a + b) / 2;
        if (tag[v]) {
            total[2 * v] = (mid - a) * (tag[v] - 1);
            total[2 * v + 1] = (b - mid) * (tag[v] - 1);
            tag[2 * v] = tag[2 * v + 1] = tag[v];
            tag[v] = 0;
        }
        if (left < mid)
            replace(2 * v, a, mid, left, right, value, values);
        if (mid < right)
            replace(2 * v + 1, mid, b, left, right, value, values);
        pull(v);
    }
    int query(int v, int a, int b, int left, int right) const {
        if (left <= a && b <= right)
            return total[v];
        if (tag[v])
            return (tag[v] - 1) * (std::min(b, right) - std::max(a, left));
        int mid = (a + b) / 2, answer = 0;
        if (left < mid)
            answer += query(2 * v, a, mid, left, right);
        if (mid < right)
            answer += query(2 * v + 1, mid, b, left, right);
        return answer;
    }
};

struct Solver {
    int n, k, odd_cap, even_cap;
    Characters characters;
    Counts counts;
    static std::vector<int> initial(const std::string &s, int k) {
        auto both = radii(s, (k + 1) / 2, k / 2);
        for (std::size_t i = 0; i < s.size(); ++i)
            both.first[i] += both.second[i];
        return std::move(both.first);
    }
    Solver(const std::string &s, int limit)
        : n(static_cast<int>(s.size())), k(limit), odd_cap((k + 1) / 2), even_cap(k / 2),
          characters(s), counts(initial(s, k)) {}
    void repair(int left, int right) {
        if (left > right)
            return;
        int start = std::max(0, left - even_cap);
        int end = std::min(n, right + odd_cap);
        auto both = radii(characters.extract(start, end), odd_cap, even_cap);
        std::vector<int> values;
        for (int i = left; i <= right; ++i)
            values.push_back(both.first[i - start] + both.second[i - start]);
        counts.replace(1, 0, n, left, right + 1, -1, values);
    }
    void assign(int left, int right, char c) {
        characters.assign(1, 0, n, left, right + 1, c);
        int a = std::max(0, left - odd_cap + 1), b = std::min(n - 1, right + even_cap);
        int x = left + even_cap, y = right - odd_cap + 1;
        if (x <= y) {
            counts.replace(1, 0, n, x, y + 1, k, {});
            repair(a, x - 1);
            repair(y + 1, b);
        } else {
            repair(a, b);
        }
    }
    int partial(int left, int right, int first, int last) const {
        auto both = radii(characters.extract(left, right), odd_cap, even_cap);
        int answer = 0;
        for (int i = first; i < last; ++i)
            answer += both.first[i] + both.second[i];
        return answer;
    }
    int query(int left, int right) const {
        int length = right - left + 1;
        if (length < k)
            return partial(left, right + 1, 0, length);
        int answer = counts.query(1, 0, n, left + even_cap, right - odd_cap + 2);
        if (even_cap)
            answer += partial(left, left + k - 1, 0, even_cap);
        if (odd_cap > 1)
            answer += partial(right - k + 2, right + 1, even_cap, k - 1);
        return answer;
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string text;
    int k, queries;
    std::cin >> text >> k >> queries;
    Solver solver(text, k);
    while (queries--) {
        int type, left, right;
        std::cin >> type >> left >> right;
        --left;
        --right;
        if (type == 1) {
            char c;
            std::cin >> c;
            solver.assign(left, right, c);
        } else {
            std::cout << solver.query(left, right) << '\n';
        }
    }
}
