#include <cstdint>
#include <cstdio>
#include <vector>

// refilling makes this buffer independent of total input size and whitespace.
constexpr int BUFFER_SIZE = 4096;
char input[BUFFER_SIZE];
int position = 0, length = 0;
int readByte() {
    if (position == length) {
        length = static_cast<int>(fread(input, 1, BUFFER_SIZE, stdin));
        position = 0;
        if (length == 0)
            return EOF;
    }
    return input[position++];
}
int nextInt() {
    int c;
    do {
        c = readByte();
    } while (c != EOF && c <= ' ');
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = readByte();
    }
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = readByte();
    }
    return value * sign;
}

int main() {
    int n = nextInt(), m = nextInt(), width = n + 1;
    // costs are 1..10000, so a 16-bit zero can represent an absent edge.
    std::vector<uint16_t> cost(width * width);
    std::vector<int> indegree(width), best(width, -1), order;
    for (int i = 0; i < m; ++i) {
        int a = nextInt(), b = nextInt(), c = nextInt();
        cost[a * width + b] = static_cast<uint16_t>(c);
        ++indegree[b];
    }
    int start = nextInt(), finish = nextInt();
    // a path has at most 499 edges of cost 10000, fitting a signed int.
    best[start] = 0;
    for (int v = 1; v <= n; ++v)
        if (indegree[v] == 0)
            order.push_back(v);
    for (size_t at = 0; at < order.size(); ++at) {
        int v = order[at];
        for (int w = 1; w <= n; ++w) {
            int c = cost[v * width + w];
            if (c == 0)
                continue;
            if (best[v] >= 0 && best[v] + c > best[w])
                best[w] = best[v] + c;
            if (--indegree[w] == 0)
                order.push_back(w);
        }
    }
    if (best[finish] < 0)
        puts("No solution");
    else
        printf("%d\n", best[finish]);
}
