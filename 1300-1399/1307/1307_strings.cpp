#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <utility>
#include <vector>

// common pieces of English, tried in this order; each one that pays off
// gets a printable character the text never uses
const char *PIECES[] = {
    "\n", " the ", "the ", " and ", "ing ", " of ", " to ", "ed ", "he ", "th", "in",
    "er", "an",    "re",   "on",    "at",   "en",   "nd",   "es",  "or",  "ou", "ha",
    "is", "it",    "te",   "st",    "ar",   "al",   "le",   "se",  "ve",  "me", "ne",
    "hi", "as",    "ng",   "e ",    "s ",   "d ",   "t ",   ", ",  ". ",  "y ", "o ",
};
const size_t ENTRY = 24;   // the size of one table line, so a piece must save more than this
const size_t CHUNK = 1000; // characters of the coded text per string literal

const int FIRST = 33;          // the first printable character that may become a code
const int LAST = 126;          // and the last one
const char *SPECIAL = "\"\\?"; // need a backslash inside a C string

// the text as it is written inside a C string literal
void writeLiteral(const char *text, size_t length) {
    for (size_t i = 0; i < length; i++) {
        char ch = text[i];
        if (ch == '\n') {
            fputs("\\n", stdout);
        } else {
            if (strchr(SPECIAL, ch))
                putchar('\\');
            putchar(ch);
        }
    }
}

size_t writtenLength(const char *piece) {
    size_t n = 0;
    for (const char *p = piece; *p; p++)
        n += (*p == '\n' || strchr(SPECIAL, *p)) ? 2 : 1;
    return n;
}

int main() {
    std::string text;
    for (int c = getchar(); c != EOF; c = getchar()) {
        if (c != '\r')
            text.push_back((char)c);
    }
    std::vector<char> free;
    for (int c = FIRST; c <= LAST; c++) {
        if (text.find((char)c) == std::string::npos && !strchr(SPECIAL, c))
            free.push_back((char)c);
    }
    std::vector<std::pair<char, const char *>> table;
    size_t next = 0;
    for (const char *piece : PIECES) {
        if (next == free.size())
            break;
        size_t length = strlen(piece), uses = 0;
        for (size_t at = text.find(piece); at != std::string::npos;
             at = text.find(piece, at + length)) {
            uses++;
        }
        // every use saves the written length of the piece less one character
        if (uses * (writtenLength(piece) - 1) <= ENTRY)
            continue;
        char code = free[next++];
        // replace in place, left to right: the text only gets shorter
        size_t write = 0;
        for (size_t read = 0; read < text.size();) {
            if (text.compare(read, length, piece) == 0) {
                text[write++] = code;
                read += length;
            } else {
                text[write++] = text[read++];
            }
        }
        text.resize(write);
        table.push_back({code, piece});
    }
    fputs("//CPP\n#include <cstdio>\nconst char *d[] = {\n", stdout);
    for (size_t i = 0; i < text.size(); i += CHUNK) {
        putchar('"');
        writeLiteral(text.data() + i, std::min(CHUNK, text.size() - i));
        fputs("\",\n", stdout);
    }
    fputs("0};\nint main() {\n    const char *t[256] = {0};\n", stdout);
    for (auto &entry : table) {
        printf("    t[%d] = \"", (int)entry.first);
        writeLiteral(entry.second, strlen(entry.second));
        fputs("\";\n", stdout);
    }
    fputs("    for (int k = 0; d[k]; k++)\n"
          "        for (const char *p = d[k]; *p; p++)\n"
          "            if (t[(unsigned char)*p]) fputs(t[(unsigned char)*p], stdout);\n"
          "            else putchar(*p);\n"
          "    return 0;\n}\n",
          stdout);
    return 0;
}
