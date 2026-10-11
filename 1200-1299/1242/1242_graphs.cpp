#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

const int WORD = 16;

// marks everyone reachable from the victims along one kind of link
void clear(const std::vector<int> &start, const std::vector<std::vector<int>> &links,
           std::vector<bool> &cleared) {
    std::vector<int> stack(start);
    std::vector<bool> seen(links.size());
    while (!stack.empty()) {
        int v = stack.back();
        stack.pop_back();
        for (int u : links[v])
            if (!seen[u]) {
                seen[u] = cleared[u] = true;
                stack.push_back(u);
            }
    }
}

int main() {
    int n;
    scanf("%d", &n);
    std::vector<std::vector<int>> parents(n + 1), children(n + 1);
    char word[WORD];
    while (scanf("%15s", word) == 1 && strcmp(word, "BLOOD") != 0) {
        int child = atoi(word), parent;
        scanf("%d", &parent);
        parents[child].push_back(parent);
        children[parent].push_back(child);
    }
    std::vector<bool> cleared(n + 1);
    std::vector<int> victims;
    int v;
    while (scanf("%d", &v) == 1) {
        victims.push_back(v);
        cleared[v] = true;
    }
    // the werewolf spares its ancestors and descendants, so no ancestor and
    // no descendant of a victim can be the werewolf
    clear(victims, parents, cleared);
    clear(victims, children, cleared);
    bool found = false;
    for (int u = 1; u <= n; u++)
        if (!cleared[u]) {
            printf(found ? " %d" : "%d", u);
            found = true;
        }
    printf(found ? "\n" : "0\n");
}
