#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

enum class OperationType { Query, Direct, Whole, Partial };

struct Operation {
    OperationType type;
    int vertex;
    int limit;
    long long value;
};

class SparseFenwick {
  public:
    explicit SparseFenwick(int size) : size_(size), coordinates_(size + 1), tree_(size + 1) {}

    void register_position(int position, int limit) {
        while (position <= size_) {
            coordinates_[position].push_back(limit);
            position += position & -position;
        }
    }

    void prepare() {
        for (int position = 1; position <= size_; ++position) {
            auto &values = coordinates_[position];
            sort(values.begin(), values.end());
            values.erase(unique(values.begin(), values.end()), values.end());
            tree_[position].assign(values.size() + 1, 0);
        }
    }

    void add(int position, int limit, long long value) {
        while (position <= size_) {
            const auto &values = coordinates_[position];
            int rank =
                static_cast<int>(values.end() - lower_bound(values.begin(), values.end(), limit));
            auto &tree = tree_[position];
            while (rank < static_cast<int>(tree.size())) {
                tree[rank] += value;
                rank += rank & -rank;
            }
            position += position & -position;
        }
    }

    long long sum(int position, int depth) const {
        long long result = 0;
        while (position > 0) {
            const auto &values = coordinates_[position];
            int rank =
                static_cast<int>(values.end() - lower_bound(values.begin(), values.end(), depth));
            const auto &tree = tree_[position];
            while (rank > 0) {
                result += tree[rank];
                rank -= rank & -rank;
            }
            position -= position & -position;
        }
        return result;
    }

  private:
    int size_;
    vector<vector<int>> coordinates_;
    vector<vector<long long>> tree_;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int size;
    cin >> size;
    vector<int> parent(size + 1), first_child(size + 1), next_sibling(size + 1);
    vector<int> depth(size + 1), subtree_size(size + 1, 1), deepest(size + 1);
    for (int vertex = 2; vertex <= size; ++vertex) {
        cin >> parent[vertex];
        depth[vertex] = depth[parent[vertex]] + 1;
        deepest[vertex] = depth[vertex];
        next_sibling[vertex] = first_child[parent[vertex]];
        first_child[parent[vertex]] = vertex;
    }
    for (int vertex = size; vertex > 1; --vertex) {
        subtree_size[parent[vertex]] += subtree_size[vertex];
        deepest[parent[vertex]] = max(deepest[parent[vertex]], deepest[vertex]);
    }

    vector<int> entry(size + 1), exit(size + 1), stack{1};
    int timer = 0;
    while (!stack.empty()) {
        int vertex = stack.back();
        stack.pop_back();
        entry[vertex] = ++timer;
        exit[vertex] = timer + subtree_size[vertex] - 1;
        for (int child = first_child[vertex]; child != 0; child = next_sibling[child]) {
            stack.push_back(child);
        }
    }

    int query_count;
    cin >> query_count;
    vector<Operation> operations;
    operations.reserve(query_count);
    SparseFenwick partial(size);
    for (int index = 0; index < query_count; ++index) {
        char symbol;
        int vertex;
        cin >> symbol >> vertex;
        if (symbol == '?') {
            operations.push_back({OperationType::Query, vertex, 0, 0});
            continue;
        }
        int radius;
        long long value;
        cin >> radius >> value;
        int limit = depth[vertex] + radius;
        OperationType type = OperationType::Partial;
        if (radius == 0) {
            type = OperationType::Direct;
        } else if (limit >= deepest[vertex]) {
            type = OperationType::Whole;
        } else {
            partial.register_position(entry[vertex], limit);
            partial.register_position(exit[vertex] + 1, limit);
        }
        operations.push_back({type, vertex, limit, value});
    }
    partial.prepare();

    vector<long long> direct(size + 1), whole(size + 1);
    for (const auto &operation : operations) {
        int vertex = operation.vertex;
        int left = entry[vertex];
        int right = exit[vertex] + 1;
        if (operation.type == OperationType::Query) {
            long long answer = direct[vertex] + partial.sum(left, depth[vertex]);
            for (int position = left; position > 0; position -= position & -position) {
                answer += whole[position];
            }
            cout << answer << '\n';
        } else if (operation.type == OperationType::Direct) {
            direct[vertex] += operation.value;
        } else if (operation.type == OperationType::Whole) {
            for (int position = left; position <= size; position += position & -position) {
                whole[position] += operation.value;
            }
            for (int position = right; position <= size; position += position & -position) {
                whole[position] -= operation.value;
            }
        } else {
            partial.add(left, operation.limit, operation.value);
            partial.add(right, operation.limit, -operation.value);
        }
    }
}
