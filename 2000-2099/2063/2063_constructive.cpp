#include <cstdint>
#include <cstdio>
#include <iostream>
#include <iterator>
#include <string>

using namespace std;

// FNV-1a of the whole input seeds splitmix64; the arrangements are never
// decoded, they only make the seed differ between tests
constexpr uint64_t FNV_OFFSET = 0xcbf29ce484222325ULL;
constexpr uint64_t FNV_PRIME = 0x100000001b3ULL;
constexpr uint64_t GOLDEN = 0x9e3779b97f4a7c15ULL;
constexpr uint64_t MIX_A = 0xbf58476d1ce4e5b9ULL;
constexpr uint64_t MIX_B = 0x94d049bb133111ebULL;
constexpr int SHIFT_A = 30, SHIFT_B = 27, SHIFT_C = 31;

uint64_t state;

uint64_t next_random() {
    uint64_t z = state += GOLDEN;
    z = (z ^ (z >> SHIFT_A)) * MIX_A;
    z = (z ^ (z >> SHIFT_B)) * MIX_B;
    return z ^ (z >> SHIFT_C);
}

int main() {
    string input((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    state = FNV_OFFSET;
    for (unsigned char c : input) state = (state ^ c) * FNV_PRIME;
    int games = stoi(input);
    string out;
    for (int game = 0; game < games; ++game) {
        int n = game + 2;
        // a bubble sort network: every white ball ends left of every black one
        for (int end = n - 1; end >= 1; --end)
            for (int i = 1; i <= end; ++i)
                out += "? " + to_string(i) + " " + to_string(i + 1) + "\n";
        int j = 1 + int(next_random() % uint64_t(n - 1));
        out += "! " + to_string(j) + " " + to_string(j + 1) + "\n";
    }
    fwrite(out.data(), 1, out.size(), stdout);
}
