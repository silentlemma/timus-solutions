#include <cstdint>
#include <cstdio>
#include <cstring>

constexpr int MAX_LENGTH = 100, DECIMAL_BASE = 10, BRACKETS = 2;
char text[MAX_LENGTH + 1];
uint8_t best[MAX_LENGTH][MAX_LENGTH], lcp[MAX_LENGTH + 1][MAX_LENGTH + 1];
int8_t choice[MAX_LENGTH][MAX_LENGTH];
uint8_t digits[MAX_LENGTH + 1];

void emit(int left, int right) {
    int decision = choice[left][right];
    if (decision > 0) {
        emit(left, decision - 1);
        emit(decision, right);
    } else if (decision < 0) {
        int period = -decision;
        printf("%d(", (right - left + 1) / period);
        emit(left, left + period - 1);
        putchar(')');
    } else
        fwrite(text + left, 1, right - left + 1, stdout);
}

int main() {
    if (scanf("%100s", text) != 1)
        return 0;
    int n = strlen(text);
    for (int value = 1; value <= n; ++value)
        digits[value] = digits[value / DECIMAL_BASE] + 1;
    for (int i = n - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            if (text[i] == text[j])
                lcp[i][j] = lcp[i + 1][j + 1] + 1;
        }
    }
    for (int size = 1; size <= n; ++size) {
        for (int left = 0; left + size <= n; ++left) {
            int right = left + size - 1;
            best[left][right] = size;
            for (int split = left + 1; split <= right; ++split) {
                int cost = best[left][split - 1] + best[split][right];
                if (cost < best[left][right]) {
                    best[left][right] = cost;
                    choice[left][right] = split;
                }
            }
            for (int period = 1; period <= size / 2; ++period) {
                // One LCP lookup replaces a full shifted-substring comparison.
                if (size % period != 0 || lcp[left][left + period] < size - period)
                    continue;
                int cost = digits[size / period] + BRACKETS + best[left][left + period - 1];
                if (cost < best[left][right]) {
                    best[left][right] = cost;
                    choice[left][right] = -period;
                }
            }
        }
    }
    emit(0, n - 1);
    putchar('\n');
}
