#include <algorithm>
#include <cstdint>
#include <cstdio>

constexpr int INPUT_SIZE = 8192;
char input[INPUT_SIZE];
int position = 0, length = 0;

int byte() {
    if (position == length) {
        length = fread(input, 1, INPUT_SIZE, stdin);
        position = 0;
        if (length == 0)
            return -1;
    }
    return input[position++];
}

long long number() {
    int c = byte();
    while (c >= 0 && c <= ' ')
        c = byte();
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = byte();
    }
    long long value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = byte();
    }
    return sign * value;
}

constexpr int IDS = 40001;
constexpr uint16_t NONE = UINT16_MAX;
struct Node {
    uint16_t parent, child, sibling, enter, leave;
};
Node nodes[IDS];

bool ancestor(int a, int b) {
    return nodes[a].enter != NONE && nodes[a].enter <= nodes[b].enter &&
           nodes[b].enter < nodes[a].leave;
}

int main() {
    int n = number(), root = NONE;
    for (auto &node : nodes)
        node = {NONE, NONE, NONE, NONE, 0};
    for (int i = 0; i < n; ++i) {
        int vertex = number(), parent = number();
        if (parent < 0)
            root = vertex;
        else {
            nodes[vertex].parent = parent;
            nodes[vertex].sibling = nodes[parent].child;
            nodes[parent].child = vertex;
        }
    }
    int vertex = root;
    uint16_t clock = 0;
    while (vertex != NONE) {
        nodes[vertex].enter = clock++;
        if (nodes[vertex].child != NONE) {
            vertex = nodes[vertex].child;
            continue;
        }
        while (vertex != NONE) {
            nodes[vertex].leave = clock;
            if (nodes[vertex].sibling != NONE) {
                vertex = nodes[vertex].sibling;
                break;
            }
            vertex = nodes[vertex].parent;
        }
    }
    int queries = number();
    for (int i = 0; i < queries; ++i) {
        int a = number(), b = number();
        std::putchar(ancestor(a, b) ? '1' : ancestor(b, a) ? '2' : '0');
        std::putchar('\n');
    }
}
