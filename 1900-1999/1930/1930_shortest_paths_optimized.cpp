#include <cstdio>
#include <deque>
#include <vector>

int minimumChanges(const std::vector<std::vector<int>> &adjacency, int start, int target) {
    const int stateCount = 2 * static_cast<int>(adjacency.size());
    std::vector<int> distance(stateCount, stateCount);
    std::vector<bool> settled(stateCount, false);
    const int first = 2 * start;
    distance[first] = distance[first + 1] = 0;
    std::deque<int> queue{first, first + 1};
    while (!queue.empty()) {
        const int state = queue.front();
        queue.pop_front();
        if (settled[state]) {
            continue;
        }
        settled[state] = true;
        const int city = state / 2;
        const int gear = state & 1;
        if (city == target) {
            return distance[state];
        }
        for (const int nextState : adjacency[city]) {
            const int cost = (nextState & 1) != gear;
            const int candidate = distance[state] + cost;
            if (candidate < distance[nextState]) {
                distance[nextState] = candidate;
                if (cost == 0) {
                    queue.push_front(nextState);
                } else {
                    queue.push_back(nextState);
                }
            }
        }
    }
    return -1;
}

const int INPUT_BUFFER = 4096;
// refilling this small buffer keeps memory independent of the input size.
int nextInt() {
    static char buffer[INPUT_BUFFER];
    static int position = 0, size = 0;
    auto read = [&]() -> int {
        if (position == size) {
            size = static_cast<int>(std::fread(buffer, 1, INPUT_BUFFER, stdin));
            position = 0;
            if (size == 0)
                return EOF;
        }
        return buffer[position++];
    };
    int c = read();
    while (c != EOF && c != '-' && (c < '0' || c > '9'))
        c = read();
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = read();
    }
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value * sign;
}

int main() {
    int count, roads;
    count = nextInt();
    roads = nextInt();
    std::vector<std::vector<int>> adjacency(count);
    for (int i = 0; i < roads; ++i) {
        int lower, upper;
        lower = nextInt();
        upper = nextInt();
        --lower;
        --upper;
        adjacency[lower].push_back(2 * upper);
        adjacency[upper].push_back(2 * lower + 1);
    }
    int start, target;
    start = nextInt();
    target = nextInt();
    std::printf("%d\n", minimumChanges(adjacency, start - 1, target - 1));
    return 0;
}
