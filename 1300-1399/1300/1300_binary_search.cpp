#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

typedef long long ll;

const ll CENTS = 100;
const size_t DIGITS = 2;

std::vector<ll> limits, rates;
ll topRate, bonusRate;

// a non-negative amount with at most two decimals, in cents
ll cents(const std::string &token) {
    size_t dot = token.find('.');
    std::string whole = token.substr(0, dot), frac;
    if (dot != std::string::npos)
        frac = token.substr(dot + 1);
    frac = (frac + "00").substr(0, DIGITS);
    return (whole.empty() ? 0 : std::stoll(whole)) * CENTS + std::stoll(frac);
}

// rate percent of an amount in cents, rounded half up to a cent
ll percent(ll amount, ll rate) { return (amount * rate + CENTS / 2) / CENTS; }

ll tax(ll amount) {
    ll raw = 0, previous = 0;
    for (size_t i = 0; i < limits.size(); i++) {
        if (amount <= limits[i])
            return (raw + (amount - previous) * rates[i] + CENTS / 2) / CENTS;
        raw += (limits[i] - previous) * rates[i];
        previous = limits[i];
    }
    return (raw + (amount - previous) * topRate + CENTS / 2) / CENTS;
}

ll net(ll gross) {
    ll bonus = percent(gross, bonusRate);
    return gross - tax(gross) + bonus - tax(bonus);
}

// net never decreases as the salary grows, so the largest salary whose
// net does not exceed the amount paid is found by bisection
ll grossFor(ll amount) {
    ll lo = 0, hi = 1;
    while (net(hi) <= amount)
        hi *= 2;
    while (hi - lo > 1) {
        ll mid = (lo + hi) / 2;
        if (net(mid) <= amount) {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    return lo;
}

int main() {
    std::string token;
    if (!(std::cin >> bonusRate))
        return 0;
    while (std::cin >> token) {
        ll limit = cents(token), rate = 0;
        std::cin >> rate;
        if (limit == 0) {
            topRate = rate;
            break;
        }
        limits.push_back(limit);
        rates.push_back(rate);
    }
    ll total = 0, withheld = 0;
    while (std::cin >> token && token != "-1") {
        ll gross = grossFor(cents(token));
        total += gross;
        withheld += tax(gross) + tax(percent(gross, bonusRate));
    }
    ll owed = tax(total) + tax(percent(total, bonusRate)) - withheld;
    printf("%s%lld.%02lld\n", owed < 0 ? "-" : "", llabs(owed) / CENTS, llabs(owed) % CENTS);
    return 0;
}
