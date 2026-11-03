#include <cstdint>
#include <cstdio>
#include <limits>
#include <vector>

const int BUFFER_SIZE = 4096;
const uint16_t UNVISITED = std::numeric_limits<uint16_t>::max();
unsigned char input[BUFFER_SIZE];
int position, available, n, q;
std::vector<uint16_t> head, to, following, askHead, askNext, distance, answer, depth, path, stack;

int read() {
    if (position == available) {
        available = fread(input, 1, BUFFER_SIZE, stdin);
        position = 0;
        if (available == 0)
            return -1;
    }
    return input[position++];
}

int next_int() {
    int c = read();
    while (c <= ' ')
        c = read();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value;
}

int walk(int root) {
    depth.assign(n + 1, UNVISITED);
    depth[root] = 0;
    int top = 1, deepest = root;
    stack[0] = root;
    while (top) {
        int vertex = stack[--top], dv = depth[vertex];
        path[dv] = vertex;
        if (dv > depth[deepest])
            deepest = vertex;
        for (int query = askHead[vertex]; query; query = askNext[query])
            if (answer[query] == 0 && distance[query] <= dv)
                answer[query] = path[dv - distance[query]];
        for (int edge = head[vertex]; edge; edge = following[edge]) {
            int child = to[edge];
            if (depth[child] == UNVISITED) {
                depth[child] = dv + 1;
                stack[top++] = child;
            }
        }
    }
    return deepest;
}

int main() {
    n = next_int();
    q = next_int();
    // Vertex<=20000, edge<=39998, query<=50000: all IDs fit uint16_t.
    // One-based list indices reserve zero as the missing-link sentinel.
    head.resize(n + 1);
    to.resize(2 * n);
    following.resize(2 * n);
    int edge = 0;
    for (int i = 0; i < n - 1; i++) {
        int a = next_int(), b = next_int();
        to[++edge] = b;
        following[edge] = head[a];
        head[a] = edge;
        to[++edge] = a;
        following[edge] = head[b];
        head[b] = edge;
    }
    askHead.resize(n + 1);
    askNext.resize(q + 1);
    distance.resize(q + 1);
    answer.resize(q + 1);
    for (int i = 1; i <= q; i++) {
        int vertex = next_int();
        distance[i] = next_int();
        askNext[i] = askHead[vertex];
        askHead[vertex] = i;
    }
    path.resize(n + 1);
    stack.resize(n + 1);
    // At least one diameter end is farthest from every vertex.
    int a = walk(1), b = walk(a);
    walk(b);
    for (int i = 1; i <= q; i++)
        printf("%u\n", static_cast<unsigned>(answer[i]));
}
