#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <string>
#include <utility>
#include <vector>

const std::string OPEN = "<friend>", CLOSE = "</friend>", END = "</blog>";

std::string trim(const std::string &s) {
    size_t a = s.find_first_not_of(" \t\r\n"), b = s.find_last_not_of(" \t\r\n");
    return a == std::string::npos ? "" : s.substr(a, b - a + 1);
}

// the name inside a friend tag, without other tags or spaces
std::string clean(const std::string &inside) {
    std::string name;
    bool tag = false;
    for (char c : inside) {
        if (c == '<')
            tag = true;
        else if (c == '>')
            tag = false;
        else if (!tag)
            name += c;
    }
    return trim(name);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::string all((std::istreambuf_iterator<char>(std::cin)), std::istreambuf_iterator<char>());
    std::vector<std::string> lines;
    for (size_t start = 0;;) {
        size_t end = all.find('\n', start);
        lines.push_back(
            all.substr(start, end == std::string::npos ? std::string::npos : end - start));
        if (end == std::string::npos)
            break;
        start = end + 1;
    }
    int n = std::stoi(lines[0]);
    size_t pos = 1;
    std::vector<std::pair<std::string, std::set<std::string>>> blogs;
    for (int b = 0; b < n; b++) {
        while (trim(lines[pos]).empty())
            pos++;
        std::string name = trim(lines[pos]), text;
        for (pos++;; pos++) {
            text += lines[pos] + "\n";
            if (lines[pos].find(END) != std::string::npos)
                break;
        }
        pos++;
        std::set<std::string> friends;
        for (size_t at = text.find(OPEN); at != std::string::npos; at = text.find(OPEN, at)) {
            size_t stop = text.find(CLOSE, at + OPEN.size());
            std::string friendName = clean(text.substr(at + OPEN.size(), stop - at - OPEN.size()));
            if (!friendName.empty() && friendName != name)
                friends.insert(friendName);
            at = stop + CLOSE.size();
        }
        blogs.push_back({name, friends});
    }
    std::string out;
    for (size_t b = 0; b < blogs.size(); b++) {
        const std::string &name = blogs[b].first;
        const std::set<std::string> &friends = blogs[b].second;
        std::set<std::string> readers, both;
        for (auto &other : blogs) {
            if (other.first != name && other.second.count(name))
                readers.insert(other.first);
        }
        std::set_intersection(friends.begin(), friends.end(), readers.begin(), readers.end(),
                              std::inserter(both, both.begin()));
        if (b > 0)
            out += "\n";
        out += name + "\n";
        const std::set<std::string> *groups[] = {&friends, &readers, &both};
        for (int g = 0; g < (int)(sizeof groups / sizeof groups[0]); g++) {
            out += std::to_string(g + 1) + ": ";
            bool first = true;
            for (const std::string &s : *groups[g]) {
                out += (first ? "" : ", ") + s;
                first = false;
            }
            out += "\n";
        }
    }
    std::cout << out;
    return 0;
}
