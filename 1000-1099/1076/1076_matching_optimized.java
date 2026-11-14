import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int INFINITY = 1 << 20;

    static int readNumber(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = input.read();
        }
        return value;
    }

    static int maximumSaved(byte[][] matrix, int n) {
        int[] rowPrice = new int[n + 1];
        int[] colPrice = new int[n + 1];
        int[] owner = new int[n + 1];
        int[] previous = new int[n + 1];
        int[] unmatched = new int[n];
        int unmatchedCount = 0;
        // Initial row potentials make every row maximum a tight edge.
        for (int row = 1; row <= n; row++) {
            byte[] amounts = matrix[row];
            int largest = 0;
            for (int col = 1; col <= n; col++) {
                largest = Math.max(largest, amounts[col]);
            }
            rowPrice[row] = -largest;
            int col = 1;
            while (col <= n && (owner[col] != 0 || amounts[col] != largest)) {
                col++;
            }
            if (col <= n) {
                owner[col] = row;
            } else {
                unmatched[unmatchedCount++] = row;
            }
        }

        int[] slack = new int[n + 1];
        int[] remaining = new int[n];
        int[] visited = new int[n];
        for (int index = 0; index < unmatchedCount; index++) {
            owner[0] = unmatched[index];
            int col = 0;
            int left = n;
            int visitedCount = 0;
            Arrays.fill(slack, INFINITY);
            for (int pos = 0; pos < n; pos++) {
                remaining[pos] = pos + 1;
            }

            while (true) {
                visited[visitedCount++] = col;
                int activeRow = owner[col];
                byte[] amounts = matrix[activeRow];
                int delta = INFINITY;
                int best = 0;
                for (int pos = 0; pos < left; pos++) {
                    int j = remaining[pos];
                    int reduced = -amounts[j] - rowPrice[activeRow] - colPrice[j];
                    if (reduced < slack[j]) {
                        slack[j] = reduced;
                        previous[j] = col;
                    }
                    boolean preferFree = owner[j] == 0 && owner[remaining[best]] != 0;
                    if (slack[j] < delta || (slack[j] == delta && preferFree)) {
                        delta = slack[j];
                        best = pos;
                    }
                }
                if (delta != 0) {
                    for (int pos = 0; pos < visitedCount; pos++) {
                        int j = visited[pos];
                        rowPrice[owner[j]] += delta;
                        colPrice[j] -= delta;
                    }
                    for (int pos = 0; pos < left; pos++) {
                        slack[remaining[pos]] -= delta;
                    }
                }
                col = remaining[best];
                if (owner[col] == 0) {
                    break;
                }
                remaining[best] = remaining[--left];
            }

            while (col != 0) {
                int prior = previous[col];
                owner[col] = owner[prior];
                col = prior;
            }
        }

        int saved = 0;
        for (int col = 1; col <= n; col++) {
            saved += matrix[owner[col]][col];
        }
        return saved;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int n = readNumber(input);
        byte[][] matrix = new byte[n + 1][n + 1];
        int total = 0;
        for (int row = 1; row <= n; row++) {
            for (int col = 1; col <= n; col++) {
                int value = readNumber(input);
                matrix[row][col] = (byte)value;
                total += value;
            }
        }
        System.out.println(total - maximumSaved(matrix, n));
    }
}
