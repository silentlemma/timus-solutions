#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

const int MAX_VALUE = 5000;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, k;
    std::cin >> n;
    // counting sort: atMost[v] is the number of elements not greater than v
    std::vector<int> atMost(MAX_VALUE + 1, 0);
    for (int i = 0, x; i < n && std::cin >> x; i++)
        atMost[x]++;
    for (int v = 1; v <= MAX_VALUE; v++)
        atMost[v] += atMost[v - 1];
    std::string separator;
    std::cin >> separator >> k;
    // the i-th smallest element is the smallest v with at least i elements <= v
    std::string out;
    for (int q = 0, i; q < k && std::cin >> i; q++)
        out += std::to_string(std::lower_bound(atMost.begin(), atMost.end(), i) - atMost.begin()) +
               "\n";
    std::cout << out;
}
