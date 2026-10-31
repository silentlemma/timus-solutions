import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static final int KEYS = 10;
    static final double HALF = Math.sqrt(1.0 / 2); // each axis of a diagonal jump
    // the numeric keypad: the jump of each key in steps east and north
    static final int[] DX = {0, -1, 0, 1, -1, 0, 1, -1, 0, 1};
    static final int[] DY = {0, -1, -1, -1, 0, 0, 0, 1, 1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        long[] times = new long[KEYS];
        boolean stopped = false;
        for (String line; (line = in.readLine()) != null;) {
            for (int i = 0; i < line.length(); i++) {
                char c = line.charAt(i);
                if (c == '0')
                    stopped = true;
                if (!stopped && c > '0' && c <= '9')
                    times[c - '0']++;
            }
        }
        // straight jumps add whole metres, diagonal ones 1/sqrt(2) on each axis
        long sx = 0, sy = 0, dx = 0, dy = 0;
        for (int k = 0; k < KEYS; k++)
            if (DX[k] != 0 && DY[k] != 0) {
                dx += DX[k] * times[k];
                dy += DY[k] * times[k];
            } else {
                sx += DX[k] * times[k];
                sy += DY[k] * times[k];
            }
        double x = sx + dx * HALF, y = sy + dy * HALF;
        System.out.println(String.format(java.util.Locale.US, "%.10f %.10f", x, y));
    }
}
