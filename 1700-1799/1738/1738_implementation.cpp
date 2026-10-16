#include <cstdio>
#include <set>
#include <string>
#include <vector>

const int HEX_PINS = 1 << 16;
const int DIGITS = 4;
const int NIBBLE = 15;
const int BITS = 4;
const int BASE = 10;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<int> pins(n + 1);
    for (int i = 1; i <= n; i++) scanf("%x", &pins[i]);
    // differing hex digits of two pins: nonzero nibbles of their xor
    std::vector<int> differ(HEX_PINS, 0);
    for (int x = 1; x < HEX_PINS; x++) differ[x] = differ[x >> BITS] + ((x & NIBBLE) ? 1 : 0);
    long long count[DIGITS + 1] = {};
    size_t longest = std::to_string(n).size();
    for (int i = 1; i <= n; i++) {
        int pin = pins[i];
        // each pair is counted from its smaller number: a digit raised in
        // place, which never repeats a number, or a digit inserted
        for (int place = 1, rest = i; rest; place *= BASE, rest /= BASE) {
            for (int d = rest % BASE + 1; d < BASE; d++) {
                int j = i + (d - rest % BASE) * place;
                if (j > n) break;
                count[differ[pin ^ pins[j]]]++;
            }
        }
        std::string s = std::to_string(i);
        if (s.size() >= longest) continue;
        std::set<int> near;
        for (size_t p = 0; p <= s.size(); p++) {
            for (char d = '0'; d <= '9'; d++) {
                std::string t = s.substr(0, p) + d + s.substr(p);
                if (t[0] != '0') near.insert(std::stoi(t));
            }
        }
        for (int j : near) {
            if (j <= n) count[differ[pin ^ pins[j]]]++;
        }
    }
    for (int k = 1; k <= DIGITS; k++) printf("%lld%c", count[k], k < DIGITS ? ' ' : '\n');
}
