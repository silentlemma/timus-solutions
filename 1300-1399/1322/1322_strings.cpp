#include <iostream>
#include <string>
#include <vector>

const int CHARS = 128;

int main() {
    std::ios::sync_with_stdio(false);
    int k = 0;
    std::string last;
    if (!(std::cin >> k >> last))
        return 0;
    int n = (int)last.size();
    // a stable counting sort of the last column: row order[j] ends with
    // the j-th character of the sorted column, the first one of row j
    std::vector<int> start(CHARS + 1, 0), order(n);
    for (char c : last)
        start[(unsigned char)c + 1]++;
    for (int c = 0; c < CHARS; c++)
        start[c + 1] += start[c];
    for (int i = 0; i < n; i++)
        order[start[(unsigned char)last[i]]++] = i;
    std::string text(n, ' ');
    int row = k - 1;
    for (int i = 0; i < n; i++) {
        row = order[row];
        text[i] = last[row];
    }
    std::cout << text << "\n";
    return 0;
}
