import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        FastInput in = new FastInput();
        long cx = in.nextLong();
        long cy = in.nextLong();
        long r = in.nextLong();
        long ax = in.nextLong();
        long ay = in.nextLong();
        long bx = in.nextLong();
        long by = in.nextLong();
        // The players are equally far from the centre, so the mirror point lies on
        // the bisector of the angle between them, in the direction w = A + B - 2C.
        long wx = ax + bx - 2 * cx;
        long wy = ay + by - 2 * cy;
        // Both shots stay outside the tank exactly when each player is strictly
        // beyond the tangent line at that point: (A - C) . w > r |w|.
        long dot = (ax - cx) * wx + (ay - cy) * wy;
        long norm = wx * wx + wy * wy;
        if (dot <= 0 || dot * dot <= r * r * norm) {
            System.out.println("No way");
            return;
        }
        double scale = r / Math.sqrt((double)norm);
        System.out.println((cx + wx * scale) + " " + (cy + wy * scale));
    }

    // A bounded byte buffer avoids Scanner's regex machinery and temporary tokens.
    static final class FastInput {
        private final byte[] buffer = new byte[4096];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = System.in.read(buffer);
                position = 0;
                if (length < 0)
                    return -1;
            }
            return buffer[position++];
        }

        long nextLong() throws IOException {
            int c;
            do {
                c = read();
            } while (c >= 0 && c <= ' ');
            boolean negative = c == '-';
            if (negative)
                c = read();
            long value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = read();
            }
            return negative ? -value : value;
        }

        String next() throws IOException {
            int c;
            do {
                c = read();
            } while (c >= 0 && c <= ' ');
            StringBuilder word = new StringBuilder();
            while (c > ' ') {
                word.append((char)c);
                c = read();
            }
            return word.toString();
        }
    }
}
