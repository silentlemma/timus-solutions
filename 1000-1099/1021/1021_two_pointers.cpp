#include <cstdio>
#include <vector>

const int TARGET = 10000;

std::vector<int> readList() {
    int n;
    if (scanf("%d", &n) != 1)
        return {};
    std::vector<int> v(n);
    for (int &x : v)
        if (scanf("%d", &x) != 1)
            return {};
    return v;
}

int main() {
    std::vector<int> up = readList(), down = readList();
    // up increases and down decreases: walking both forward, a sum that is
    // too small can only grow by moving in up, a sum too big only shrink in down
    size_t i = 0, j = 0;
    while (i < up.size() && j < down.size()) {
        int sum = up[i] + down[j];
        if (sum == TARGET)
            break;
        if (sum < TARGET)
            i++;
        else
            j++;
    }
    puts(i < up.size() && j < down.size() ? "YES" : "NO");
}
