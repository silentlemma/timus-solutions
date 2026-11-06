#include <iostream>
#include <string>

void restore(std::string &word, int size) {
    const int length = static_cast<int>(word.size());
    const int modulus = size + 1;
    int weight = 0;
    for (int i = 0; i < length; ++i)
        if (word[i] == '1')
            weight += i + 1;
    int residue = weight % modulus;
    if (length == size) {
        if (residue != 0)
            word[residue - 1] = '0';
    } else if (length < size) {
        // The residue includes the extra position of every one to the right.
        for (int i = length; i >= 0; --i) {
            if (residue == 0 || residue + i + 1 == modulus) {
                word.insert(i, 1, residue == 0 ? '0' : '1');
                return;
            }
            if (i > 0 && word[i - 1] == '1' && ++residue == modulus)
                residue = 0;
        }
    } else {
        // The last received position equals the modulus and contributes zero.
        int position_residue = 0;
        for (int i = length - 1; i >= 0; --i) {
            const bool one = word[i] == '1';
            if (residue == (one ? position_residue : 0)) {
                word.erase(i, 1);
                return;
            }
            if (one)
                residue = residue == 0 ? modulus - 1 : residue - 1;
            position_residue = i;
        }
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size;
    if (!(std::cin >> size))
        return 0;
    std::string word;
    word.reserve(size + 1);
    while (std::cin >> word) {
        restore(word, size);
        std::cout << word << '\n';
    }
}
