#include <cctype>
#include <cstdio>
#include <cstring>

const int MAX_QUOTA = 12, MAX_NAME_LENGTH = 36, LINE_BUFFER = 64;

int main() {
    char line[LINE_BUFFER], seen[MAX_QUOTA][MAX_NAME_LENGTH + 1];
    int year, n, quota, count = 0;
    fgets(line, LINE_BUFFER, stdin);
    sscanf(line, "%d %d %d", &year, &n, &quota);
    for (int i = 0; i < n; i++) {
        fgets(line, LINE_BUFFER, stdin);
        char *team = line;
        while (std::isspace(static_cast<unsigned char>(*team)))
            team++;
        char *end = team + std::strlen(team);
        while (end > team && std::isspace(static_cast<unsigned char>(end[-1])))
            *--end = 0;
        char *hash = std::strrchr(team, '#');
        char *universityEnd = hash ? hash : end;
        while (universityEnd > team && std::isspace(static_cast<unsigned char>(universityEnd[-1])))
            universityEnd--;
        char university[MAX_NAME_LENGTH + 1];
        int length = universityEnd - team;
        for (int j = 0; j < length; j++)
            university[j] = std::tolower(static_cast<unsigned char>(team[j]));
        university[length] = 0;
        // Only quota universities are retained; the next unseen university
        // is the answer, so a fixed small array needs no tree allocations.
        bool duplicate = false;
        for (int j = 0; j < count; j++)
            if (std::strcmp(seen[j], university) == 0)
                duplicate = true;
        if (duplicate)
            continue;
        if (count == quota) {
            puts(team);
            return 0;
        }
        std::strcpy(seen[count++], university);
    }
}
