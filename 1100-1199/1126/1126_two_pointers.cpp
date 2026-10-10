#include <cstdio>
#include <deque>
#include <string>
#include <vector>

int main() {
    int m;
    if (scanf("%d", &m) != 1)
        return 0;
    std::vector<int> values;
    for (int v; scanf("%d", &v) == 1 && v >= 0;)
        values.push_back(v);
    // indices of the window whose values decrease from front to back: the
    // front is the maximum, and a value never matters once a later one is larger
    std::deque<int> window;
    std::string out;
    for (int i = 0; i < (int)values.size(); i++) {
        while (!window.empty() && values[window.back()] <= values[i])
            window.pop_back();
        window.push_back(i);
        if (window.front() <= i - m)
            window.pop_front();
        if (i >= m - 1)
            out += std::to_string(values[window.front()]) + "\n";
    }
    fputs(out.c_str(), stdout);
}
