import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int MAX_COORD = 100, SPAN = 2 * MAX_COORD + 1;
    static int nextInt(BufferedInputStream in) throws IOException {
        int symbol;
        do {
            symbol = in.read();
        } while (symbol <= ' ' && symbol != -1);
        int sign = 1;
        if (symbol == '-' || symbol == '+') {
            if (symbol == '-')
                sign = -1;
            symbol = in.read();
        }
        int value = 0;
        while (symbol > ' ') {
            value = value * 10 + symbol - '0';
            symbol = in.read();
        }
        return sign * value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        int n = nextInt(in), left = 0, right = 0, lower = 0, upper = 0;
        int[] points = new int[n];
        for (int i = 0; i < n; i++) {
            int x = nextInt(in), y = nextInt(in);
            left = Math.min(left, x);
            right = Math.max(right, x);
            lower = Math.min(lower, y);
            upper = Math.max(upper, y);
            points[i] = (y + MAX_COORD) * SPAN + x + MAX_COORD;
        }
        Arrays.sort(points);
        int width = right - left + 1, next = n - 1;
        byte[] vertical = new byte[width], row = new byte[width + 1];
        Arrays.fill(vertical, (byte)'.');
        vertical[-left] = '|';
        row[width] = '\n';
        BufferedOutputStream out = new BufferedOutputStream(System.out);
        // Packed coordinates sort by y; each row needs only one reusable buffer.
        for (int y = upper; y >= lower; y--) {
            if (y == 0) {
                Arrays.fill(row, 0, width, (byte)'-');
                row[-left] = '+';
            } else
                System.arraycopy(vertical, 0, row, 0, width);
            while (next >= 0 && points[next] / SPAN == y + MAX_COORD) {
                int x = points[next--] % SPAN - MAX_COORD;
                row[x - left] = '*';
            }
            out.write(row);
        }
        out.flush();
    }
}
