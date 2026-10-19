#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

// arcs in pairs e, e ^ 1: an undirected edge is two arcs of full capacity,
// each the reverse of the other
struct Network {
    std::vector<std::vector<int>> head;
    std::vector<int> target, cap, level, arc;

    explicit Network(int nodes) : head(nodes), level(nodes), arc(nodes) {}

    void link(int a, int b, int forward, int backward) {
        head[a].push_back(target.size());
        target.push_back(b);
        cap.push_back(forward);
        head[b].push_back(target.size());
        target.push_back(a);
        cap.push_back(backward);
    }

    bool levels(int source, int sink) {
        std::fill(level.begin(), level.end(), -1);
        level[source] = 0;
        std::vector<int> queue = {source};
        for (size_t i = 0; i < queue.size(); i++) {
            int v = queue[i];
            for (int e : head[v]) {
                if (cap[e] && level[target[e]] < 0) {
                    level[target[e]] = level[v] + 1;
                    queue.push_back(target[e]);
                }
            }
        }
        return level[sink] >= 0;
    }

    int push(int v, int sink, int amount) {
        if (v == sink) return amount;
        for (; arc[v] < (int)head[v].size(); arc[v]++) {
            int e = head[v][arc[v]];
            if (cap[e] && level[target[e]] == level[v] + 1) {
                int got = push(target[e], sink, std::min(amount, cap[e]));
                if (got) {
                    cap[e] -= got;
                    cap[e ^ 1] += got;
                    return got;
                }
            }
        }
        return 0;
    }
};

int main() {
    std::string s, p;
    std::cin >> s >> p;
    int n = s.size(), m = p.size();
    // every erased character is a node; a node on the source side becomes 1,
    // on the sink side 0. Characters s[j] and p[i] meet once in every window
    // where j - i is between 0 and n - m, and differing costs 1.
    std::vector<int> nodeS(n, -1), nodeP(m, -1);
    int count = 0;
    for (int j = 0; j < n; j++) {
        if (s[j] == '?') nodeS[j] = count++;
    }
    for (int i = 0; i < m; i++) {
        if (p[i] == '?') nodeP[i] = count++;
    }
    int source = count, sink = count + 1;
    // pairs with a fixed 1 cost when the node is 0, and with a fixed 0 when 1
    std::vector<int> ones(count, 0), zeros(count, 0);
    long long base = 0;
    Network net(count + 2);
    for (int i = 0; i < m; i++) {
        for (int j = i; j <= i + n - m; j++) {
            int u = nodeP[i], v = nodeS[j];
            if (u < 0 && v < 0) {
                base += p[i] != s[j];
            } else if (u < 0 || v < 0) {
                int w = u < 0 ? v : u;
                char c = u < 0 ? p[i] : s[j];
                (c == '1' ? ones : zeros)[w]++;
            } else {
                net.link(u, v, 1, 1);
            }
        }
    }
    for (int w = 0; w < count; w++) {
        // a node with both kinds of fixed partners pays the smaller anyway
        int both = std::min(ones[w], zeros[w]);
        base += both;
        if (ones[w] > both) net.link(source, w, ones[w] - both, 0);
        if (zeros[w] > both) net.link(w, sink, zeros[w] - both, 0);
    }
    long long flow = 0;
    while (net.levels(source, sink)) {
        std::fill(net.arc.begin(), net.arc.end(), 0);
        while (int got = net.push(source, sink, n * m)) flow += got;
    }
    // the source side of the last search is a minimum cut
    net.levels(source, sink);
    for (int j = 0; j < n; j++) {
        if (nodeS[j] >= 0) s[j] = net.level[nodeS[j]] >= 0 ? '1' : '0';
    }
    for (int i = 0; i < m; i++) {
        if (nodeP[i] >= 0) p[i] = net.level[nodeP[i]] >= 0 ? '1' : '0';
    }
    std::cout << base + flow << "\n" << s << "\n" << p << "\n";
    return 0;
}
