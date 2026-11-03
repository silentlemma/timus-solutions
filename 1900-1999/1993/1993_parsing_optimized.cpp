#include <cstdio>
#include <cstring>

const int MAX_LENGTH = 100, ROLE_COUNT = 3;
char text[MAX_LENGTH + 2], output[MAX_LENGTH + 2];
int used;

void append(int start, int length) {
    memcpy(output + used, text + start, length);
    used += length;
}

int main() {
    if (!fgets(text, sizeof(text), stdin))
        return 0;
    int n = std::strlen(text);
    while (n && (text[n - 1] == '\n' || text[n - 1] == '\r'))
        n--;
    for (int i = 0; i < n; i++)
        if (text[i] >= 'A' && text[i] <= 'Z')
            text[i] += 'a' - 'A';
    const char opening[] = "{([", closing[] = "})]";
    int begin = 0;
    while (begin < n) {
        int end = begin;
        while (end < n && text[end] != ',')
            end++;
        int starts[ROLE_COUNT] = {}, lengths[ROLE_COUNT] = {};
        int prefix = 0, prefix_length = 0, i = begin;
        // Keep spans in the original line instead of streams and copied clauses.
        while (i < end) {
            int role = 0;
            while (role < ROLE_COUNT && opening[role] != text[i])
                role++;
            if (role < ROLE_COUNT) {
                starts[role] = ++i;
                while (i < end && text[i] != closing[role])
                    i++;
                lengths[role] = i - starts[role];
                i++;
            } else if (text[i] >= 'a' && text[i] <= 'z') {
                prefix = i;
                while (i < end && text[i] >= 'a' && text[i] <= 'z')
                    i++;
                prefix_length = i - prefix;
            } else
                i++;
        }
        if (used) {
            output[used++] = ',';
            output[used++] = ' ';
        }
        if (prefix_length) {
            append(prefix, prefix_length);
            output[used++] = ' ';
        }
        for (int role = 0; role < ROLE_COUNT; role++) {
            if (role)
                output[used++] = ' ';
            append(starts[role], lengths[role]);
        }
        begin = end + 1;
    }
    // Only the first word of the complete sentence is capitalized.
    output[0] += 'A' - 'a';
    output[used++] = '\n';
    fwrite(output, 1, used, stdout);
}
