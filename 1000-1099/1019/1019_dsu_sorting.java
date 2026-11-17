import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int LINE_END = 1_000_000_000;

    static int token(BufferedInputStream input) throws IOException {
        int ch;
        do {
            ch = input.read();
        } while (ch >= 0 && ch <= ' ');
        if (ch < '0' || ch > '9') {
            return ch;
        }
        int value = 0;
        do {
            value = value * 10 + ch - '0';
            ch = input.read();
        } while (ch >= '0' && ch <= '9');
        return value;
    }

    static int find(int[] next, int i) {
        while (next[i] != i) {
            next[i] = next[next[i]];
            i = next[i];
        }
        return i;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int n = token(input);
        int[] operations = new int[2 * n];
        int[] coordinate = new int[2 * n + 2];
        byte[] black = new byte[n];
        for (int i = 0; i < n; i++) {
            coordinate[2 * i] = operations[2 * i] = token(input);
            coordinate[2 * i + 1] = operations[2 * i + 1] = token(input);
            black[i] = (byte)(token(input) == 'b' ? 1 : 0);
        }
        coordinate[2 * n + 1] = LINE_END;
        Arrays.sort(coordinate);
        int count = 1;
        for (int i = 1; i < coordinate.length; i++) {
            if (coordinate[i] != coordinate[count - 1]) {
                coordinate[count++] = coordinate[i];
            }
        }

        int[] next = new int[count];
        byte[] piece = new byte[count - 1];
        for (int i = 0; i < count; i++) {
            next[i] = i;
        }
        for (int i = n - 1; i >= 0; i--) {
            int left = Arrays.binarySearch(coordinate, 0, count, operations[2 * i]);
            int right = Arrays.binarySearch(coordinate, 0, count, operations[2 * i + 1]);
            for (int at = find(next, left); at < right; at = next[at]) {
                piece[at] = black[i];
                next[at] = find(next, at + 1);
            }
        }

        int bestLeft = 0, bestRight = 0, left = 0;
        for (int i = 0; i < piece.length; i++) {
            if (piece[i] != 0) {
                left = i + 1;
            } else if (coordinate[i + 1] - coordinate[left] > bestRight - bestLeft) {
                bestLeft = coordinate[left];
                bestRight = coordinate[i + 1];
            }
        }
        System.out.println(bestLeft + " " + bestRight);
    }
}
