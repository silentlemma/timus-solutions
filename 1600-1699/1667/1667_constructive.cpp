#include <algorithm>
#include <cstdio>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>

typedef long long ll;
const ll ROOT_LIMIT = 316227766;  // the largest integer whose square is at most 10^17
const int LEGS = 40;  // Pythagorean pairs from m^2 - n^2 and 2mn with n < m < LEGS

const int STARTS = 30;  // first terms of the arithmetic sequences
const int STEPS = 6;  // their differences
const int OFFSETS = 30;  // where the runs of consecutive primes start
const int PRIMES = 80;
const int HALF = 32;  // a reduced fraction x / y is stored as x << HALF | y

struct List {
    std::vector<ll> nums;
    std::vector<ll> ratios;  // sorted reduced fractions x / y < 1
    ll top;
};

// with S the sum of u^2 over u_1..u_k, the numbers 2u_1, ..., 2u_k and S - 1
// have squares adding up to (S + 1)^2; empty if they repeat
std::vector<ll> fromUs(const std::vector<ll>& us) {
    ll total = 0;
    std::vector<ll> nums;
    for (ll u : us) {
        total += u * u;
        nums.push_back(2 * u);
    }
    nums.push_back(total - 1);
    if (std::set<ll>(nums.begin(), nums.end()).size() != nums.size()) {
        return {};
    }
    return nums;
}

List makeList(const std::vector<ll>& nums) {
    List list{nums, {}, *std::max_element(nums.begin(), nums.end())};
    for (ll x : nums) {
        for (ll y : nums) {
            if (x < y) {
                ll g = std::gcd(x, y);
                list.ratios.push_back((x / g) << HALF | (y / g));
            }
        }
    }
    std::sort(list.ratios.begin(), list.ratios.end());
    return list;
}

// lists of distinct positive integers whose squares add up to a square,
// smallest maximum first
std::vector<List> lists(int size, const std::vector<ll>& primes) {
    std::vector<std::vector<ll>> found;
    if (size == 1) {
        found.push_back({1});
    } else if (size == 2) {
        for (ll m = 2; m < LEGS; m++) {
            for (ll n = 1; n < m; n++) {
                if (std::gcd(m, n) == 1 && (m - n) % 2 == 1) {
                    found.push_back({m * m - n * n, 2 * m * n});
                }
            }
        }
    } else {
        int k = size - 1;
        for (ll s = 1; s < STARTS; s++) {
            for (ll d = 1; d <= STEPS; d++) {
                std::vector<ll> us;
                for (int i = 0; i < k; i++) {
                    us.push_back(s + d * i);
                }
                found.push_back(fromUs(us));
            }
        }
        for (int off = 0; off < OFFSETS; off++) {
            auto first = primes.begin() + off;
            found.push_back(fromUs(std::vector<ll>(first, first + k)));
        }
    }
    std::vector<List> out;
    for (const auto& nums : found) {
        if (!nums.empty()) {
            out.push_back(makeList(nums));
        }
    }
    auto lower = [](const List& x, const List& y) { return x.top < y.top; };
    std::stable_sort(out.begin(), out.end(), lower);
    return out;
}

bool disjoint(const std::vector<ll>& x, const std::vector<ll>& y) {
    size_t i = 0, j = 0;
    while (i < x.size() && j < y.size()) {
        if (x[i] == y[j]) {
            return false;
        }
        x[i] < y[j] ? i++ : j++;
    }
    return true;
}

int main() {
    std::vector<ll> primes;
    for (ll n = 2; (int)primes.size() < PRIMES; n++) {
        bool prime = true;
        for (ll p : primes) {
            if (p * p > n) {
                break;
            }
            if (n % p == 0) {
                prime = false;
                break;
            }
        }
        if (prime) {
            primes.push_back(n);
        }
    }
    int t;
    scanf("%d", &t);
    std::map<int, std::vector<List>> pool;
    std::string out;
    for (int k = 0; k < t; k++) {
        int rows, cols;
        scanf("%d %d", &rows, &cols);
        for (int size : {rows, cols}) {
            if (!pool.count(size)) {
                pool[size] = lists(size, primes);
            }
        }
        // entry (i, j) is (a_i b_j)^2; two products a_i b_j and a_k b_l are
        // equal exactly when a_i / a_k = b_l / b_j, so no ratio may be shared
        const List *found = nullptr, *other = nullptr;
        ll smallest = pool[cols][0].top;
        for (const List& a : pool[rows]) {
            if (a.top * smallest > ROOT_LIMIT || found) {
                break;
            }
            for (const List& b : pool[cols]) {
                if (a.top * b.top > ROOT_LIMIT) {
                    break;
                }
                if (disjoint(a.ratios, b.ratios)) {
                    found = &a, other = &b;
                    break;
                }
            }
        }
        if (k > 0) {
            out += "\n";
        }
        if (!found) {
            out += "-1\n";
            continue;
        }
        for (ll x : found->nums) {
            for (size_t j = 0; j < other->nums.size(); j++) {
                ll v = x * other->nums[j];
                out += std::to_string(v * v) + (j + 1 < other->nums.size() ? " " : "\n");
            }
        }
    }
    printf("%s", out.c_str());
}
