import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Main {
    static final int AXES = 3;

    static long[] cross(long[] a, long[] b) {
        return new long[] {a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
                           a[0] * b[1] - a[1] * b[0]};
    }

    static long dot(long[] a, long[] b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }

    static long gcd(long a, long b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long[][] points = new long[n][AXES];
        for (long[] p : points)
            for (int k = 0; k < AXES; k++)
                p[k] = in.nextLong();

        // every plane through the origin and two non-parallel points, once
        Set<List<Long>> normals = new HashSet<>();
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++) {
                long[] c = cross(points[i], points[j]);
                long g = gcd(gcd(c[0], c[1]), c[2]);
                if (g == 0)
                    continue;
                long lead = c[0] != 0 ? c[0] : c[1] != 0 ? c[1] : c[2];
                if (lead < 0)
                    g = -g;
                List<Long> key = new ArrayList<>();
                for (long x : c)
                    key.add(x / g);
                normals.add(key);
            }

        int best = 1; // a single airplane is always visible
        for (List<Long> key : normals) {
            long[] normal = {key.get(0), key.get(1), key.get(2)};
            int above = 0, below = 0;
            List<long[]> circle = new ArrayList<>();
            for (long[] p : points) {
                long s = dot(normal, p);
                if (s > 0)
                    above++;
                else if (s < 0)
                    below++;
                else
                    circle.add(p);
            }
            // a slight tilt shows the points of the circle in its best open half:
            // its edge passes through one of them, which a tilt adds as well
            int half = 0;
            for (long[] z : circle) {
                long[] edge = cross(normal, z);
                int ahead = 0, behind = 0;
                for (long[] p : circle) {
                    long s = dot(edge, p);
                    if (s > 0)
                        ahead++;
                    else if (s < 0)
                        behind++;
                }
                half = Math.max(half, Math.max(ahead, behind) + 1);
            }
            best = Math.max(best, Math.max(above, below) + half);
        }
        System.out.println(best);
    }
}
