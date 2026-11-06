#include <cstdio>

constexpr int MAX_ROOMS = 100;
enum Edge : signed char { absent, unused, outward, inward };
static int count[MAX_ROOMS + 1][MAX_ROOMS + 1];
static Edge edge[MAX_ROOMS + 1][MAX_ROOMS + 1];
static int cursor[MAX_ROOMS + 1];

int main() {
    int rooms;
    if (std::scanf("%d", &rooms) != 1)
        return 0;
    const int dummy = rooms;
    for (int room = 0; room < rooms; ++room) {
        int degree;
        std::scanf("%d", &degree);
        for (int i = 0; i < degree; ++i) {
            int other;
            std::scanf("%d", &other);
            ++count[room][other - 1];
        }
        if (degree % 2 != 0)
            edge[room][dummy] = edge[dummy][room] = unused;
        for (int other = 0; other < rooms; ++other)
            if (other != room && count[room][other] % 2 != 0)
                edge[room][other] = unused;
    }
    // Even multiplicities cancel. In the remaining even-degree graph each walk closes.
    for (int start = 0; start <= dummy; ++start) {
        int room = start;
        for (;;) {
            int &other = cursor[room];
            while (other <= dummy && edge[room][other] != unused)
                ++other;
            if (other > dummy)
                break;
            edge[room][other] = outward;
            edge[other][room] = inward;
            room = other;
        }
    }
    for (int room = 0; room < rooms; ++room) {
        bool space = false;
        for (int other = 0; other < rooms; ++other) {
            const int doors = count[room][other];
            const int green = doors / 2 + (edge[room][other] == outward);
            for (int i = 0; i < doors; ++i) {
                if (space)
                    std::putchar(' ');
                std::putchar(i < green ? 'G' : 'Y');
                space = true;
            }
        }
        std::putchar('\n');
    }
}
