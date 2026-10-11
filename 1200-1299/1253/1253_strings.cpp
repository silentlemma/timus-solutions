#include <algorithm>
#include <cstdio>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

const int LIMIT = 1000000;

int n;
std::vector<std::string> text;
std::vector<int> sizeOf, state;
std::string out;

// the fully expanded length, capped above the limit; state 1 marks
// templates being expanded, so meeting one again is a cycle
bool measure(int i) {
    state[i] = 1;
    for (size_t k = 0; k < text[i].size(); k++) {
        if (text[i][k] != '*') {
            sizeOf[i] = std::min(sizeOf[i] + 1, LIMIT + 1);
            continue;
        }
        int j = text[i][++k] - '0';
        if (state[j] == 1 || (state[j] == 0 && !measure(j)))
            return false;
        sizeOf[i] = std::min(sizeOf[i] + sizeOf[j], LIMIT + 1);
    }
    state[i] = 2;
    return true;
}

void write(int i) {
    for (size_t k = 0; k < text[i].size(); k++) {
        if (text[i][k] == '*')
            write(text[i][++k] - '0');
        else
            out += text[i][k];
    }
}

int main() {
    std::string data((std::istreambuf_iterator<char>(std::cin)), std::istreambuf_iterator<char>());
    data.erase(std::remove(data.begin(), data.end(), '\r'), data.end());
    size_t line = data.find('\n');
    n = std::stoi(data.substr(0, line));
    // a template runs from the start of a line to its '#'
    text.assign(n + 1, "");
    size_t pos = line + 1;
    for (int i = 1; i <= n; i++) {
        size_t end = data.find('#', pos);
        text[i] = data.substr(pos, end - pos);
        pos = end + 1;
        if (pos < data.size() && data[pos] == '\n')
            pos++;
    }
    sizeOf.assign(n + 1, 0);
    state.assign(n + 1, 0);
    if (!measure(1) || sizeOf[1] > LIMIT) {
        puts("#");
        return 0;
    }
    write(1);
    out += '\n';
    fwrite(out.data(), 1, out.size(), stdout);
}
