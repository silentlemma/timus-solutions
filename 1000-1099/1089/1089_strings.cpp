#include <iostream>
#include <set>
#include <string>
#include <vector>

std::set<std::string> known;
int errors = 0;

std::string fix(const std::string &word) {
    if (known.count(word))
        return word;
    // only a single wrong letter is corrected, never a missing or extra one
    for (const std::string &d : known) {
        if (d.size() != word.size())
            continue;
        int diff = 0;
        for (size_t i = 0; i < d.size(); i++)
            diff += d[i] != word[i];
        if (diff == 1) {
            errors++;
            return d;
        }
    }
    return word;
}

int main() {
    std::string line;
    while (std::getline(std::cin, line)) {
        while (!line.empty() && (line.back() == '\r' || line.back() == ' '))
            line.pop_back();
        if (line == "#")
            break;
        if (!line.empty())
            known.insert(line);
    }
    std::string out;
    while (std::getline(std::cin, line)) {
        if (!line.empty() && line.back() == '\r')
            line.pop_back();
        for (size_t i = 0; i < line.size();) {
            if (line[i] < 'a' || line[i] > 'z') {
                out += line[i++];
                continue;
            }
            size_t j = i;
            while (j < line.size() && line[j] >= 'a' && line[j] <= 'z')
                j++;
            out += fix(line.substr(i, j - i));
            i = j;
        }
        out += '\n';
    }
    std::cout << out << errors << "\n";
}
