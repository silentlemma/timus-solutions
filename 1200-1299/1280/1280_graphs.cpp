#include <cstdio>
#include <vector>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    std::vector<int> from(m), to(m), place(n + 1);
    for (int i = 0; i < m; i++)
        scanf("%d %d", &from[i], &to[i]);
    for (int i = 0; i < n; i++) {
        int subject;
        scanf("%d", &subject);
        place[subject] = i;
    }
    // the plan is right exactly when every rule points forward in it; a
    // rule from a subject to itself can never hold
    bool ok = true;
    for (int i = 0; i < m; i++)
        if (place[from[i]] >= place[to[i]])
            ok = false;
    printf(ok ? "YES\n" : "NO\n");
}
