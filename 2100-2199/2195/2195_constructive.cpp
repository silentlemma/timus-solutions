#include <iostream>
#include <utility>
#include <vector>

using namespace std;

vector<int> preorder(const vector<int> &parent) {
    int n = static_cast<int>(parent.size());
    vector<vector<int>> children(n);
    for (int vertex = 1; vertex < n; ++vertex) {
        children[parent[vertex]].push_back(vertex);
    }
    vector<int> order;
    vector<int> stack{0};
    while (!stack.empty()) {
        int vertex = stack.back();
        stack.pop_back();
        order.push_back(vertex);
        for (auto it = children[vertex].rbegin(); it != children[vertex].rend(); ++it) {
            stack.push_back(*it);
        }
    }
    return order;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> source(n), target(n);
    for (int vertex = 1; vertex < n; ++vertex) {
        cin >> source[vertex];
    }
    for (int vertex = 1; vertex < n; ++vertex) {
        cin >> target[vertex];
    }
    vector<int> first = preorder(source);
    vector<int> second = preorder(target);
    vector<int> mapping(n);
    for (int i = 0; i < n; ++i) {
        mapping[second[i]] = first[i];
    }

    vector<pair<int, int>> moves;
    // Join consecutive preorder subtrees into one path.
    for (int i = 1; i < n; ++i) {
        if (source[first[i]] != first[i - 1]) {
            moves.emplace_back(first[i], first[i - 1]);
        }
    }
    // Undo the target's path construction using the source labels.
    for (int i = n - 1; i > 0; --i) {
        if (target[second[i]] != second[i - 1]) {
            moves.emplace_back(mapping[second[i]], mapping[target[second[i]]]);
        }
    }
    cout << moves.size() << '\n';
    for (auto move : moves) {
        cout << move.first << ' ' << move.second << '\n';
    }
}
