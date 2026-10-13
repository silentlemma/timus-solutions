import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int SLOTS = 1 << 13; // an open-addressing table, more than twice N
    static final int MIX_Y = 1_000_003;
    static final int MIX_Z = 998_244_353;

    static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] xs = new int[n], ys = new int[n], zs = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            xs[i] = (int)in.nval;
            in.nextToken();
            ys[i] = (int)in.nval;
            in.nextToken();
            zs[i] = (int)in.nval;
        }
        int[] kx = new int[SLOTS], ky = new int[SLOTS], kz = new int[SLOTS], count = new int[SLOTS];
        int[] used = new int[SLOTS];
        int best = 1;
        for (int i = 0; i < n && n - i > best; i++) {
            int same = 0, most = 0, filled = 0;
            for (int j = i + 1; j < n; j++) {
                int dx = xs[j] - xs[i], dy = ys[j] - ys[i], dz = zs[j] - zs[i];
                int g = gcd(Math.abs(dx), gcd(Math.abs(dy), Math.abs(dz)));
                if (g == 0) {
                    same++; // several flies may hang at one point
                    continue;
                }
                // one key per direction: reduced, with the first non-zero part positive
                if (dx < 0 || (dx == 0 && (dy < 0 || (dy == 0 && dz < 0))))
                    g = -g;
                dx /= g;
                dy /= g;
                dz /= g;
                int h = (dx + dy * MIX_Y + dz * MIX_Z) & (SLOTS - 1);
                while (count[h] > 0 && (kx[h] != dx || ky[h] != dy || kz[h] != dz))
                    h = (h + 1) & (SLOTS - 1);
                if (count[h] == 0) {
                    kx[h] = dx;
                    ky[h] = dy;
                    kz[h] = dz;
                    used[filled++] = h;
                }
                most = Math.max(most, ++count[h]);
            }
            for (int k = 0; k < filled; k++)
                count[used[k]] = 0;
            best = Math.max(best, 1 + same + most);
        }
        System.out.println(best);
    }
}
