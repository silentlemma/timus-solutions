#include <cstdio>
#include <cstring>

const int MAX_ROOMS = 30;
const int NAME_SIZE = 21;
// at most thirty names of twenty characters, plus their terminating zeroes.
char names[MAX_ROOMS][NAME_SIZE];
int count = 0;

void remember(const char *name) {
    for (int i = 0; i < count; ++i)
        if (std::strcmp(names[i], name) == 0)
            return;
    std::strcpy(names[count++], name);
}

int main() {
    char line[2 * NAME_SIZE];
    if (std::scanf("%41s", line) != 1)
        return 0;
    remember(line);
    while (std::scanf("%41s", line) == 1 && line[0] != '#') {
        char *dash = std::strchr(line, '-');
        *dash = '\0';
        remember(line);
        remember(dash + 1);
    }
    // every other compartment must be emptied through one opened partition,
    // and the partitions of a tree towards the airlock are enough
    std::printf("%d\n", count - 1);
}
