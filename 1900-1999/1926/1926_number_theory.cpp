#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

constexpr std::int64_t MODULUS = 614889782588491410;
constexpr std::size_t QUERY_FIELDS = 3;

std::vector<std::int64_t>
processQueries(std::string number,
               const std::vector<std::array<std::int64_t, QUERY_FIELDS>> &queries) {
    std::vector<std::int64_t> weights(number.size(), 1);
    for (std::size_t index = 1; index < weights.size(); ++index) {
        weights[index] = weights[index - 1] * 10 % MODULUS;
    }
    std::int64_t remainder = 0;
    for (char digit : number) {
        remainder = (remainder * 10 + (digit - '0')) % MODULUS;
    }
    std::vector<std::int64_t> answers;
    for (const auto &query : queries) {
        if (query[0] == 0) {
            answers.push_back(remainder % query[1]);
        } else {
            std::size_t place = static_cast<std::size_t>(query[1]);
            std::size_t index = number.size() - place;
            std::int64_t difference = query[2] - (number[index] - '0');
            number[index] = static_cast<char>('0' + query[2]);
            remainder = (remainder + difference * weights[place - 1]) % MODULUS;
            if (remainder < 0)
                remainder += MODULUS;
        }
    }
    return answers;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string number;
    int count;
    std::cin >> number >> count;
    std::vector<std::array<std::int64_t, QUERY_FIELDS>> queries(count);
    for (auto &query : queries) {
        std::cin >> query[0] >> query[1];
        if (query[0] == 1)
            std::cin >> query[2];
    }
    for (std::int64_t answer : processQueries(number, queries)) {
        std::cout << answer << '\n';
    }
    return 0;
}
