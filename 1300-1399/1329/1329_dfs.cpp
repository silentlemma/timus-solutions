#include <cstdio>
#include <vector>

const int IDS = 40001;

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<int>> children(IDS);
    int root = -1;
    for (int i = 0; i < n; i++) {
        int node = 0, parent = 0;
        if (scanf("%d %d", &node, &parent) != 2)
            return 0;
        if (parent < 0)
            root = node;
        else
            children[parent].push_back(node);
    }
    // enter[v] and leave[v] bound the times of the whole subtree of v
    std::vector<int> enter(IDS, -1), leave(IDS, -1), stack = {root};
    int clock = 0;
    while (!stack.empty()) {
        int node = stack.back();
        stack.pop_back();
        if (node >= 0) {
            enter[node] = clock++;
            stack.push_back(~node);
            for (int child : children[node])
                stack.push_back(child);
        } else {
            leave[~node] = clock;
        }
    }
    int queries = 0;
    if (scanf("%d", &queries) != 1)
        return 0;
    std::vector<char> out;
    for (int i = 0; i < queries; i++) {
        int a = 0, b = 0;
        if (scanf("%d %d", &a, &b) != 2)
            break;
        char answer = '0';
        if (enter[a] >= 0 && enter[a] <= enter[b] && enter[b] < leave[a])
            answer = '1';
        else if (enter[b] >= 0 && enter[b] <= enter[a] && enter[a] < leave[b])
            answer = '2';
        out.push_back(answer);
        out.push_back('\n');
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
