#include <cstdint>
#include <cstdio>

constexpr int MAX_LENGTH = 100000, ROOT_COUNT = 2, EMPTY_ROOT = 1;

struct Node {
    int32_t length;
    uint32_t link, child, sibling;
    char letter;
};

Node nodes[MAX_LENGTH + ROOT_COUNT];
char text[MAX_LENGTH + 1];

uint32_t transition(uint32_t parent, char letter) {
    // A palindrome has one inner palindrome: its incoming edge can live in its own node.
    for (uint32_t edge = nodes[parent].child; edge != 0; edge = nodes[edge].sibling)
        if (nodes[edge].letter == letter)
            return edge;
    return 0;
}

int main() {
    if (scanf("%100000s", text) != 1)
        return 0;
    nodes[0].length = -1;
    uint32_t count = ROOT_COUNT, last = EMPTY_ROOT;
    for (int position = 0; text[position] != '\0'; ++position) {
        char letter = text[position];
        uint32_t parent = last;
        while (true) {
            int left = position - nodes[parent].length - 1;
            if (left >= 0 && text[left] == letter)
                break;
            parent = nodes[parent].link;
        }
        uint32_t node = transition(parent, letter);
        if (node == 0) {
            node = count++;
            nodes[node].length = nodes[parent].length + 2;
            nodes[node].letter = letter;
            nodes[node].sibling = nodes[parent].child;
            nodes[parent].child = node;
            if (nodes[node].length == 1)
                nodes[node].link = EMPTY_ROOT;
            else {
                uint32_t candidate = nodes[parent].link;
                while (true) {
                    int left = position - nodes[candidate].length - 1;
                    if (left >= 0 && text[left] == letter)
                        break;
                    candidate = nodes[candidate].link;
                }
                nodes[node].link = transition(candidate, letter);
            }
        }
        last = node;
        printf("%s%u", position == 0 ? "" : " ", count - ROOT_COUNT);
    }
    putchar('\n');
}
