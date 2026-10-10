import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    // coordinates have at most three decimals, so in thousandths they are
    // exact integers and every turn below is decided without rounding
    static final double SCALE = 1000;

    static int half(long[] p) { return p[1] > 0 || (p[1] == 0 && p[0] > 0) ? 0 : 1; }

    static long cross(long[] p, long[] q) { return p[0] * q[1] - p[1] * q[0]; }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = br.readLine(); line != null; line = br.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer in = new StringTokenizer(all.toString());
        long hx = Math.round(Double.parseDouble(in.nextToken()) * SCALE);
        long hy = Math.round(Double.parseDouble(in.nextToken()) * SCALE);
        int n = Integer.parseInt(in.nextToken());
        // x, y relative to the house, then the id
        long[][] friends = new long[n][];
        for (int i = 0; i < n; i++) {
            long x = Math.round(Double.parseDouble(in.nextToken()) * SCALE) - hx;
            long y = Math.round(Double.parseDouble(in.nextToken()) * SCALE) - hy;
            friends[i] = new long[] {x, y, Long.parseLong(in.nextToken())};
        }
        Arrays.sort(friends,
                    (p, q) -> half(p) != half(q) ? half(p) - half(q) : -Long.signum(cross(p, q)));
        // consecutive friends by angle, joined in turn, never cross; the house
        // closes the loop across one angular gap, which must be the one wider
        // than half a turn if there is one
        int start = 0;
        for (int i = 0; i < n; i++) {
            if (cross(friends[(i + n - 1) % n], friends[i]) < 0) {
                start = i;
            }
        }
        StringBuilder out = new StringBuilder("0\n");
        for (int k = 0; k < n; k++) {
            out.append(friends[(start + k) % n][2]).append('\n');
        }
        System.out.print(out.append("0\n"));
    }
}
