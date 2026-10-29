import java.io.IOException;
import java.math.BigDecimal;
import java.math.RoundingMode;

public class Main {
    static final int BUFFER_SIZE = 1024;
    static final int DECIMAL_PLACES = 2;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, length;

    // the input is read in 1 KB blocks and each number is cut out by hand,
    // which needs less memory than Scanner
    static int read() throws IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length <= 0)
                return -1;
        }
        return buffer[position++];
    }

    static double nextDouble() throws IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        StringBuilder token = new StringBuilder();
        while (c > ' ') {
            token.append((char)c);
            c = read();
        }
        return Double.parseDouble(token.toString());
    }

    public static void main(String[] args) throws IOException {
        int n = (int)nextDouble();
        double r = nextDouble();
        double firstX = nextDouble(), firstY = nextDouble();
        // the polygon is walked while reading, so the nails are never stored
        double previousX = firstX, previousY = firstY;
        // the straight parts are the sides of the polygon, the arcs around the
        // nails turn by 2*pi in total: one full circle of radius r
        double length = 2 * Math.PI * r;
        for (int i = 1; i < n; i++) {
            double x = nextDouble(), y = nextDouble();
            length += Math.hypot(x - previousX, y - previousY);
            previousX = x;
            previousY = y;
        }
        length += Math.hypot(firstX - previousX, firstY - previousY);
        // the shortest decimal form from BigDecimal.valueOf is rounded half up, as
        // String.format does
        System.out.println(BigDecimal.valueOf(length)
                               .setScale(DECIMAL_PLACES, RoundingMode.HALF_UP)
                               .toPlainString());
    }
}
