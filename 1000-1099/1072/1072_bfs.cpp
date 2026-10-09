#include <cstdio>
#include <queue>
#include <vector>

const int OCTETS = 4;
const int OCTET_BITS = 8;

unsigned read_address() {
    unsigned v = 0;
    for (int i = 0; i < OCTETS; i++) {
        unsigned part = 0;
        scanf(i > 0 ? ".%u" : "%u", &part);
        v = v << OCTET_BITS | part;
    }
    return v;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // each interface is reduced to its subnet, IP AND mask
    std::vector<std::vector<unsigned>> nets(n);
    for (auto &own : nets) {
        int k = 0;
        scanf("%d", &k);
        for (int j = 0; j < k; j++) {
            unsigned ip = read_address();
            own.push_back(ip & read_address());
        }
    }
    int start = 0, end = 0;
    scanf("%d %d", &start, &end);
    start--, end--;
    auto linked = [&](int u, int v) {
        for (unsigned p : nets[u])
            for (unsigned q : nets[v])
                if (p == q)
                    return true;
        return false;
    };
    std::vector<int> from(n, -1);
    from[start] = start;
    std::queue<int> queue;
    queue.push(start);
    while (!queue.empty()) {
        int u = queue.front();
        queue.pop();
        for (int v = 0; v < n; v++)
            if (from[v] < 0 && linked(u, v)) {
                from[v] = u;
                queue.push(v);
            }
    }
    if (from[end] < 0) {
        puts("No");
        return 0;
    }
    std::vector<int> path{end};
    while (path.back() != start)
        path.push_back(from[path.back()]);
    puts("Yes");
    for (size_t i = path.size(); i-- > 0;)
        printf("%d%c", path[i] + 1, i ? ' ' : '\n');
}
