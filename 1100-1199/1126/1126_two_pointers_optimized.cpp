#include <cstdio>
#include <deque>
#include <utility>

// nextInt parses a reading by hand with getchar; the closing -1 is told by
// its minus sign, and -1 is returned for it
int nextInt() {
    int c = getchar();
    while (c <= ' ' && c != EOF)
        c = getchar();
    if (c == EOF || c == '-')
        return -1;
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = getchar();
    }
    return value;
}

int main() {
    int width = nextInt();
    // (value, index) pairs of the window, values decreasing from front to back: the
    // front is the maximum, and a value never matters once a later one is larger
    std::deque<std::pair<int, int>> window;
    for (int index = 0, value; (value = nextInt()) >= 0; ++index) {
        if (!window.empty() && window.front().second <= index - width)
            window.pop_front();
        // a later reading at least as large makes the earlier one irrelevant
        while (!window.empty() && window.back().first <= value)
            window.pop_back();
        window.emplace_back(value, index);
        if (index + 1 >= width)
            printf("%d\n", window.front().first);
    }
}
