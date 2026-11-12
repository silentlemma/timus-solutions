#include <algorithm>
#include <iostream>
#include <vector>

const int MINUTES = 2000;
const int SHAVES = 2;

struct Edge {
    int to, reverse, capacity;
};

std::vector<std::vector<Edge>> graph;
std::vector<bool> visited;

void addEdge(int from, int to, int capacity) {
    const int forward = graph[from].size(), backward = graph[to].size();
    graph[from].push_back({to, backward, capacity});
    graph[to].push_back({from, forward, 0});
}

bool augment(int vertex, int sink) {
    if (vertex == sink)
        return true;
    visited[vertex] = true;
    for (Edge &edge : graph[vertex]) {
        if (edge.capacity > 0 && !visited[edge.to] && augment(edge.to, sink)) {
            --edge.capacity;
            ++graph[edge.to][edge.reverse].capacity;
            return true;
        }
    }
    return false;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, k;
    if (!(std::cin >> n >> k))
        return 0;
    const int sink = n + MINUTES, source = sink + 1;
    graph.resize(source + 1);
    visited.resize(graph.size());
    for (int person = 0; person < n; ++person) {
        int arrival, duration;
        std::cin >> arrival >> duration;
        addEdge(source, person, SHAVES);
        for (int minute = arrival; minute < arrival + duration; ++minute)
            addEdge(person, n + minute, 1);
    }
    for (int minute = 0; minute < MINUTES; ++minute)
        addEdge(n + minute, sink, k);

    for (int flow = 0; flow < SHAVES * n; ++flow) {
        std::fill(visited.begin(), visited.end(), false);
        if (!augment(source, sink)) {
            std::cout << "No\n";
            return 0;
        }
    }

    std::cout << "Yes\n";
    for (int person = 0; person < n; ++person) {
        bool first = true;
        for (const Edge &edge : graph[person]) {
            if (n <= edge.to && edge.to < sink && edge.capacity == 0) {
                std::cout << (first ? "" : " ") << edge.to - n;
                first = false;
            }
        }
        std::cout << '\n';
    }
}
