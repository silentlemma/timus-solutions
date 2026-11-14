#include <algorithm>
#include <cstdio>
#include <vector>

constexpr int MAX_SALARY = 1000000000;
constexpr int BUFFER_SIZE = 8192;

class Input {
    unsigned char buffer[BUFFER_SIZE];
    std::size_t position = 0, length = 0;

    int byte() {
        if (position == length) {
            length = std::fread(buffer, 1, sizeof buffer, stdin);
            position = 0;
            if (!length)
                return EOF;
        }
        return buffer[position++];
    }

  public:
    int number() {
        int c = byte();
        while (c != EOF && c <= ' ')
            c = byte();
        const bool negative = c == '-';
        if (negative)
            c = byte();
        int result = 0;
        for (; c >= '0' && c <= '9'; c = byte())
            result = result * 10 + c - '0';
        return negative ? -result : result;
    }
};

struct Employee {
    int parent = -1;
    int offset = 0;
    int low = 0, high = MAX_SALARY;
};

int find(std::vector<Employee> &staff, int v) {
    Employee &node = staff[v];
    if (node.parent < 0)
        return v;
    const int parent = node.parent;
    const int root = find(staff, parent);
    node.offset += staff[parent].offset;
    node.parent = root;
    return root;
}

int main() {
    Input input;
    const int people = input.number();
    const int statements = input.number();
    std::vector<Employee> staff(people);
    staff[0].high = 0;

    for (int k = 1; k <= statements; ++k) {
        const int a = input.number();
        const int b = input.number();
        const int difference = input.number();
        int left = find(staff, a), right = find(staff, b);
        int shift = staff[a].offset - staff[b].offset - difference;
        bool consistent = shift == 0;
        if (left != right) {
            if (staff[left].parent > staff[right].parent) {
                std::swap(left, right);
                shift = -shift;
            }
            Employee &root = staff[left];
            Employee &child = staff[right];
            root.low = std::max(root.low, child.low - shift);
            root.high = std::min(root.high, child.high - shift);
            consistent = root.low <= root.high;
            root.parent += child.parent;
            child.parent = left;
            child.offset = shift;
        }
        if (!consistent) {
            std::printf("Impossible after %d statements\n", k);
            return 0;
        }
    }

    std::puts("Possible");
    for (int v = 0; v < people; ++v) {
        const int root = find(staff, v);
        std::printf("%d\n", staff[root].low + staff[v].offset);
    }
}
