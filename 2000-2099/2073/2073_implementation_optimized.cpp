#include <cstdio>
#include <cstring>

const int NAME_WIDTH = 30, DATE_WIDTH = 8, PROBLEMS = 13;
const int WIDTH = NAME_WIDTH + DATE_WIDTH + PROBLEMS + 4;
const int DATE_START = NAME_WIDTH + 2, MARK_START = NAME_WIDTH + DATE_WIDTH + 3;
const int LINE_BUFFER = 64;
char row[WIDTH + 1], border[WIDTH + 1];

void blank_row() {
    for (int i = 0; i < WIDTH; i++)
        row[i] = ' ';
    row[0] = row[NAME_WIDTH + 1] = row[NAME_WIDTH + DATE_WIDTH + 2] = row[WIDTH - 1] = '|';
    row[WIDTH] = '\n';
}

void end_line() {
    int ch;
    do {
        ch = getchar();
    } while (ch != EOF && ch != '\n');
}

void line(char *text) {
    if (!fgets(text, LINE_BUFFER, stdin)) {
        text[0] = 0;
        return;
    }
    int length = std::strlen(text);
    while (length && (text[length - 1] == '\r' || text[length - 1] == '\n'))
        text[--length] = 0;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    end_line();
    blank_row();
    for (int i = 0; i < WIDTH; i++)
        border[i] = row[i] == '|' ? '+' : '-';
    border[WIDTH] = '\n';
    std::memcpy(row + 1, "Contest name", sizeof("Contest name") - 1);
    std::memcpy(row + DATE_START, "Date", sizeof("Date") - 1);
    for (int i = 0; i < PROBLEMS; i++)
        row[MARK_START + i] = char('A' + i);
    fwrite(border, 1, sizeof(border), stdout);
    fwrite(row, 1, sizeof(row), stdout);
    fwrite(border, 1, sizeof(border), stdout);
    char name[LINE_BUFFER], date[LINE_BUFFER], submit[LINE_BUFFER];
    for (int contest = 0; contest < n; contest++) {
        line(name);
        line(date);
        int p, s;
        if (scanf("%d %d", &p, &s) != 2)
            return 0;
        end_line();
        blank_row();
        std::memcpy(row + 1, name, std::strlen(name));
        std::memcpy(row + DATE_START, date, DATE_WIDTH);
        for (int i = 0; i < p; i++)
            row[MARK_START + i] = '.';
        for (int attempt = 0; attempt < s; attempt++) {
            line(submit);
            int i = submit[0] - 'A', verdict = 1;
            while (submit[verdict] == ' ')
                verdict++;
            // Among the six allowed verdicts, only Accepted starts with A.
            if (submit[verdict] == 'A')
                row[MARK_START + i] = 'o';
            else if (row[MARK_START + i] != 'o')
                row[MARK_START + i] = 'x';
        }
        fwrite(row, 1, sizeof(row), stdout);
        fwrite(border, 1, sizeof(border), stdout);
    }
}
