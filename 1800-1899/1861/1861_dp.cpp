#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::string text, name;
    std::cin >> text >> name;
    int n = text.size(), m = name.size();
    // the name can be written from position j on when each of its letters
    // lands on that letter or on a "?"
    std::vector<bool> fits(n - m + 1, true);
    for (int j = 0; j + m <= n; j++) {
        for (int i = 0; i < m && fits[j]; i++) {
            if (text[j + i] != '?' && text[j + i] != name[i]) fits[j] = false;
        }
    }
    // two copies d < m apart agree exactly when d is a period of the name:
    // copies far apart never meet, and a set of copies agrees as soon as each
    // copy agrees with the next one, which covers what lies between
    std::vector<int> border(m, 0), periods;
    for (int i = 1, k = 0; i < m; i++) {
        while (k && name[k] != name[i]) k = border[k - 1];
        if (name[k] == name[i]) k++;
        border[i] = k;
    }
    for (int k = border[m - 1]; k; k = border[k - 1]) periods.push_back(m - k);
    // best[j]: the most copies with the last one at j; before[j]: the most
    // with the last one before j
    std::vector<int> best(n - m + 1, 0), before(n - m + 2, 0);
    for (int j = 0; j + m <= n; j++) {
        if (fits[j]) {
            int previous = j >= m ? before[j - m + 1] : 0;
            for (int d : periods) {
                if (d <= j) previous = std::max(previous, best[j - d]);
            }
            best[j] = previous + 1;
        }
        before[j + 1] = std::max(before[j], best[j]);
    }
    std::cout << before[n - m + 1] << "\n";
    return 0;
}
