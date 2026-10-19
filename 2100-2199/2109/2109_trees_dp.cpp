#include <algorithm>
#include <cstdio>
#include <numeric>
#include <utility>
#include <vector>

constexpr int ROOT = 1;
constexpr int UNSEEN = -1;
constexpr int IO_BUFFER_SIZE = 65536;
constexpr int DECIMAL_BASE = 10;
constexpr int MAX_DIGITS = 10;

class FastInput {
    char buffer[IO_BUFFER_SIZE];
    int position = 0;
    int size = 0;

    int get() {
        if (position == size) {
            size = static_cast<int>(std::fread(buffer, 1, IO_BUFFER_SIZE, stdin));
            position = 0;
            if (size == 0) {
                return EOF;
            }
        }
        return buffer[position++];
    }

  public:
    int next() {
        int character = get();
        while (character <= ' ' && character != EOF) {
            character = get();
        }
        int value = 0;
        while (character >= '0' && character <= '9') {
            value = value * DECIMAL_BASE + character - '0';
            character = get();
        }
        return value;
    }
};

class FastOutput {
    char buffer[IO_BUFFER_SIZE];
    int size = 0;

    void put(char character) {
        if (size == IO_BUFFER_SIZE) {
            flush();
        }
        buffer[size++] = character;
    }

  public:
    void flush() {
        std::fwrite(buffer, 1, size, stdout);
        size = 0;
    }

    void write(int value) {
        char digits[MAX_DIGITS];
        int count = 0;
        do {
            digits[count++] = static_cast<char>('0' + value % DECIMAL_BASE);
            value /= DECIMAL_BASE;
        } while (value != 0);
        while (count != 0) {
            put(digits[--count]);
        }
        put('\n');
    }
};

int find(int vertex, std::vector<int> &representative) {
    while (representative[vertex] != vertex) {
        representative[vertex] = representative[representative[vertex]];
        vertex = representative[vertex];
    }
    return vertex;
}

int main() {
    FastInput input;
    const int count = input.next();
    std::vector<std::vector<int>> graph(count + 1);
    for (int edge = 1; edge < count; ++edge) {
        const int left = input.next();
        const int right = input.next();
        graph[left].push_back(right);
        graph[right].push_back(left);
    }
    const int query_count = input.next();
    if (query_count == 0) {
        return 0;
    }

    std::vector<int> parent(count + 1, ROOT);
    std::vector<int> representative(count + 1);
    std::iota(representative.begin(), representative.end(), 0);
    std::vector<int> first(count + 1, UNSEEN);
    std::vector<int> order;
    order.reserve(count);
    std::vector<int> adjacent(count - 1);
    std::vector<int> stack{ROOT};
    while (!stack.empty()) {
        const int event = stack.back();
        stack.pop_back();
        if (event < 0) {
            const int vertex = -event;
            representative[vertex] = parent[vertex];
            continue;
        }
        const int vertex = event;
        first[vertex] = static_cast<int>(order.size());
        order.push_back(vertex);
        // Finished subtrees point to their nearest ancestor still on the DFS path.
        for (int neighbor : {vertex - 1, vertex + 1}) {
            if (neighbor >= ROOT && neighbor <= count && first[neighbor] != UNSEEN) {
                const int ancestor = find(neighbor, representative);
                adjacent[std::min(vertex, neighbor) - 1] = first[ancestor];
            }
        }
        stack.push_back(-vertex);
        for (int neighbor : graph[vertex]) {
            if (neighbor != parent[vertex]) {
                parent[neighbor] = vertex;
                stack.push_back(neighbor);
            }
        }
    }

    std::vector<std::vector<int>> table;
    table.push_back(std::move(adjacent));
    const int length = count - 1;
    for (int span = 1; span * 2 <= length; span *= 2) {
        const auto &previous = table.back();
        std::vector<int> row(length - span * 2 + 1);
        for (int index = 0; index < static_cast<int>(row.size()); ++index) {
            row[index] = std::min(previous[index], previous[index + span]);
        }
        table.push_back(std::move(row));
    }
    std::vector<int> logarithm(count);
    for (int value = 2; value < count; ++value) {
        logarithm[value] = logarithm[value / 2] + 1;
    }

    FastOutput output;
    for (int query = 0; query < query_count; ++query) {
        const int left = input.next();
        const int right = input.next();
        if (left == right) {
            output.write(left);
            continue;
        }
        const int level = logarithm[right - left];
        const int span = 1 << level;
        const auto &row = table[level];
        // The range LCA is an ancestor of every adjacent LCA, so its preorder is least.
        const int position = std::min(row[left - 1], row[right - 1 - span]);
        output.write(order[position]);
    }
    output.flush();
}
