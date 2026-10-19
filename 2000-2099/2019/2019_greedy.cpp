#include <iostream>
#include <string>
#include <vector>

constexpr int CASE_BIT = 32;

struct Endpoint {
    char letter;
    int id;
};

std::vector<int> solve(int n, const std::string &word) {
    std::vector<int> answer(n);
    std::vector<Endpoint> pending;
    pending.reserve(word.size());
    int upper = 0, lower = 0;
    for (char code : word) {
        bool is_upper = code >= 'A' && code <= 'Z';
        int index = is_upper ? upper++ : lower++;
        if (!pending.empty() && (pending.back().letter ^ code) == CASE_BIT) {
            int previous = pending.back().id;
            pending.pop_back();
            if (is_upper)
                answer[index] = previous;
            else
                answer[previous] = index;
        } else {
            pending.push_back({code, index});
        }
    }
    if (!pending.empty())
        return {};
    return answer;
}

void run(std::istream &in, std::ostream &out) {
    int n;
    std::string word;
    in >> n >> word;
    auto answer = solve(n, word);
    if (answer.empty())
        out << "Impossible\n";
    else {
        for (std::size_t i = 0; i < answer.size(); ++i)
            out << (i ? " " : "") << answer[i] + 1;
        out << '\n';
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    run(std::cin, std::cout);
    return 0;
}
