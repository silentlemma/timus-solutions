#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

enum Kind { LEAF, DIRECT, SKEW };

std::vector<Kind> kinds;
std::vector<int> lefts, rights, values;

int newNode(Kind kind, int left, int right, int value) {
    kinds.push_back(kind);
    lefts.push_back(left);
    rights.push_back(right);
    values.push_back(value);
    return kinds.size() - 1;
}

// the children of the maximal run of nodes of the same kind below and
// including node, in order of position (both joins are associative)
std::vector<int> parts(int node) {
    std::vector<int> out, todo = {node};
    while (!todo.empty()) {
        int cur = todo.back();
        todo.pop_back();
        if (kinds[cur] == kinds[node]) {
            todo.push_back(rights[cur]);
            todo.push_back(lefts[cur]);
        } else {
            out.push_back(cur);
        }
    }
    return out;
}

// a direct node is a sequence of its parts; a skew node is its parts joined
// by stars from the smallest values up, which the stars put last; built
// without recursion, as the tree can be 10^4 levels deep
std::string show(int root) {
    enum What { TEXT, EXPR, SEQ };
    struct Item {
        What what;
        int node;
        char text;
    };
    std::string out;
    std::vector<Item> work = {{EXPR, root, 0}};
    while (!work.empty()) {
        Item item = work.back();
        work.pop_back();
        if (item.what == TEXT) {
            out += item.text;
        } else if (kinds[item.node] == LEAF) {
            std::string number = std::to_string(values[item.node]);
            out += item.what == EXPR ? number : "(" + number + ")";
        } else if (kinds[item.node] == SKEW) {
            std::vector<int> children = parts(item.node);
            // pushed in reverse: the largest values come out first as text
            for (size_t i = 0; i < children.size(); i++) {
                if (i > 0) {
                    work.push_back({TEXT, 0, '*'});
                }
                work.push_back({SEQ, children[i], 0});
            }
        } else {
            std::vector<int> children = parts(item.node);
            work.push_back({TEXT, 0, ')'});
            for (size_t i = children.size(); i-- > 0;) {
                work.push_back({EXPR, children[i], 0});
                work.push_back({TEXT, 0, i > 0 ? ',' : '('});
            }
        }
    }
    // a lone number at the top must still be a sequence
    return kinds[root] == LEAF ? "(" + out + ")" : out;
}

int main() {
    int n;
    scanf("%d", &n);
    // blocks of consecutive positions holding consecutive values, as
    // (lowest value, highest value, tree); two neighbours whose value ranges
    // touch join into one block
    struct Block {
        int lo, hi, node;
    };
    std::vector<Block> stack;
    for (int i = 0; i < n; i++) {
        int v;
        scanf("%d", &v);
        Block cur = {v, v, newNode(LEAF, -1, -1, v)};
        while (!stack.empty()) {
            Block prev = stack.back();
            if (prev.hi + 1 == cur.lo) {
                cur.node = newNode(DIRECT, prev.node, cur.node, 0);
            } else if (cur.hi + 1 == prev.lo) {
                cur.node = newNode(SKEW, prev.node, cur.node, 0);
            } else {
                break;
            }
            stack.pop_back();
            cur.lo = std::min(cur.lo, prev.lo);
            cur.hi = std::max(cur.hi, prev.hi);
        }
        stack.push_back(cur);
    }
    printf("%s\n", stack.size() == 1 ? show(stack[0].node).c_str() : "IMPOSSIBLE");
}
