import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    // every n is below 2^60, and a lowered bit leaves at most 60 free ones
    static final int BITS = 61;
    static final int ENDINGS = 4; // per first bit: as is, last bit 1, last two 11, last two 01

    public static void main(String[] args) throws IOException {
        // maps[r][c]: p, q with a = p a_m + q a_m+1 after candidate suffix c of
        // r free bits: alternating bits with the last one or two changed
        long[][][] maps = new long[BITS][2 * ENDINGS][];
        for (int r = 0; r < BITS; r++)
            for (int first = 0; first < 2; first++)
                for (int e = 0; e < ENDINGS; e++) {
                    int[] bits = new int[r];
                    for (int k = 0; k < r; k++)
                        bits[k] = (first + k) % 2;
                    if (e == 1 && r >= 1)
                        bits[r - 1] = 1;
                    if (e >= 2 && r >= 2) {
                        bits[r - 2] = e == 2 ? 1 : 0;
                        bits[r - 1] = 1;
                    }
                    // (a_m, a_m+1) -> (a_2m+bit, a_2m+bit+1), for both unit vectors
                    long px = 1, py = 0, qx = 0, qy = 1;
                    for (int b : bits)
                        if (b == 0) {
                            py += px;
                            qy += qx;
                        } else {
                            px += py;
                            qx += qy;
                        }
                    maps[r][first * ENDINGS + e] = new long[] {px, qx};
                }
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            StringTokenizer st = new StringTokenizer(line);
            if (!st.hasMoreTokens())
                continue;
            long n = Long.parseLong(st.nextToken());
            if (n == 0)
                break;
            int length = Long.SIZE - Long.numberOfLeadingZeros(n);
            long best = 0, x = 0, y = 1; // (a_0, a_1) for the empty prefix
            for (int k = length - 1; k >= 0; k--) {
                if ((n >> k & 1) == 1) {
                    // lower this bit to 0: the k bits below are free
                    long lx = x, ly = x + y;
                    for (long[] pq : maps[k])
                        best = Math.max(best, pq[0] * lx + pq[1] * ly);
                    x += y;
                } else
                    y += x;
            }
            out.append(Math.max(best, x)).append('\n');
        }
        System.out.print(out);
    }
}
