#include <iostream>
#include <set>
#include <string>

// test 6 was removed and new tests were added after test 7, which became
// test 6: a failure on old test 7 must now read 6, while an accepted run or
// a failure on old test 6 may change or stay as it was
const int REMOVED = 6;
const int RENUMBERED = 7;

int main() {
    int n;
    std::cin >> n;
    std::set<std::string> must, any;
    for (int i = 0; i < n; i++) {
        std::string name, verdict;
        std::cin >> name >> verdict;
        if (verdict == "ML" || verdict == "TL" || verdict == "WA") {
            int test;
            std::cin >> test;
            if (test == RENUMBERED) {
                must.insert(name);
                any.insert(name);
            } else if (test == REMOVED) {
                any.insert(name);
            }
        } else if (verdict == "AC") {
            any.insert(name);
        }
    }
    std::cout << must.size() << " " << any.size() << "\n";
}
