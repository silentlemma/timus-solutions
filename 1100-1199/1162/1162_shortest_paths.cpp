#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

// Nonnegative integers stored in base 100, with no rounding.
struct Amount {
    std::vector<int> digits;

    Amount(std::string text = "0") {
        for (int end = (int)text.size(); end > 0; end -= 2)
            digits.push_back(std::stoi(text.substr(std::max(0, end - 2), std::min(2, end))));
        trim();
    }

    void trim() {
        while (digits.size() > 1 && digits.back() == 0)
            digits.pop_back();
    }

    bool operator<(const Amount &other) const {
        if (digits.size() != other.digits.size())
            return digits.size() < other.digits.size();
        return std::lexicographical_compare(digits.rbegin(), digits.rend(),
                                            other.digits.rbegin(), other.digits.rend());
    }

    Amount operator*(int factor) const {
        Amount result;
        result.digits.clear();
        int carry = 0;
        for (int digit : digits) {
            carry += digit * factor;
            result.digits.push_back(carry % 100);
            carry /= 100;
        }
        while (carry) {
            result.digits.push_back(carry % 100);
            carry /= 100;
        }
        result.trim();
        return result;
    }

    Amount operator-(const Amount &other) const {
        Amount result = *this;
        int borrow = 0;
        for (size_t i = 0; i < digits.size(); i++) {
            int digit = digits[i] - borrow - (i < other.digits.size() ? other.digits[i] : 0);
            borrow = digit < 0;
            result.digits[i] = digit + borrow * 100;
        }
        result.trim();
        return result;
    }
};

std::string scaled(std::string text, int places) {
    size_t dot = text.find('.');
    int digits = dot == std::string::npos ? 0 : (int)(text.size() - dot - 1);
    if (dot != std::string::npos)
        text.erase(dot, 1);
    if (text[0] == '+' || text[0] == '-')
        text.erase(0, 1);
    return text + std::string(places - digits, '0');
}

struct Exchange {
    int from, to;
    int rate, fee;
};

int main() {
    int n, m, s;
    std::string text;
    if (!(std::cin >> n >> m >> s >> text))
        return 0;
    size_t dot = text.find('.');
    int places = std::max(2, dot == std::string::npos ? 0 : (int)(text.size() - dot - 1));
    Amount v(scaled(text, places)), unit("1" + std::string(places - 2, '0'));
    std::vector<Exchange> edges;
    for (int k = 0; k < m; k++) {
        int a, b;
        std::string rab, cab, rba, cba;
        if (!(std::cin >> a >> b >> rab >> cab >> rba >> cba))
            return 0;
        edges.push_back({a, b, std::stoi(scaled(rab, 2)), std::stoi(scaled(cab, 2))});
        edges.push_back({b, a, std::stoi(scaled(rba, 2)), std::stoi(scaled(cba, 2))});
    }
    // All amounts share an exact denominator, multiplied by 100 each pass.
    // A change on pass n means a reachable gaining cycle.
    std::vector<Amount> best(n + 1);
    std::vector<bool> reached(n + 1, false);
    best[s] = v;
    reached[s] = true;
    bool changed = false;
    for (int pass = 0; pass < n; pass++) {
        std::vector<Amount> after;
        for (const Amount &amount : best)
            after.push_back(amount * 100);
        std::vector<bool> next_reached = reached;
        changed = false;
        for (const Exchange &e : edges) {
            Amount cost = unit * e.fee;
            if (reached[e.from] && !(best[e.from] < cost)) {
                Amount got = (best[e.from] - cost) * e.rate;
                if (!next_reached[e.to] || after[e.to] < got) {
                    after[e.to] = got;
                    next_reached[e.to] = true;
                    changed = true;
                }
            }
        }
        best = after;
        reached = next_reached;
        unit = unit * 100;
        v = v * 100;
        if (v < best[s] || !changed)
            break;
    }
    std::cout << (v < best[s] || changed ? "YES\n" : "NO\n");
}
