#include <cstdio>
#include <map>
#include <string>

const int MAX_NAME_LENGTH = 30;

int main() {
    int count;
    if (scanf("%d", &count) != 1)
        return 0;
    // a team that submitted more than once is the spammer; the teams are
    // printed in the order of their second submission
    std::map<std::string, int> submissions;
    // the names are read with scanf into a fixed buffer, without iostream
    char team[MAX_NAME_LENGTH + 1];
    for (int i = 0; i < count; ++i) {
        scanf("%30s", team);
        // a team is printed at its second submission, once
        if (++submissions[team] == 2)
            puts(team);
    }
}
