#include <cstdint>
#include <cstdio>

constexpr int MAX_VERTICES = 100;
constexpr int INFINITY_DISTANCE = 32767;
constexpr int INPUT_BUFFER_SIZE = 4096;
constexpr int END_OF_INPUT = -1;

struct Input {
    unsigned char buffer[INPUT_BUFFER_SIZE];
    std::size_t position = 0, length = 0;

    int byte() {
        if (position == length) {
            length = std::fread(buffer, 1, sizeof buffer, stdin);
            position = 0;
            if (length == 0)
                return EOF;
        }
        return buffer[position++];
    }

    int number() {
        int digit = byte();
        while (digit != EOF && digit <= ' ')
            digit = byte();
        if (digit == '-' || digit == EOF)
            return END_OF_INPUT;
        int value = 0;
        while (digit >= '0' && digit <= '9') {
            value = value * 10 + digit - '0';
            digit = byte();
        }
        return value;
    }
};

int main() {
    Input input;
    for (int n = input.number(); n != END_OF_INPUT; n = input.number()) {
        std::uint16_t road[MAX_VERTICES][MAX_VERTICES];
        std::uint16_t dist[MAX_VERTICES][MAX_VERTICES];
        std::uint8_t next[MAX_VERTICES][MAX_VERTICES];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                road[i][j] = dist[i][j] = i == j ? 0 : INFINITY_DISTANCE;
                next[i][j] = j;
            }
        }
        const int roads = input.number();
        for (int i = 0; i < roads; ++i) {
            const int a = input.number() - 1;
            const int b = input.number() - 1;
            const int weight = input.number();
            if (weight < road[a][b])
                road[a][b] = road[b][a] = dist[a][b] = dist[b][a] = weight;
        }

        int best = INFINITY_DISTANCE;
        int cycle[MAX_VERTICES], count = 0;
        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < k; ++i) {
                if (road[k][i] >= best)
                    continue;
                for (int j = i + 1; j < k; ++j) {
                    const int length = road[k][i] + road[k][j] + dist[i][j];
                    if (length < best) {
                        best = length;
                        count = 0;
                        for (int v = i; v != j; v = next[v][j])
                            cycle[count++] = v;
                        cycle[count++] = j;
                        cycle[count++] = k;
                    }
                }
            }
            // Distances are symmetric. A path at least as long as the best
            // cycle cannot contribute to any shorter cycle with positive roads.
            for (int i = 0; i < n; ++i) {
                const int left = dist[k][i];
                if (i == k || left >= best)
                    continue;
                for (int j = i + 1; j < n; ++j) {
                    const int length = left + dist[k][j];
                    if (length < dist[i][j] && length < best) {
                        dist[i][j] = dist[j][i] = length;
                        next[i][j] = next[i][k];
                        next[j][i] = next[j][k];
                    }
                }
            }
        }
        if (count == 0)
            std::puts("No solution.");
        for (int i = 0; i < count; ++i)
            std::printf("%d%c", cycle[i] + 1, i + 1 == count ? '\n' : ' ');
    }
}
