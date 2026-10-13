import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final int CAMEL = 1;
    static final int FIELDS = 3; // a, b and the kind

    static int gcd(int x, int y) {
        while (y != 0) {
            int t = x % y;
            x = y;
            y = t;
        }
        return x;
    }

    // animals[i] = {a, b, kind}: a ray from the origin, reduced by the gcd
    static long cross(int[] p, int[] q) { return (long)p[0] * q[1] - (long)p[1] * q[0]; }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[][] animals = new int[n][];
        boolean origin = false;
        for (int i = 0; i < n; i++) {
            int[] x = new int[FIELDS];
            for (int k = 0; k < x.length; k++) {
                in.nextToken();
                x[k] = (int)in.nval;
            }
            int g = gcd(x[0], x[1]);
            if (g == 0) {
                origin = true; // nobody can judge an animal at the origin
            } else {
                x[0] /= g;
                x[1] /= g;
            }
            animals[i] = x;
        }
        if (origin) {
            System.out.println(-1);
            return;
        }
        // rays by angle, counterclockwise from the A axis
        Arrays.sort(animals, (p, q) -> Long.signum(cross(q, p)));
        List<int[]> experts = new ArrayList<>();
        for (int i = 0; i + 1 < n; i++) {
            int[] p = animals[i], q = animals[i + 1];
            if (cross(p, q) == 0) {
                if (p[2] != q[2]) {
                    System.out.println(-1); // every expert judges a whole ray alike
                    return;
                }
                continue;
            }
            if (p[2] == q[2])
                continue;
            // a line along p + q passes strictly between the two rays
            int x = p[0] + q[0], y = p[1] + q[1], g = gcd(x, y);
            x /= g;
            y /= g;
            experts.add(p[2] == CAMEL ? new int[] {y, -x} : new int[] {-y, x});
        }
        if (experts.size() % 2 == 0) {
            // an odd count avoids ties; one more expert votes for the first kind
            int s = animals[0][2] == CAMEL ? 1 : -1;
            experts.add(new int[] {s, s});
        }
        StringBuilder out = new StringBuilder();
        out.append(experts.size()).append('\n');
        for (int[] e : experts)
            out.append(e[0]).append(' ').append(e[1]).append('\n');
        System.out.print(out);
    }
}
