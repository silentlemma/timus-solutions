#include <cstdio>
#include <vector>

struct Bus {
    long long ready, last;  // the first and the last minute it may enter
};

std::vector<Bus> readSide() {
    int count = 0;
    if (scanf("%d", &count) != 1) return {};
    std::vector<Bus> side(count);
    for (Bus &b : side) {
        long long t, p;
        if (scanf("%lld %lld", &t, &p) != 2) return {};
        b = {t, t + p - 1};
    }
    // a bus must enter before the next one on its side
    for (int i = count - 2; i >= 0; i--) {
        if (side[i].last > side[i + 1].last - 1) side[i].last = side[i + 1].last - 1;
    }
    return side;
}

int main() {
    std::vector<Bus> sides[2] = {readSide(), readSide()};
    size_t head[2] = {0, 0};
    long long now = 0;
    while (head[0] < sides[0].size() || head[1] < sides[1].size()) {
        // among the waiting front buses, the one with the earlier last minute
        int pick = -1;
        long long next = -1;
        for (int s = 0; s < 2; s++) {
            if (head[s] == sides[s].size()) continue;
            const Bus &b = sides[s][head[s]];
            if (next < 0 || b.ready < next) next = b.ready;
            if (b.ready <= now && (pick < 0 || b.last < sides[pick][head[pick]].last)) pick = s;
        }
        if (pick < 0) {
            now = next;
            continue;
        }
        if (now > sides[pick][head[pick]].last) {
            puts("NO");
            return 0;
        }
        head[pick]++;
        now++;
    }
    puts("YES");
    return 0;
}
