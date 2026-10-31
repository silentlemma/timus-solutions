#include <cstdio>

const int MAX_CITIES = 100, MAX_COST = 100000, BUFFER_SIZE = 4096;

int read_number() {
    // this buffer is refilled, so its size does not limit the input length.
    static char data[BUFFER_SIZE];
    static int at = 0, size = 0;
    int value = 0;
    bool started = false;
    while (true) {
        if (at == size) {
            size = static_cast<int>(fread(data, 1, BUFFER_SIZE, stdin));
            at = 0;
            if (size == 0)
                return value;
        }
        int c = data[at++];
        if (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            started = true;
        } else if (started) {
            return value;
        }
    }
}

int main() {
    int n = read_number(), k = read_number();
    // n <= 100 and costs <= 100000; even 99 purchased edges fit a signed int.
    static int cost[MAX_CITIES][MAX_CITIES];
    int best[MAX_CITIES];
    bool used[MAX_CITIES] = {};
    // every cost is at most MAX_COST, so MAX_COST + 1 works as infinity
    for (int i = 0; i < n; ++i)
        best[i] = MAX_COST + 1;
    for (int i = 0; i < k; ++i)
        best[read_number() - 1] = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cost[i][j] = read_number();
    int answer = 0;
    for (int step = 0; step < n; ++step) {
        int vertex = -1;
        for (int v = 0; v < n; ++v)
            if (!used[v] && (vertex < 0 || best[v] < best[vertex]))
                vertex = v;
        answer += best[vertex];
        used[vertex] = true;
        for (int v = 0; v < n; ++v)
            if (!used[v] && cost[vertex][v] < best[v])
                best[v] = cost[vertex][v];
    }
    printf("%d\n", answer);
}
