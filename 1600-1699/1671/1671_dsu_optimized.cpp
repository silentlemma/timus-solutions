#include <cstdio>
#include <utility>
#include <vector>

// refilling this small buffer avoids storing the input; tokens may cross refills.
constexpr int INPUT_BUFFER_SIZE = 8192;

int read_int() {
    static char buffer[INPUT_BUFFER_SIZE];
    static int position = 0, length = 0;
    auto next = []() {
        if (position == length) {
            length = static_cast<int>(std::fread(buffer, 1, INPUT_BUFFER_SIZE, stdin));
            position = 0;
            if (length == 0)
                return EOF;
        }
        return static_cast<int>(buffer[position++]);
    };
    int c;
    do {
        c = next();
    } while (c <= ' ' && c != EOF);
    int value = 0;
    while (c > ' ') {
        value = value * 10 + c - '0';
        c = next();
    }
    return value;
}

std::vector<int> parent;

int find(int v) {
    int root = v;
    while (parent[root] >= 0)
        root = parent[root];
    while (v != root) {
        int next = parent[v];
        parent[v] = root;
        v = next;
    }
    return root;
}

int main() {
    int n = read_int(), m = read_int();
    std::vector<int> from(m), to(m);
    for (int i = 0; i < m; ++i) {
        from[i] = read_int();
        to[i] = read_int();
    }
    int q = read_int();
    std::vector<int> cuts(q);
    std::vector<bool> cut(m);
    for (int &edge : cuts) {
        edge = read_int() - 1;
        cut[edge] = true;
    }
    parent.assign(n + 1, -1);
    int pieces = n;
    auto join = [&](int edge) {
        int a = find(from[edge]), b = find(to[edge]);
        if (a == b)
            return;
        // a root stores the negative size; attach the smaller tree to it.
        if (parent[a] > parent[b])
            std::swap(a, b);
        parent[a] += parent[b];
        parent[b] = a;
        --pieces;
    };
    // run backwards: start from the web after all cuts and put the threads
    // back one by one, last cut first
    for (int i = 0; i < m; ++i)
        if (!cut[i])
            join(i);
    for (int k = q - 1; k >= 0; --k) {
        int edge = cuts[k];
        // the processed cut index is no longer needed, so reuse its slot.
        cuts[k] = pieces;
        join(edge);
    }
    for (int k = 0; k < q; ++k)
        std::printf("%d%c", cuts[k], k + 1 == q ? '\n' : ' ');
}
