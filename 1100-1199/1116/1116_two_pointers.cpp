#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

struct Piece {
    int a, b, y;
};

std::vector<Piece> read() {
    int n;
    std::vector<Piece> f;
    if (scanf("%d", &n) != 1)
        return f;
    f.resize(n);
    for (auto &p : f)
        scanf("%d %d %d", &p.a, &p.b, &p.y);
    return f;
}

int main() {
    std::vector<Piece> first = read(), second = read(), out;
    size_t j = 0;
    for (const auto &p : first) {
        int cur = p.a;
        // walk through [a, b) and keep what no interval of the second covers
        while (cur < p.b) {
            while (j < second.size() && second[j].b <= cur)
                j++;
            if (j < second.size() && second[j].a <= cur) {
                cur = second[j].b;
                continue;
            }
            int end = j < second.size() ? std::min(p.b, second[j].a) : p.b;
            out.push_back({cur, end, p.y});
            cur = end;
        }
    }
    std::string s = std::to_string(out.size());
    for (const auto &p : out)
        s += " " + std::to_string(p.a) + " " + std::to_string(p.b) + " " + std::to_string(p.y);
    puts(s.c_str());
}
