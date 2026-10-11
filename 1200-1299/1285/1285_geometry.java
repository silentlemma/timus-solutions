import java.io.*;
import java.util.*;

public class Main {
    static final int DIM = 8;
    static final int POINTS = 3;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        long[][] p = new long[POINTS][DIM];
        for (long[] v : p)
            for (int i = 0; i < DIM; i++) {
                in.nextToken();
                v[i] = (long)in.nval;
            }
        in.nextToken();
        long r = (long)in.nval;
        long[] a = p[0], b = p[1], c = p[2];
        long length2 = 0, ca2 = 0, cb2 = 0, dot = 0;
        for (int i = 0; i < DIM; i++) {
            long ab = b[i] - a[i], ac = c[i] - a[i], bc = c[i] - b[i];
            length2 += ab * ab;
            ca2 += ac * ac;
            cb2 += bc * bc;
            dot += ab * ac;
        }
        // the segment enters the ball when the closest point of it to C lies
        // strictly inside; outside 0 <= t <= 1 the closest point is an end, and
        // both ends are outside: |AC|^2 |AB|^2 - (AB . AC)^2 < R^2 |AB|^2
        if (length2 == 0 || dot <= 0 || dot >= length2 ||
            ca2 * length2 - dot * dot >= r * r * length2) {
            System.out.println(String.format(Locale.ROOT, "%.2f", Math.sqrt(length2)));
            return;
        }
        // otherwise, in the plane of A, B and C: a tangent from A, an arc of the
        // great circle and a tangent to B
        double da = Math.sqrt(ca2), db = Math.sqrt(cb2);
        double angle = Math.acos(Math.max(-1, Math.min(1, (ca2 + cb2 - length2) / (2 * da * db))));
        double arc = angle - Math.acos(r / da) - Math.acos(r / db);
        double total = Math.sqrt(ca2 - r * r) + Math.sqrt(cb2 - r * r) + r * arc;
        System.out.println(String.format(Locale.ROOT, "%.2f", total));
    }
}
