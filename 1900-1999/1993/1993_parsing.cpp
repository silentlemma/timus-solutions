#include <array>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>

constexpr std::size_t ROLE_COUNT = 3;

std::string transform(std::string sentence) {
    for (char &c : sentence)
        c = static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
    const std::string opening = "{([", closing = "})]";
    std::stringstream input(sentence);
    std::string clause, answer;
    while (std::getline(input, clause, ',')) {
        std::array<std::string, ROLE_COUNT> phrases;
        std::string prefix;
        std::size_t i = 0;
        while (i < clause.size()) {
            const auto role = opening.find(clause[i]);
            if (role != std::string::npos) {
                const auto end = clause.find(closing[role], i + 1);
                phrases[role] = clause.substr(i + 1, end - i - 1);
                i = end + 1;
            } else if (clause[i] >= 'a' && clause[i] <= 'z') {
                const auto begin = i;
                while (i < clause.size() && clause[i] >= 'a' && clause[i] <= 'z')
                    ++i;
                prefix = clause.substr(begin, i - begin);
            } else
                ++i;
        }
        if (!answer.empty())
            answer += ", ";
        if (!prefix.empty())
            answer += prefix + ' ';
        answer += phrases[0] + ' ' + phrases[1] + ' ' + phrases[2];
    }
    answer[0] = static_cast<char>(std::toupper(static_cast<unsigned char>(answer[0])));
    return answer;
}
int main() {
    std::string sentence;
    std::getline(std::cin, sentence);
    std::cout << transform(sentence) << '\n';
    return 0;
}
