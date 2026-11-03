#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <numeric>
#include <string>
#include <vector>

const uint32_t RADIX = 1000000000;
const int LIMB_DIGITS = 9, RATE_DIGITS = 2, DECIMAL_SCALE = 100;
const int BUFFER_SIZE = 4096;
char input[BUFFER_SIZE];
int position, available;

int read() {
    if (position == available) {
        available = fread(input, 1, BUFFER_SIZE, stdin);
        position = 0;
        if (!available)
            return -1;
    }
    return input[position++];
}

std::string token() {
    int c = read();
    while (c >= 0 && c <= ' ')
        c = read();
    std::string text;
    while (c > ' ') {
        text += char(c);
        c = read();
    }
    return text;
}

std::string scaled(std::string text, int places) {
    if (text[0] == '+')
        text.erase(0, 1);
    size_t dot = text.find('.');
    int fractional = dot == std::string::npos ? 0 : int(text.size() - dot - 1);
    if (dot != std::string::npos)
        text.erase(dot, 1);
    return text + std::string(places - fractional, '0');
}

struct Amount {
    std::vector<uint32_t> digits;

    Amount() : digits(1, 0) {}

    explicit Amount(const std::string &text) {
        for (int end = int(text.size()); end > 0; end -= LIMB_DIGITS) {
            int begin = std::max(0, end - LIMB_DIGITS);
            digits.push_back(std::stoul(text.substr(begin, end - begin)));
        }
        trim();
    }

    void trim() {
        while (digits.size() > 1 && digits.back() == 0)
            digits.pop_back();
    }

    bool zero() const { return digits.size() == 1 && digits[0] == 0; }

    bool operator<(const Amount &other) const {
        if (digits.size() != other.digits.size())
            return digits.size() < other.digits.size();
        return std::lexicographical_compare(digits.rbegin(), digits.rend(), other.digits.rbegin(),
                                            other.digits.rend());
    }

    void multiply(const Amount &value, uint32_t factor) {
        size_t count = value.digits.size();
        digits.resize(count + 2);
        uint64_t carry = 0;
        // A limb times rate/fee is below10^13, safely inside uint64.
        // Reading each old limb before writing also permits value==*this.
        for (size_t i = 0; i < count; i++) {
            carry += uint64_t(value.digits[i]) * factor;
            digits[i] = carry % RADIX;
            carry /= RADIX;
        }
        size_t size = count;
        while (carry) {
            digits[size++] = carry % RADIX;
            carry /= RADIX;
        }
        digits.resize(size);
        trim();
    }

    void subtract(const Amount &a, const Amount &b) {
        digits.resize(a.digits.size());
        uint64_t borrow = 0;
        for (size_t i = 0; i < a.digits.size(); i++) {
            uint64_t take = borrow + (i < b.digits.size() ? b.digits[i] : 0);
            if (a.digits[i] < take) {
                digits[i] = uint64_t(RADIX) + a.digits[i] - take;
                borrow = 1;
            } else {
                digits[i] = a.digits[i] - take;
                borrow = 0;
            }
        }
        trim();
    }
};

int root(std::vector<int> &parent, int v) {
    while (parent[v] != v) {
        parent[v] = parent[parent[v]];
        v = parent[v];
    }
    return v;
}

struct Edge {
    int from, to;
    uint32_t rate, fee;
};

int main() {
    int n = std::stoi(token()), m = std::stoi(token()), start = std::stoi(token()) - 1;
    std::string text = token();
    size_t dot = text.find('.');
    int places = std::max(RATE_DIGITS, dot == std::string::npos ? 0 : int(text.size() - dot - 1));
    Amount initial(scaled(text, places));
    // With nonnegative commissions, zero capital can never become positive.
    if (initial.zero()) {
        puts("NO");
        return 0;
    }
    Amount unit("1" + std::string(places - RATE_DIGITS, '0'));
    std::vector<int> parent(n);
    std::iota(parent.begin(), parent.end(), 0);
    std::vector<Edge> edges;
    edges.reserve(2 * m);
    for (int i = 0; i < m; i++) {
        int a = std::stoi(token()) - 1, b = std::stoi(token()) - 1;
        uint32_t rab = std::stoul(scaled(token(), RATE_DIGITS));
        uint32_t cab = std::stoul(scaled(token(), RATE_DIGITS));
        uint32_t rba = std::stoul(scaled(token(), RATE_DIGITS));
        uint32_t cba = std::stoul(scaled(token(), RATE_DIGITS));
        parent[root(parent, a)] = root(parent, b);
        edges.push_back({a, b, rab, cab});
        edges.push_back({b, a, rba, cba});
    }
    int component = root(parent, start), count = 0;
    std::vector<int> index(n, -1);
    for (int i = 0; i < n; i++)
        if (root(parent, i) == component)
            index[i] = count++;
    int kept = 0;
    for (Edge edge : edges)
        if (index[edge.from] >= 0) {
            edge.from = index[edge.from];
            edge.to = index[edge.to];
            edges[kept++] = edge;
        }
    edges.resize(kept);
    start = index[start];
    std::vector<Amount> best(count), after(count);
    std::vector<unsigned char> reached(count), next(count);
    best[start] = initial;
    reached[start] = 1;
    Amount cost, got;
    bool changed = false;
    // Jacobi passes use one exact common denominator. Never read after[from].
    // Only the source component matters, so count passes suffice for a cycle.
    for (int pass = 0; pass < count; pass++) {
        for (int i = 0; i < count; i++)
            if (reached[i])
                after[i].multiply(best[i], DECIMAL_SCALE);
        next = reached;
        changed = false;
        for (const Edge &edge : edges) {
            if (!reached[edge.from])
                continue;
            if (edge.fee == 0)
                got.multiply(best[edge.from], edge.rate);
            else {
                cost.multiply(unit, edge.fee);
                if (best[edge.from] < cost)
                    continue;
                got.subtract(best[edge.from], cost);
                got.multiply(got, edge.rate);
            }
            if (!next[edge.to] || after[edge.to] < got) {
                after[edge.to] = got;
                next[edge.to] = 1;
                changed = true;
            }
        }
        best.swap(after);
        reached.swap(next);
        unit.multiply(unit, DECIMAL_SCALE);
        initial.multiply(initial, DECIMAL_SCALE);
        if (initial < best[start] || !changed)
            break;
    }
    puts(initial < best[start] || changed ? "YES" : "NO");
}
