#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

const unsigned long long LIMB = 1000000000;  // the big number is kept in base 10^9

int main() {
    unsigned long long n;
    std::string word;
    std::cin >> n >> word;
    int size = word.size();
    // prefix function: pi[i] is the longest border of word[0..i]
    std::vector<int> pi(size, 0);
    for (int i = 1; i < size; i++) {
        int j = pi[i - 1];
        while (j > 0 && word[i] != word[j]) {
            j = pi[j - 1];
        }
        if (word[i] == word[j]) {
            j++;
        }
        pi[i] = j;
    }
    // the expected time is the sum of n^k over the lengths k of the word's
    // borders, the whole word included: a number whose base-n digits are 0
    // and 1, built by Horner's rule from the top digit down
    std::vector<int> border(size + 1, 0);
    for (int k = size; k > 0; k = pi[k - 1]) {
        border[k] = 1;
    }
    std::vector<unsigned long long> total = {0};  // limbs, lowest first
    auto times_plus = [&](unsigned long long mul, unsigned long long add) {
        unsigned long long carry = add;
        for (unsigned long long& limb : total) {
            unsigned long long cur = limb * mul + carry;
            limb = cur % LIMB;
            carry = cur / LIMB;
        }
        while (carry > 0) {
            total.push_back(carry % LIMB);
            carry /= LIMB;
        }
    };
    for (int k = size; k > 0; k--) {
        times_plus(n, border[k]);
    }
    times_plus(n, 0);
    printf("%llu", total.back());
    for (int i = (int)total.size() - 2; i >= 0; i--) {
        printf("%09llu", total[i]);
    }
    printf("\n");
}
