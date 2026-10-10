import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {
    // anything that is not a digit acts like a digit too large for every base
    static final int WALL = 36, SMALLEST = 2, BUFFER = 1 << 16;

    static int value(int ch) {
        if (ch >= '0' && ch <= '9') {
            return ch - '0';
        }
        if (ch >= 'A' && ch <= 'Z') {
            return ch - 'A' + 10;
        }
        return WALL;
    }

    public static void main(String[] args) throws IOException {
        InputStream in = new BufferedInputStream(System.in, BUFFER);
        // a number in base k starts at every digit below k whose left
        // neighbour is k or more, so each neighbouring pair (left, right) with
        // right < left starts a number in the bases right + 1 .. left
        long[][] pairs = new long[WALL + 1][WALL + 1];
        int left = WALL;
        for (int ch = in.read(); ch != -1; ch = in.read()) {
            int right = value(ch);
            pairs[left][right]++;
            left = right;
        }
        long[] count = new long[WALL + 2];
        for (int l = 1; l <= WALL; l++) {
            for (int r = 0; r < l; r++) {
                count[Math.max(r + 1, SMALLEST)] += pairs[l][r];
                count[l + 1] -= pairs[l][r];
            }
        }
        long best = -1, running = 0;
        int bestK = SMALLEST;
        for (int k = 0; k <= WALL; k++) {
            running += count[k];
            if (k >= SMALLEST && running > best) {
                best = running;
                bestK = k;
            }
        }
        System.out.println(bestK + " " + best);
    }
}
