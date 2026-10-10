#include <cctype>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

typedef std::map<std::string, long long> Counts;

// the number starting at s[i] (1 if there is none); i moves past it
long long number(const std::string &s, size_t &i) {
    size_t j = i;
    while (j < s.size() && isdigit(s[j])) {
        j++;
    }
    long long v = j > i ? std::stoll(s.substr(i, j - i)) : 1;
    i = j;
    return v;
}

Counts totals(const std::string &formula) {
    Counts result;
    std::stringstream terms(formula);
    std::string term;
    while (std::getline(terms, term, '+')) {
        size_t i = 0;
        long long times = number(term, i);
        // one level per open bracket; a closing bracket multiplies its level
        // by the number after it and adds it to the level outside
        std::vector<Counts> stack(1);
        while (i < term.size()) {
            if (term[i] == '(') {
                stack.emplace_back();
                i++;
            } else if (term[i] == ')') {
                Counts inner = stack.back();
                stack.pop_back();
                i++;
                long long k = number(term, i);
                for (auto &[name, count] : inner) {
                    stack.back()[name] += count * k;
                }
            } else {
                size_t j = i + 1;
                if (j < term.size() && islower(term[j])) {
                    j++;
                }
                std::string name = term.substr(i, j - i);
                stack.back()[name] += number(term, j);
                i = j;
            }
        }
        for (auto &[name, count] : stack[0]) {
            result[name] += count * times;
        }
    }
    return result;
}

int main() {
    std::string left, right;
    int n;
    std::cin >> left >> n;
    Counts want = totals(left);
    for (int q = 0; q < n; q++) {
        std::cin >> right;
        std::cout << left << (totals(right) == want ? "==" : "!=") << right << "\n";
    }
}
