#include <algorithm>
#include <cctype>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string line, text;
    getline(cin, line);
    int n, m;
    sscanf(line.c_str(), "%d %d", &n, &m);
    getline(cin, text); // read whole: the text may start with spaces
    if (!text.empty() && text.back() == '\r')
        text.pop_back();
    int len = text.size();
    // run[i]: how many letters and spaces start at position i
    vector<int> run(len + 1, 0);
    for (int i = len - 1; i >= 0; i--)
        if (isalpha((unsigned char)text[i]) || text[i] == ' ')
            run[i] = run[i + 1] + 1;
    // the farthest reach never moves back, so the longest message each time is best
    int pos = 0, count = 0;
    while (pos < len) {
        pos += max(n, min(m, run[pos]));
        count++;
    }
    printf("%d\n", count);
}
