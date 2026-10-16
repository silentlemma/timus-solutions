#include <iostream>
#include <string>
#include <utility>
#include <vector>

const int MOST = 30;

int main() {
    std::string line;
    if (!std::getline(std::cin, line)) return 0;
    int t = std::stoi(line);
    for (int test = 0; test < t; test++) {
        std::getline(std::cin, line);
        std::vector<int> numbers;
        bool firstHome = line.find(" home ") != std::string::npos;
        size_t i = 0;
        while (i < line.size()) {
            if (isdigit((unsigned char)line[i])) {
                size_t len = 0;
                numbers.push_back(std::stoi(line.substr(i), &len));
                i += len;
            } else {
                i++;
            }
        }
        int x = numbers[0], y = numbers[1], lowest = -1, highest = -1;
        for (int g = 0; g <= MOST; g++) {
            bool canPass = false, canFail = false;
            for (int o = 0; o <= MOST; o++) {
                // totals first, then goals scored at the other team's stadium, and
                // when both are equal a coin decides, so both may happen
                std::pair<int, int> ours = {x + g, firstHome ? g : x};
                std::pair<int, int> theirs = {y + o, firstHome ? y : o};
                if (ours >= theirs) canPass = true;
                if (ours <= theirs) canFail = true;
            }
            if (canPass && lowest == -1) lowest = g;
            if (canFail) highest = g;
        }
        std::cout << lowest << " " << highest << "\n";
    }
    return 0;
}
