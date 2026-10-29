#include <cstdio>

constexpr int LOW_MARK = 3;
constexpr int TOP_MARK = 5;
constexpr int DOUBLED_THRESHOLD = 9;

const char *classify(int count, int total, int lowest) {
    if (lowest == LOW_MARK)
        return "None";
    if (lowest == TOP_MARK)
        return "Named";
    if (2 * total >= DOUBLED_THRESHOLD * count)
        return "High";
    return "Common";
}

// scanf and puts instead of iostream and std::string
int main() {
    int count;
    if (scanf("%d", &count) != 1)
        return 0;
    int total = 0, lowest = TOP_MARK;
    for (int i = 0; i < count; ++i) {
        int grade;
        scanf("%d", &grade);
        total += grade;
        if (grade < lowest)
            lowest = grade;
    }
    puts(classify(count, total, lowest));
}
