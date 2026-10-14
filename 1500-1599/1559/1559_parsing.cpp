#include <cstdio>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>
using namespace std;

// what is known about a set of words: is it non-empty, does it hold the empty
// word, does it hold a non-empty word, is it infinite
struct Set {
    bool any, emptyWord, longWord, infinite;
};

const Set NOTHING = {false, false, false, false};
const Set EMPTY_WORD = {true, true, false, false};
const Set LETTER = {true, false, true, false};

Set unite(Set x, Set y) {
    return {x.any || y.any, x.emptyWord || y.emptyWord, x.longWord || y.longWord,
            x.infinite || y.infinite};
}

Set concat(Set x, Set y) {
    if (!x.any || !y.any)
        return NOTHING;
    return {true, x.emptyWord && y.emptyWord, x.longWord || y.longWord, x.infinite || y.infinite};
}

// repeating a non-empty word gives ever longer words
Set star(Set x) { return {true, true, x.longWord, x.longWord}; }

// one level of brackets: the union so far, the concatenation so far and the
// last symbol, which a star may still apply to
struct Frame {
    Set all = NOTHING, cat = EMPTY_WORD, last = NOTHING;
    bool hasLast = false;

    Set close() const { return unite(all, hasLast ? concat(cat, last) : cat); }

    void push(Set symbol) {
        if (hasLast)
            cat = concat(cat, last);
        last = symbol, hasLast = true;
    }
};

int main() {
    string text((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    vector<Frame> frames(1);
    for (char c : text) {
        Frame &frame = frames.back();
        if (c == '(')
            frames.emplace_back();
        else if (c == ')') {
            Set value = frame.close();
            frames.pop_back();
            frames.back().push(value);
        } else if (c == '|') {
            frame.all = frame.close();
            frame.cat = EMPTY_WORD, frame.hasLast = false;
        } else if (c == '*')
            frame.last = star(frame.last);
        else if (c == '0')
            frame.push(NOTHING);
        else if (c >= 'a' && c <= 'z')
            frame.push(LETTER);
    }
    puts(frames[0].close().infinite ? "N" : "F");
}
