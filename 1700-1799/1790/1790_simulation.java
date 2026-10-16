import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static DataInputStream in = new DataInputStream(System.in);

    static int readInt() throws IOException {
        int c = in.read();
        while (c < '0') c = in.read();
        int v = 0;
        while (c >= '0') {
            v = v * 10 + (c - '0');
            c = in.read();
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        // lo[p], hi[p]: the pedestals lo, lo + 2, ..., hi of parity p where
        // the artifact may be; empty when lo > hi
        int[] lo = {2, 1};
        int[] hi = {n - n % 2, n - 1 + n % 2};
        for (int i = 0; i < m; i++) {
            int x = readInt(), p = x % 2;
            // a touch inside the run leaves a hole that the next move fills
            // again, so only a touch at an end shrinks it
            if (lo[p] <= hi[p]) {
                if (x == lo[p]) {
                    lo[p] += 2;
                } else if (x == hi[p]) {
                    hi[p] -= 2;
                }
            }
            // every step flips the parity of the pedestal
            int[] newLo = new int[2], newHi = new int[2];
            for (int q = 0; q < 2; q++) {
                if (lo[q] > hi[q]) {
                    newLo[1 - q] = 1;
                    newHi[1 - q] = 0;
                } else {
                    newLo[1 - q] = lo[q] > 1 ? lo[q] - 1 : lo[q] + 1;
                    newHi[1 - q] = hi[q] < n ? hi[q] + 1 : hi[q] - 1;
                }
            }
            lo = newLo;
            hi = newHi;
        }
        System.out.println(lo[0] > hi[0] && lo[1] > hi[1] ? "YES" : "NO");
    }
}
