import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static long nextLong() throws IOException {
        int ch;
        do {
            ch = INPUT.read();
        } while (ch <= ' ' && ch != -1);
        long value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = INPUT.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int n = (int) nextLong();
        int m = (int) nextLong();
        int a = (int) nextLong();
        int b = (int) nextLong();
        long rowTotal = 0;
        long columnTotal = 0;
        long selectedRow = 0;
        long selectedColumn = 0;
        for (int i = 1; i <= n; ++i) {
            long value = nextLong();
            rowTotal += value;
            if (i == a) {
                selectedRow = value;
            }
        }
        for (int j = 1; j <= m; ++j) {
            long value = nextLong();
            columnTotal += value;
            if (j == b) {
                selectedColumn = value;
            }
        }

        if (rowTotal != columnTotal) {
            System.out.println(0);
            return;
        }
        long lower = Math.max(0, selectedRow + selectedColumn - rowTotal);
        long upper = Math.min(selectedRow, selectedColumn);
        System.out.println(upper - lower + 1);
    }
}
