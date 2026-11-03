#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>

const int MAX_PHONE = 100, MAX_WORD_LENGTH = 50, MAX_NODES = MAX_PHONE * MAX_WORD_LENGTH + 1;
const char *const KEYPAD = "22233344115566070778889990";
int edges[MAX_NODES][10];
std::string words[MAX_NODES];

int main() {
    char phone[MAX_PHONE + 1], word[MAX_WORD_LENGTH + 1];
    int previousNodes = 1;
    while (scanf("%100s", phone) == 1 && strcmp(phone, "-1") != 0) {
        for (int node = 0; node < previousNodes; node++) {
            std::fill(edges[node], edges[node] + 10, 0);
            words[node].clear();
        }
        int n = strlen(phone), nodes = 1, count;
        scanf("%d", &count);
        // Build only substrings that occur in this phone. Unrelated dictionary
        // words never allocate nodes, unlike a trie of the entire dictionary.
        for (int start = 0; start < n; start++) {
            int node = 0;
            for (int end = start; end < std::min(n, start + MAX_WORD_LENGTH); end++) {
                int &next = edges[node][phone[end] - '0'];
                if (next == 0)
                    next = nodes++;
                node = next;
            }
        }
        while (count--) {
            scanf("%50s", word);
            int node = 0;
            for (int i = 0; word[i]; i++) {
                node = edges[node][KEYPAD[word[i] - 'a'] - '0'];
                if (node == 0)
                    break;
            }
            if (node && words[node].empty())
                words[node] = word;
        }
        previousNodes = nodes;
        std::vector<int> best(n + 1, n + 1), how(n + 1);
        best[0] = 0;
        for (int start = 0; start < n; start++) {
            if (best[start] > n)
                continue;
            int node = 0;
            for (int end = start; end < std::min(n, start + MAX_WORD_LENGTH); end++) {
                node = edges[node][phone[end] - '0'];
                if (!words[node].empty() && best[start] + 1 < best[end + 1]) {
                    best[end + 1] = best[start] + 1;
                    how[end + 1] = node;
                }
            }
        }
        if (best[n] > n) {
            puts("No solution.");
            continue;
        }
        std::vector<int> used;
        for (int position = n; position; position -= words[how[position]].size())
            used.push_back(how[position]);
        for (int i = int(used.size()) - 1; i >= 0; i--)
            printf("%s%c", words[used[i]].c_str(), i ? ' ' : '\n');
    }
}
