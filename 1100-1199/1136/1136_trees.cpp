#include <cstdio>
#include <vector>

// identification numbers are positive and below this bound, so 0 means none
const int LIMIT = 65536;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<int> post(n);
    for (auto &v : post)
        if (scanf("%d", &v) != 1)
            return 0;
    // read backwards, the odd-session order gives every chairman, then the
    // right wing, then the left wing; a stack of the open chairmen rebuilds the
    // tree from that
    std::vector<int> left(LIMIT, 0), right(LIMIT, 0), stack;
    for (int k = n - 1; k >= 0; k--) {
        int v = post[k];
        if (!stack.empty() && v > stack.back()) {
            right[stack.back()] = v;
        } else if (!stack.empty()) {
            int parent = stack.back();
            stack.pop_back();
            while (!stack.empty() && stack.back() > v) {
                parent = stack.back();
                stack.pop_back();
            }
            left[parent] = v;
        }
        stack.push_back(v);
    }
    // the even-session order is the plain order root, left, right reversed
    std::vector<int> order;
    stack.assign(1, post[n - 1]);
    while (!stack.empty()) {
        int v = stack.back();
        stack.pop_back();
        order.push_back(v);
        if (right[v])
            stack.push_back(right[v]);
        if (left[v])
            stack.push_back(left[v]);
    }
    for (int k = n - 1; k >= 0; k--)
        printf("%d\n", order[k]);
}
