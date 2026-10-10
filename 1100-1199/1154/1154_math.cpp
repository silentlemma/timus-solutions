#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <string>

const int MINUTE = 60, HOUR = MINUTE * MINUTE, DAY = 24 * HOUR;
const std::string ELEMENTS = "AEFW";
// values closer than this are taken as equal
const double EPS = 1e-9;

struct Element {
    int strong, top, weak, low;
};

int seconds(const std::string &text) {
    int h, m, s;
    sscanf(text.c_str(), "%d:%d:%d", &h, &m, &s);
    return h * HOUR + m * MINUTE + s;
}

// the power falls linearly from the strong moment to the weak one and rises
// back over the rest of the day
double power(const Element &e, int t) {
    int fall = ((e.weak - e.strong) % DAY + DAY) % DAY;
    int since = ((t - e.strong) % DAY + DAY) % DAY;
    if (since <= fall)
        return e.top + double(e.low - e.top) * since / fall;
    return e.low + double(e.top - e.low) * (since - fall) / (DAY - fall);
}

int main() {
    std::map<char, Element> moments;
    for (size_t k = 0; k < ELEMENTS.size(); k++) {
        std::string code, strong, weak;
        int top, low;
        std::cin >> code >> strong >> top >> weak >> low;
        moments[code[0]] = {seconds(strong), top, seconds(weak), low};
    }
    std::string light, dark;
    std::cin >> light >> dark;
    std::map<char, int> side;
    for (char c : light)
        side[c]++;
    for (char c : dark)
        side[c]--;
    auto advantage = [&](int t) {
        double sum = 0;
        for (char e : ELEMENTS)
            if (side[e])
                sum += side[e] * power(moments[e], t);
        return sum;
    };
    // the advantage is linear between the moments, so its largest value over
    // the day is at a moment or at either end of the day
    std::set<int> times = {0, DAY - 1};
    for (auto &[code, e] : moments)
        times.insert({e.strong, e.weak});
    int when = -1;
    double best = 0;
    for (int t : times)
        if (when < 0 || advantage(t) > best + EPS) {
            best = advantage(t);
            when = t;
        }
    if (best <= EPS)
        puts("We can't win!");
    else
        printf("%02d:%02d:%02d\n%.2f\n", when / HOUR, when / MINUTE % MINUTE, when % MINUTE, best);
}
