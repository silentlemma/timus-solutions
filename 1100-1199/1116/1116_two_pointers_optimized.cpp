#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>

struct Interval {
    std::int16_t start, end, value;
};

Interval read_interval() {
    Interval result;
    std::scanf("%hd%hd%hd", &result.start, &result.end, &result.value);
    return result;
}

int main() {
    int first_count;
    if (std::scanf("%d", &first_count) != 1)
        return 0;
    std::vector<Interval> first(first_count);
    for (auto &interval : first)
        interval = read_interval();
    int remaining;
    if (std::scanf("%d", &remaining) != 1)
        return 0;
    Interval mask = read_interval();
    --remaining;
    std::vector<Interval> result;
    result.reserve(first_count + remaining + 1);
    for (const auto &interval : first) {
        auto start = interval.start;
        while (start < interval.end) {
            while (remaining > 0 && mask.end <= start) {
                mask = read_interval();
                --remaining;
            }
            if (mask.start <= start && start < mask.end) {
                start = mask.end;
                continue;
            }
            const auto end = start < mask.start ? std::min(interval.end, mask.start) : interval.end;
            result.push_back({start, end, interval.value});
            start = end;
        }
    }
    std::printf("%zu", result.size());
    for (const auto &interval : result)
        std::printf(" %d %d %d", interval.start, interval.end, interval.value);
    std::puts("");
}
