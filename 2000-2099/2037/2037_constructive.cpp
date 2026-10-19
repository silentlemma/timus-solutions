#include <iostream>
#include <string>

constexpr int SMALL_LIMIT = 7, STABLE_MIN = 8, EXTRA_COUNT = 6;
const std::string PERIOD = "babbaa";
std::string construct(int n, int count) {
    int minimum = n <= SMALL_LIMIT ? n : (n == STABLE_MIN ? SMALL_LIMIT : STABLE_MIN);
    if (count < minimum)
        return "NO";
    if (count == n)
        return std::string(n, 'a');
    if (n == STABLE_MIN)
        return "aababbaa";
    int run = count - EXTRA_COUNT;
    std::string word(run, 'a');
    word.reserve(n);
    for (int at = run; at < n; ++at)
        word += PERIOD[(at - run) % PERIOD.size()];
    return word;
}
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    if (!(std::cin >> n))
        return 0;
    for (int count = 1; count <= n; ++count)
        std::cout << count << " : " << construct(n, count) << '\n';
}
