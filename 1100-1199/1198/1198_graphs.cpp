#include <cstdio>
#include <vector>

static const int BUFFER = 1 << 16;
static char buf[BUFFER];
static int bufLen = 0, bufPos = 0;

static int readChar() {
    if (bufPos == bufLen) {
        bufLen = (int)fread(buf, 1, BUFFER, stdin);
        bufPos = 0;
        if (bufLen <= 0) {
            return -1;
        }
    }
    return buf[bufPos++];
}

static int readInt() {
    int c = readChar();
    while (c != -1 && (c < '0' || c > '9')) {
        c = readChar();
    }
    int v = 0;
    while (c >= '0' && c <= '9') {
        v = v * 10 + c - '0';
        c = readChar();
    }
    return v;
}

// Marks everything reachable from root that is not marked yet; returns how
// many vertices it marked.
static int search(int root, const std::vector<int> &start, const std::vector<int> &edges,
                  std::vector<char> &seen) {
    std::vector<int> queue(1, root);
    seen[root] = 1;
    for (size_t head = 0; head < queue.size(); head++) {
        int u = queue[head];
        for (int e = start[u]; e < start[u + 1]; e++) {
            if (!seen[edges[e]]) {
                seen[edges[e]] = 1;
                queue.push_back(edges[e]);
            }
        }
    }
    return (int)queue.size();
}

int main() {
    int n = readInt();
    std::vector<int> start(n + 1, 0), edges;
    for (int i = 0; i < n; i++) {
        for (int v = readInt(); v != 0; v = readInt()) {
            edges.push_back(v - 1);
        }
        start[i + 1] = (int)edges.size();
    }
    // the reverse graph in the same compact form, built by counting
    std::vector<int> rstart(n + 1, 0), redges(edges.size());
    for (int v : edges) {
        rstart[v + 1]++;
    }
    for (int i = 0; i < n; i++) {
        rstart[i + 1] += rstart[i];
    }
    std::vector<int> fill(rstart.begin(), rstart.end() - 1);
    for (int u = 0; u < n; u++) {
        for (int e = start[u]; e < start[u + 1]; e++) {
            redges[fill[edges[e]]++] = u;
        }
    }

    // nobody outside the marked set can reach the root of the last search,
    // so that root lies in a strongly connected component with no way in
    std::vector<char> seen(n, 0);
    int root = 0;
    for (int u = 0; u < n; u++) {
        if (!seen[u]) {
            root = u;
            search(u, start, edges, seen);
        }
    }
    std::vector<char> forward(n, 0), backward(n, 0);
    if (search(root, start, edges, forward) == n) {
        search(root, rstart, redges, backward);
        for (int u = 0; u < n; u++) {
            if (backward[u]) {
                printf("%d ", u + 1);
            }
        }
    }
    printf("0\n");
}
