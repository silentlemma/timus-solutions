#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <utility>
#include <vector>

// common pieces of English, tried along with the frequent words of the text
const char *PIECES[] = {
    "\n", " the ", "the ", " and ", "ing ", " of ", " to ", "ed ", "he ", "th", "in",
    "er", "an",    "re",   "on",    "at",   "en",   "nd",   "es",  "or",  "ou", "ha",
    "is", "it",    "te",   "st",    "ar",   "al",   "le",   "se",  "ve",  "me", "ne",
    "hi", "as",    "ng",   "e ",    "s ",   "d ",   "t ",   ", ",  ". ",  "y ", "o ",
};
const size_t LINE = 17;    // a table line without its piece: '    t[NNN] = "";' and a line end
const size_t CHUNK = 1000; // characters of the coded text per string literal
const size_t WORDS = 300;  // the most promising words of the text that are tried

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

size_t writtenLength(const std::string &piece) {
    size_t n = 0;
    for (char ch : piece)
        n += (ch == '\n' || strchr(SPECIAL, ch)) ? 2 : 1;
    return n;
}

// uses of a piece, counted left to right without overlaps
size_t count(const std::string &text, const std::string &piece) {
    size_t uses = 0;
    for (size_t at = text.find(piece); at != std::string::npos;
         at = text.find(piece, at + piece.size()))
        uses++;
    return uses;
}

bool isLetter(char ch) { return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'); }

struct Candidate {
    std::string piece;
    size_t estimate;
};

int main() {
    std::string text;
    for (int c = getchar(); c != EOF; c = getchar()) {
        if (c != '\r')
            text.push_back((char)c);
    }
    bool used[256] = {false};
    for (char ch : text)
        used[(unsigned char)ch] = true;
    std::vector<char> free;
    for (int c = FIRST; c <= LAST; c++) {
        if (!used[c] && !strchr(SPECIAL, c))
            free.push_back((char)c);
    }
    // the words of the text, with the space before them and without, as
    // (start, length) in the text; sorting them groups equal ones
    std::vector<std::pair<unsigned, unsigned>> spans;
    for (size_t i = 0; i < text.size();) {
        if (!isLetter(text[i])) {
            i++;
            continue;
        }
        size_t j = i;
        while (j < text.size() && isLetter(text[j]))
            j++;
        if (j - i >= 2) {
            if (i > 0 && text[i - 1] == ' ')
                spans.push_back({(unsigned)(i - 1), (unsigned)(j - i + 1)});
            spans.push_back({(unsigned)i, (unsigned)(j - i)});
        }
        i = j;
    }
    typedef std::pair<unsigned, unsigned> Span;
    auto less = [&](const Span &a, const Span &b) {
        return text.compare(a.first, a.second, text, b.first, b.second) < 0;
    };
    std::sort(spans.begin(), spans.end(), less);
    std::vector<Candidate> words;
    for (size_t i = 0; i < spans.size();) {
        size_t j = i;
        while (j < spans.size() && !less(spans[i], spans[j]))
            j++;
        size_t uses = j - i, length = spans[i].second;
        words.push_back({text.substr(spans[i].first, length), uses * (length - 1)});
        i = j;
    }
    std::vector<std::pair<unsigned, unsigned>>().swap(spans);
    auto better = [](const Candidate &a, const Candidate &b) {
        return a.estimate != b.estimate ? a.estimate > b.estimate : a.piece < b.piece;
    };
    std::sort(words.begin(), words.end(), better);
    if (words.size() > WORDS)
        words.resize(WORDS);
    // a piece made only of characters of the text can never match a code
    std::vector<Candidate> order;
    for (const char *p : PIECES) {
        std::string piece = p;
        bool fits = true;
        for (char ch : piece)
            fits = fits && used[(unsigned char)ch];
        if (fits)
            order.push_back({piece, count(text, piece) * (writtenLength(piece) - 1)});
    }
    for (Candidate &w : words) {
        bool found = false;
        for (Candidate &c : order) {
            if (c.piece == w.piece) {
                c.estimate = std::max(c.estimate, w.estimate);
                found = true;
            }
        }
        if (!found)
            order.push_back(w);
    }
    std::sort(order.begin(), order.end(), better);
    std::vector<std::pair<char, std::string>> table;
    size_t next = 0;
    for (const Candidate &c : order) {
        if (next == free.size())
            break;
        const std::string &piece = c.piece;
        size_t cost = writtenLength(piece);
        // every use saves the written length of the piece less one character
        if (count(text, piece) * (cost - 1) <= LINE + cost)
            continue;
        char code = free[next++];
        // replace in place, left to right: the text only gets shorter
        size_t write = 0;
        for (size_t read = 0; read < text.size();) {
            if (text.compare(read, piece.size(), piece) == 0) {
                text[write++] = code;
                read += piece.size();
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
        writeLiteral(entry.second.data(), entry.second.size());
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
