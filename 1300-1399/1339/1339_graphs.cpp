#include <cstdio>
#include <vector>

const int NUMBER = 16; // room for one number and a space

int k;
std::vector<int> likes, partner;
std::vector<char> liked, seen;
std::vector<int> chain;

// pair the children along the likes from start, two by two; on an odd
// path the last one, who likes nobody, stays free
void pairAlong(int start) {
    chain.clear();
    for (int v = start; v >= 0 && !seen[v]; v = likes[v]) {
        seen[v] = 1;
        chain.push_back(v);
    }
    for (size_t i = 0; i + 1 < chain.size(); i += 2) {
        partner[chain[i]] = chain[i + 1];
        partner[chain[i + 1]] = chain[i];
    }
}

int main() {
    if (scanf("%d", &k) != 1)
        return 0;
    // children 0..k-1 are boys and k..2k-1 girls; likes[v] is the child v
    // likes, or -1; nobody is liked by two, so the likes form paths and cycles
    likes.assign(2 * k, -1);
    partner.assign(2 * k, -1);
    liked.assign(2 * k, 0);
    seen.assign(2 * k, 0);
    for (int i = 0; i < 2 * k; i++) {
        int x = 0;
        if (scanf("%d", &x) != 1)
            return 0;
        if (x != 0) {
            likes[i] = i < k ? k + x - 1 : x - 1;
            liked[likes[i]] = 1;
        }
    }
    for (int v = 0; v < 2 * k; v++) {
        if (!liked[v])
            pairAlong(v);
    }
    for (int v = 0; v < 2 * k; v++) {
        if (!seen[v])
            pairAlong(v); // what is left are cycles, always of even length
    }
    // the free children like nobody and can be paired in any way
    int g = k;
    for (int b = 0; b < k; b++) {
        if (partner[b] >= 0)
            continue;
        while (partner[g] >= 0)
            g++;
        partner[b] = g;
        partner[g] = b;
    }
    std::vector<char> out;
    char buffer[NUMBER];
    for (int i = 0; i < k; i++) {
        int length =
            snprintf(buffer, sizeof buffer, i + 1 < k ? "%d " : "%d\n", partner[i] - k + 1);
        out.insert(out.end(), buffer, buffer + length);
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
