#include <iostream>
#include <vector>

std::vector<int> locate(const std::vector<int> &left, const std::vector<int> &right,
                        const std::vector<int> &queries) {
    std::vector<int> stack, answers;
    stack.reserve(left.size());
    answers.reserve(queries.size());
    std::size_t index = 0;
    for (int point : queries) {
        while (index < left.size() && left[index] <= point) {
            while (!stack.empty() && right[stack.back()] < left[index])
                stack.pop_back();
            stack.push_back(static_cast<int>(index++));
        }
        while (!stack.empty() && right[stack.back()] < point)
            stack.pop_back();
        answers.push_back(stack.empty() ? -1 : stack.back() + 1);
    }
    return answers;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    std::cin >> n;
    std::vector<int> left(n), right(n);
    for (int i = 0; i < n; ++i)
        std::cin >> left[i] >> right[i];
    int m;
    std::cin >> m;
    std::vector<int> queries(m);
    for (int &point : queries)
        std::cin >> point;
    for (int answer : locate(left, right, queries))
        std::cout << answer << '\n';
}
