#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

constexpr std::int64_t MOD = 998244353;
constexpr int CYCLE_PERIOD = 4;

struct Path {
    int from;
    int to;
    int internal;
};

std::int64_t power(std::int64_t base, std::int64_t exponent) {
    std::int64_t result = 1;
    while (exponent > 0) {
        if (exponent % 2 == 1) {
            result = result * base % MOD;
        }
        base = base * base % MOD;
        exponent /= 2;
    }
    return result;
}

std::int64_t determinant(std::vector<std::vector<std::int64_t>> &matrix) {
    const int size = static_cast<int>(matrix.size());
    std::int64_t result = 1;
    for (int column = 0; column < size; ++column) {
        int pivot = column;
        while (pivot < size && matrix[pivot][column] == 0) {
            ++pivot;
        }
        if (pivot == size) {
            return 0;
        }
        if (pivot != column) {
            std::swap(matrix[pivot], matrix[column]);
            result = MOD - result;
        }
        const auto value = matrix[column][column];
        result = result * value % MOD;
        const auto inverse = power(value, MOD - 2);
        for (int row = column + 1; row < size; ++row) {
            if (matrix[row][column] == 0) {
                continue;
            }
            const auto factor = matrix[row][column] * inverse % MOD;
            for (int next = column + 1; next < size; ++next) {
                auto updated = matrix[row][next] - factor * matrix[column][next] % MOD;
                if (updated < 0) {
                    updated += MOD;
                }
                matrix[row][next] = updated;
            }
        }
    }
    return result;
}

std::int64_t solve(const std::vector<std::vector<int>> &graph) {
    const int size = static_cast<int>(graph.size());
    std::vector<int> degree(size);
    std::vector<int> queue;
    queue.reserve(size);
    std::vector<bool> active(size, true);
    for (int vertex = 0; vertex < size; ++vertex) {
        degree[vertex] = static_cast<int>(graph[vertex].size());
        if (degree[vertex] == 0) {
            return 0;
        }
        if (degree[vertex] == 1) {
            queue.push_back(vertex);
        }
    }

    std::int64_t result = 1;
    for (std::size_t head = 0; head < queue.size(); ++head) {
        const int leaf = queue[head];
        if (!active[leaf]) {
            continue;
        }
        int neighbor = -1;
        for (int vertex : graph[leaf]) {
            if (active[vertex]) {
                neighbor = vertex;
                break;
            }
        }
        // Expanding at a leaf removes its neighbor and changes the sign.
        active[leaf] = false;
        active[neighbor] = false;
        result = MOD - result;
        for (int vertex : graph[neighbor]) {
            if (active[vertex]) {
                --degree[vertex];
                if (degree[vertex] == 0) {
                    return 0;
                }
                if (degree[vertex] == 1) {
                    queue.push_back(vertex);
                }
            }
        }
    }

    std::vector<int> index(size, -1);
    int branches = 0;
    for (int vertex = 0; vertex < size; ++vertex) {
        if (active[vertex] && degree[vertex] > 2) {
            index[vertex] = branches++;
        }
    }
    std::vector<bool> visited(size, false);
    std::vector<Path> paths;
    int auxiliaries = 0;
    for (int vertex = 0; vertex < size; ++vertex) {
        if (index[vertex] < 0) {
            continue;
        }
        for (int neighbor : graph[vertex]) {
            if (!active[neighbor]) {
                continue;
            }
            if (index[neighbor] >= 0) {
                if (vertex < neighbor) {
                    paths.push_back({index[vertex], index[neighbor], 0});
                }
                continue;
            }
            if (visited[neighbor]) {
                continue;
            }
            int previous = vertex;
            int current = neighbor;
            int internal = 0;
            while (index[current] < 0) {
                visited[current] = true;
                ++internal;
                int next = -1;
                for (int candidate : graph[current]) {
                    if (active[candidate] && candidate != previous) {
                        next = candidate;
                        break;
                    }
                }
                previous = current;
                current = next;
            }
            paths.push_back({index[vertex], index[current], internal});
            auxiliaries += internal % 2;
        }
    }

    // Odd paths leave independent auxiliary vertices in the reduced matrix.
    if (auxiliaries > branches) {
        return 0;
    }
    for (int vertex = 0; vertex < size; ++vertex) {
        if (!active[vertex] || index[vertex] >= 0 || visited[vertex]) {
            continue;
        }
        int length = 0;
        int previous = -1;
        int current = vertex;
        do {
            visited[current] = true;
            ++length;
            int next = -1;
            for (int candidate : graph[current]) {
                if (active[candidate] && candidate != previous) {
                    next = candidate;
                    break;
                }
            }
            previous = current;
            current = next;
        } while (current != vertex);
        if (length % 2 == 1) {
            result = result * 2 % MOD;
        } else if (length % CYCLE_PERIOD == 0) {
            return 0;
        } else {
            result = result * (MOD - CYCLE_PERIOD) % MOD;
        }
    }

    const int reduced_size = branches + auxiliaries;
    std::vector<std::vector<std::int64_t>> matrix(reduced_size,
                                                  std::vector<std::int64_t>(reduced_size, 0));
    const auto add_edge = [&](int from, int to, std::int64_t weight) {
        matrix[from][to] = (matrix[from][to] + weight) % MOD;
        matrix[to][from] = (matrix[to][from] + weight) % MOD;
    };
    int next_auxiliary = branches;
    for (const auto &path : paths) {
        const bool negative = (path.internal / 2) % 2 == 1;
        const std::int64_t weight = negative ? MOD - 1 : 1;
        if (negative) {
            result = MOD - result;
        }
        // Removing two internal vertices negates the new edge and determinant.
        if (path.internal % 2 == 0) {
            add_edge(path.from, path.to, weight);
        } else {
            add_edge(path.from, next_auxiliary, weight);
            add_edge(next_auxiliary, path.to, 1);
            ++next_auxiliary;
        }
    }
    return result * determinant(matrix) % MOD;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size;
    int edges;
    std::cin >> size >> edges;
    std::vector<std::vector<int>> graph(size);
    for (int edge = 0; edge < edges; ++edge) {
        int from;
        int to;
        std::cin >> from >> to;
        --from;
        --to;
        graph[from].push_back(to);
        graph[to].push_back(from);
    }
    std::cout << solve(graph) << '\n';
}
