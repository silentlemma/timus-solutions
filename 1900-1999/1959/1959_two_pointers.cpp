#include <algorithm>
#include <iostream>
#include <vector>

struct Modes {
    std::vector<int> frequency, previous, following, head;
    int maximum = 0;
    Modes(int alphabet, int capacity)
        : frequency(alphabet + 1), previous(alphabet + 1), following(alphabet + 1),
          head(capacity + 1) {}
    void change(int value, int delta) {
        const int old = frequency[value];
        if (old != 0) {
            const int left = previous[value], right = following[value];
            if (left != 0)
                following[left] = right;
            else
                head[old] = right;
            if (right != 0)
                previous[right] = left;
        }
        const int nextCount = old + delta;
        frequency[value] = nextCount;
        if (nextCount != 0) {
            const int first = head[nextCount];
            previous[value] = 0;
            following[value] = first;
            if (first != 0)
                previous[first] = value;
            head[nextCount] = value;
        } else
            previous[value] = following[value] = 0;
        maximum = std::max(maximum, nextCount);
        while (maximum != 0 && head[maximum] == 0)
            --maximum;
    }
    int mode() const { return head[maximum]; }
};

void restore(std::vector<int> &text, std::vector<int> &pattern) {
    const int n = static_cast<int>(text.size()), m = static_cast<int>(pattern.size());
    const int gap = n - m;
    const int alphabet = std::max(*std::max_element(text.begin(), text.end()),
                                  *std::max_element(pattern.begin(), pattern.end()));
    if (std::find(text.begin(), text.end(), 0) != text.end()) {
        Modes counter(alphabet, m);
        for (int index = 0; index < n; ++index) {
            if (index < m)
                counter.change(pattern[index], 1);
            if (index > gap)
                counter.change(pattern[index - gap - 1], -1);
            if (text[index] == 0)
                text[index] = counter.mode();
        }
    } else if (std::find(pattern.begin(), pattern.end(), 0) != pattern.end()) {
        const int width = gap + 1;
        Modes counter(alphabet, width);
        for (int index = 0; index < width; ++index)
            counter.change(text[index], 1);
        for (int index = 0; index < m; ++index) {
            if (pattern[index] == 0)
                pattern[index] = counter.mode();
            if (index + 1 < m) {
                counter.change(text[index], -1);
                counter.change(text[index + width], 1);
            }
        }
    }
}

void printRow(const std::vector<int> &values) {
    for (std::size_t i = 0; i < values.size(); ++i) {
        if (i != 0)
            std::cout << ' ';
        std::cout << values[i];
    }
    std::cout << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    if (!(std::cin >> n))
        return 0;
    std::vector<int> text(n);
    for (auto &value : text)
        std::cin >> value;
    int m;
    std::cin >> m;
    std::vector<int> pattern(m);
    for (auto &value : pattern)
        std::cin >> value;
    restore(text, pattern);
    printRow(text);
    printRow(pattern);
}
