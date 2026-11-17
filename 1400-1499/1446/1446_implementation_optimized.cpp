#include <cstdio>
#include <cstring>
#include <vector>

const int HOUSE_COUNT = 4;
const int MAX_STUDENTS = 1000;
const int MAX_NAME = 200;
const int LINE_CAPACITY = MAX_NAME + 2 + 1;
const char *const HOUSES[HOUSE_COUNT] = {"Slytherin", "Hufflepuff", "Gryffindor", "Ravenclaw"};

int main() {
    // the lines are read with fgets into fixed char arrays, at most 1000 names
    // of at most 200 characters, instead of iostream and strings
    char line[LINE_CAPACITY];
    if (!fgets(line, sizeof(line), stdin))
        return 0;
    int n;
    if (sscanf(line, "%d", &n) != 1)
        return 0;
    char names[MAX_STUDENTS][MAX_NAME + 1];
    std::vector<const char *> lists[HOUSE_COUNT];
    for (int i = 0; i < n; ++i) {
        // names keep their inner spaces, so only the line break is dropped
        if (!fgets(line, sizeof(line), stdin))
            return 0;
        line[strcspn(line, "\r\n")] = '\0';
        strcpy(names[i], line);
        if (!fgets(line, sizeof(line), stdin))
            return 0;
        const char *house = line + strspn(line, " \t");
        for (int h = 0; h < HOUSE_COUNT; ++h)
            if (*house == HOUSES[h][0])
                lists[h].push_back(names[i]);
    }
    for (int h = 0; h < HOUSE_COUNT; ++h) {
        if (h > 0)
            putchar('\n');
        printf("%s:\n", HOUSES[h]);
        for (const char *name : lists[h])
            puts(name);
    }
}
