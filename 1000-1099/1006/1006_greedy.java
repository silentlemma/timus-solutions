import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static final int WIDTH = 50, HEIGHT = 20, MIN_SIDE = 2, BUFFER = 1 << 12;
    static final int EMPTY = '.';
    static final int UPPER_LEFT = 218, UPPER_RIGHT = 191, LOWER_LEFT = 192, LOWER_RIGHT = 217;
    static final int VERTICAL = 179, HORIZONTAL = 196;

    static int[][] screen = new int[HEIGHT][WIDTH];
    static boolean[][] peeled = new boolean[HEIGHT][WIDTH];
    static int fresh, left;

    // A peeled cell is covered by a frame drawn later, so it may hold anything.
    static boolean fits(int x, int y, int c) {
        if (peeled[y][x]) {
            return true;
        }
        if (screen[y][x] != c) {
            return false;
        }
        fresh++;
        return true;
    }

    // The frame matches the picture where it is visible and shows something new.
    static boolean frameFits(int x, int y, int side) {
        int last = side - 1;
        fresh = 0;
        if (!fits(x, y, UPPER_LEFT) || !fits(x + last, y, UPPER_RIGHT) ||
            !fits(x, y + last, LOWER_LEFT) || !fits(x + last, y + last, LOWER_RIGHT)) {
            return false;
        }
        for (int i = 1; i < last; i++) {
            if (!fits(x + i, y, HORIZONTAL) || !fits(x + i, y + last, HORIZONTAL) ||
                !fits(x, y + i, VERTICAL) || !fits(x + last, y + i, VERTICAL)) {
                return false;
            }
        }
        return fresh > 0;
    }

    static void peelCell(int x, int y) {
        if (!peeled[y][x]) {
            peeled[y][x] = true;
            left--;
        }
    }

    static void peel(int x, int y, int side) {
        int last = side - 1;
        for (int i = 0; i <= last; i++) {
            peelCell(x + i, y);
            peelCell(x + i, y + last);
            peelCell(x, y + i);
            peelCell(x + last, y + i);
        }
    }

    static byte[] readAll(InputStream in) throws IOException {
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        byte[] buffer = new byte[BUFFER];
        for (int n; (n = in.read(buffer)) > 0;) {
            bytes.write(buffer, 0, n);
        }
        return bytes.toByteArray();
    }

    public static void main(String[] args) throws IOException {
        byte[] data = readAll(System.in);
        int pos = 0;
        for (int y = 0; y < HEIGHT; y++) {
            for (int x = 0; x < WIDTH; x++) {
                int c = EMPTY;
                if (pos < data.length && data[pos] != '\n' && data[pos] != '\r') {
                    c = Byte.toUnsignedInt(data[pos++]);
                }
                screen[y][x] = c;
                if (c != EMPTY) {
                    left++;
                }
            }
            while (pos < data.length && data[pos] != '\n') {
                pos++;
            }
            pos++;
        }

        // Undo the drawing: a frame that fits can be the last one drawn among the
        // remaining ones; its cells then may hold anything.
        List<int[]> frames = new ArrayList<>();
        while (left > 0) {
            int before = left;
            for (int y = 0; y < HEIGHT; y++) {
                for (int x = 0; x < WIDTH; x++) {
                    for (int side = MIN_SIDE; x + side <= WIDTH && y + side <= HEIGHT; side++) {
                        if (frameFits(x, y, side)) {
                            frames.add(new int[] {x, y, side});
                            peel(x, y, side);
                        }
                    }
                }
            }
            if (left == before) {
                break;
            }
        }

        StringBuilder out = new StringBuilder();
        out.append(frames.size()).append('\n');
        for (int i = frames.size() - 1; i >= 0; i--) {
            int[] f = frames.get(i);
            out.append(f[0]).append(' ').append(f[1]).append(' ').append(f[2]).append('\n');
        }
        System.out.print(out);
    }
}
