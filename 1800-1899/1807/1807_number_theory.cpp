#include <cmath>
#include <cstdio>
#include <string>
#include <vector>

// the best split of a prime p < 31623 never uses a prime above 700
const int BOUND = 1000;

int main() {
    long long n;
    if (scanf("%lld", &n) != 1) return 0;
    long long p = n;
    for (long long d = 2; d * d <= n; d++) {
        if (n % d == 0) {
            p = d;
            break;
        }
    }
    // the largest gcd is n / p: the pockets hold n/p times parts adding up
    // to p, and the lcm is n/p times the lcm of the parts. Parts that are
    // powers of distinct primes, padded with ones, give the best lcm
    long long unit = n / p;
    int cap = (int)p;
    std::vector<std::vector<int>> groups;
    std::vector<char> composite(BOUND, 0);
    for (int q = 2; q < BOUND && q < cap; q++) {
        if (composite[q]) continue;
        for (int m = q * q; m < BOUND; m += q) composite[m] = 1;
        std::vector<int> powers;
        for (long long w = q; w < cap; w *= q) powers.push_back((int)w);
        groups.push_back(powers);
    }
    // best[s]: the largest log of an lcm of parts with weight at most s
    std::vector<double> best(cap + 1, 0.0), next;
    std::vector<std::vector<unsigned char>> choices;
    for (const auto &powers : groups) {
        next = best;
        std::vector<unsigned char> choice(cap + 1, 0);
        for (size_t e = 0; e < powers.size(); e++) {
            int w = powers[e];
            double value = std::log((double)w);
            for (int s = w; s <= cap; s++) {
                double candidate = best[s - w] + value;
                if (candidate > next[s]) {
                    next[s] = candidate;
                    choice[s] = (unsigned char)(e + 1);
                }
            }
        }
        best.swap(next);
        choices.push_back(choice);
    }
    std::vector<long long> parts;
    int s = cap, used = 0;
    for (size_t g = groups.size(); g-- > 0;) {
        int e = choices[g][s];
        if (e) {
            parts.push_back(groups[g][e - 1]);
            s -= groups[g][e - 1];
            used += groups[g][e - 1];
        }
    }
    while (used < cap) {
        parts.push_back(1);
        used++;
    }
    std::string out;
    for (size_t i = 0; i < parts.size(); i++) {
        if (i > 0) out += ' ';
        out += std::to_string(parts[i] * unit);
    }
    puts(out.c_str());
    return 0;
}
