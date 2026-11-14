#include <cstdio>
#include <iterator>
#include <set>
#include <utility>
#include <vector>

constexpr int HEADER_FIELDS = 4;

struct Request {
    int start, next;
};

int main() {
    int stops, capacity, requests, price;
    if (scanf("%d %d %d %d", &stops, &capacity, &requests, &price) != HEADER_FIELDS)
        return 0;
    std::vector<int> firstAtEnd(stops + 1);
    std::vector<Request> trips(requests + 1);
    for (int id = 1; id <= requests; ++id) {
        int start, end;
        scanf("%d %d", &start, &end);
        trips[id] = {start, firstAtEnd[end]};
        firstAtEnd[end] = id;
    }

    std::multiset<int> seatEnds;
    for (int i = 0; i < capacity; ++i)
        seatEnds.insert(0);
    std::vector<int> chosen;
    chosen.reserve(requests);
    // Finish earlier trips first and use the latest seat that is already free.
    for (int end = 1; end <= stops; ++end) {
        for (int id = firstAtEnd[end]; id != 0; id = trips[id].next) {
            auto after = seatEnds.upper_bound(trips[id].start);
            if (after == seatEnds.begin())
                continue;
            auto seat = seatEnds.extract(std::prev(after));
            seat.value() = end;
            seatEnds.insert(std::move(seat));
            chosen.push_back(id);
        }
    }
    printf("%lld\n", static_cast<long long>(chosen.size()) * price);
    const char *separator = "";
    for (int id : chosen) {
        printf("%s%d", separator, id);
        separator = " ";
    }
    putchar('\n');
}
