#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef unsigned __int128 Key;

const int LETTER_BITS = 5; // letters 1 to 26
const int GAP_BITS = 4;    // a place in the rest, at most 14
const int CUT_BITS = 2;    // 0, 1 or 2 letters deleted
const int ID_SHIFT = CUT_BITS + 2 * GAP_BITS;
const int ID_BITS = 13; // word numbers below 8192
const int LOW_BITS = ID_BITS + ID_SHIFT;
const int GAP_MASK = (1 << GAP_BITS) - 1;
const int CUT_MASK = (1 << CUT_BITS) - 1;
const int PAIR_MASK = (1 << (2 * GAP_BITS)) - 1;

// the rest of a word without letters skip1 and skip2, packed with low
Key pack(const string &w, int skip1, int skip2, unsigned low) {
    Key k = 0;
    for (int i = 0; i < (int)w.size(); i++)
        if (i != skip1 && i != skip2)
            k = (k << LETTER_BITS) | (unsigned)(w[i] - 'a' + 1);
    return (k << LOW_BITS) | low;
}

unsigned lowOf(Key x) { return (unsigned)(x & (((Key)1 << LOW_BITS) - 1)); }
unsigned cutOf(unsigned low) { return low >> (2 * GAP_BITS) & CUT_MASK; }

// marks the words of one rest that have a close word in it; the keys of one
// word differ in their gaps, so equal pairs come from different words
void markGroup(const vector<Key> &keys, size_t start, size_t end, vector<bool> &found) {
    vector<unsigned> singles, doubles;
    for (size_t t = start; t < end; t++) {
        unsigned low = lowOf(keys[t]);
        if (cutOf(low) == 0) {
            // the rest is a word itself, at most two deletions from every other
            for (size_t u = start; u < end; u++)
                found[lowOf(keys[u]) >> ID_SHIFT] = true;
            return;
        }
        (cutOf(low) == 1 ? singles : doubles).push_back(low);
    }
    bool gapsWith[GAP_MASK + 1] = {}, nearGap[GAP_MASK + 1] = {}, many = false;
    for (unsigned low : singles) {
        gapsWith[low & GAP_MASK] = true;
        many = many || low >> ID_SHIFT != singles[0] >> ID_SHIFT;
    }
    // one deletion from each costs at most two edits
    if (many)
        for (unsigned low : singles)
            found[low >> ID_SHIFT] = true;
    sort(doubles.begin(), doubles.end(),
         [](unsigned a, unsigned b) { return (a & PAIR_MASK) < (b & PAIR_MASK); });
    for (size_t a = 0; a < doubles.size(); a++) {
        unsigned low = doubles[a], g1 = low >> GAP_BITS & GAP_MASK, g2 = low & GAP_MASK;
        // the same two gaps: two substitutions
        bool same = (a > 0 && (doubles[a - 1] & PAIR_MASK) == (low & PAIR_MASK)) ||
                    (a + 1 < doubles.size() && (doubles[a + 1] & PAIR_MASK) == (low & PAIR_MASK));
        // one more letter in a gap shared with a single deletion
        bool near = gapsWith[g1] || gapsWith[g2];
        if (same || near)
            found[low >> ID_SHIFT] = true;
        if (near)
            nearGap[g1] = nearGap[g2] = true;
    }
    for (unsigned low : singles)
        if (nearGap[low & GAP_MASK])
            found[low >> ID_SHIFT] = true;
}

int main() {
    int k;
    cin >> k;
    vector<string> words(k);
    for (auto &w : words)
        cin >> w;
    // two words are at most two edits apart when deleting at most two letters
    // from each leaves the same rest and, gap by gap of the rest, the larger
    // number of deleted letters adds up to at most two
    vector<Key> keys;
    for (int id = 0; id < k; id++) {
        const string &w = words[id];
        int n = w.size();
        unsigned tag = (unsigned)id << ID_SHIFT;
        keys.push_back(pack(w, -1, -1, tag));
        for (int i = 0; i < n; i++) {
            keys.push_back(pack(w, i, -1, tag | 1u << (2 * GAP_BITS) | i));
            // the second deleted letter, w[j + 1], sits in gap j of the rest
            for (int j = i; j < n - 1; j++)
                keys.push_back(pack(w, i, j + 1, tag | 2u << (2 * GAP_BITS) | i << GAP_BITS | j));
        }
    }
    sort(keys.begin(), keys.end());
    vector<bool> found(k, false);
    size_t start = 0;
    while (start < keys.size()) {
        size_t end = start + 1;
        while (end < keys.size() && keys[end] >> LOW_BITS == keys[start] >> LOW_BITS)
            end++;
        if (end - start > 1)
            markGroup(keys, start, end, found);
        start = end;
    }
    vector<string> chosen;
    for (int id = 0; id < k; id++)
        if (found[id])
            chosen.push_back(words[id]);
    sort(chosen.begin(), chosen.end());
    string out = to_string(chosen.size()) + "\n";
    for (auto &w : chosen)
        out += w + "\n";
    fputs(out.c_str(), stdout);
}
