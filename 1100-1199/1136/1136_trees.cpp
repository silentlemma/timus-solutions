#include <cstdio>
#include <vector>

// a binary search tree in arrays: the number of node v and its children,
// -1 for a missing child
std::vector<int> number, leftChild, rightChild;

void insert(int value) {
    int node = number.size();
    number.push_back(value);
    leftChild.push_back(-1);
    rightChild.push_back(-1);
    for (int v = 0; node > 0;) {
        int &child = value < number[v] ? leftChild[v] : rightChild[v];
        if (child < 0) {
            child = node;
            return;
        }
        v = child;
    }
}

// the even-session order: right wing, left wing, then the chairman
void speak(int v) {
    if (v < 0)
        return;
    speak(rightChild[v]);
    speak(leftChild[v]);
    printf("%d\n", number[v]);
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<int> post(n);
    for (int &v : post)
        if (scanf("%d", &v) != 1)
            return 0;
    // read backwards, the odd-session order names every chairman before the
    // members of the wings, so inserting in that order rebuilds the tree
    for (int k = n - 1; k >= 0; k--)
        insert(post[k]);
    if (n > 0)
        speak(0);
}
