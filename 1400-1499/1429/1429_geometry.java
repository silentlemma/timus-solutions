import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

public class Main {
    static final double CELL = 1e-3; // distinct crossing points are at least this far apart
    static final double SAME = 1e-4; // two estimates of one point are much closer than this

    // the crossing points on each circle as angles around its centre: one
    // table of all points would not fit in the memory limit
    static double[][] angles;
    static int[] count;

    static void add(int c, double a) {
        if (count[c] == angles[c].length)
            angles[c] = Arrays.copyOf(angles[c], Math.max(2, 2 * count[c]));
        angles[c][count[c]++] = a;
    }

    static int[] parent;

    static int find(int a) {
        while (parent[a] != a)
            a = parent[a] = parent[parent[a]];
        return a;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // a cut made twice is still one cut
        Set<List<Long>> unique = new LinkedHashSet<>();
        for (int i = 0; i < n; i++) {
            in.nextToken();
            long x = (long)in.nval;
            in.nextToken();
            long y = (long)in.nval;
            in.nextToken();
            unique.add(Arrays.asList(x, y, (long)in.nval));
        }
        List<List<Long>> circles = new ArrayList<>(unique);
        int k = circles.size();
        parent = new int[k];
        for (int i = 0; i < k; i++)
            parent[i] = i;
        angles = new double[k][0];
        count = new int[k];
        for (int i = 0; i < k; i++) {
            long x1 = circles.get(i).get(0), y1 = circles.get(i).get(1), r1 = circles.get(i).get(2);
            for (int j = i + 1; j < k; j++) {
                long x2 = circles.get(j).get(0), y2 = circles.get(j).get(1),
                     r2 = circles.get(j).get(2);
                long dx = x2 - x1, dy = y2 - y1, d2 = dx * dx + dy * dy;
                if (d2 > (r1 + r2) * (r1 + r2) || d2 < (r1 - r2) * (r1 - r2))
                    continue; // apart, or one inside the other
                // the crossings are p1 + (m * (dx, dy) +- sqrt(K) * (-dy, dx)) / (2 d2), K exact
                long m = d2 + r1 * r1 - r2 * r2;
                double root = Math.sqrt((double)((2 * r1) * (2 * r1) * d2 - m * m));
                for (int sign = 1; sign >= -1; sign -= 2) {
                    double x = x1 + (m * dx - sign * root * dy) / (2.0 * d2);
                    double y = y1 + (m * dy + sign * root * dx) / (2.0 * d2);
                    add(i, Math.atan2(y - y1, x - x1));
                    add(j, Math.atan2(y - y2, x - x2));
                    if (root == 0)
                        break;
                }
                parent[find(i)] = find(j);
            }
        }
        // sorted by angle, the estimates of one point stand together: distinct
        // points differ by at least CELL / r in angle, estimates by far less. A
        // group of s estimates is a point on s + 1 circles: 1 / (s + 1) vertex
        long edges = 0;
        int components = 0;
        long[] shared = new long[k + 1]; // groups seen, by circles through the point
        for (int i = 0; i < k; i++) {
            double gap = SAME / circles.get(i).get(2);
            double[] a = angles[i];
            int e = count[i];
            Arrays.sort(a, 0, e);
            int[] sizes = new int[Math.max(1, e)];
            int groups = 0;
            for (int t = 0; t < e; t++)
                if (t > 0 && a[t] - a[t - 1] < gap)
                    sizes[groups - 1]++;
                else
                    sizes[groups++] = 1;
            if (groups > 1 && a[0] + 2 * Math.PI - a[e - 1] < gap)
                sizes[0] += sizes[--groups]; // the group around the angle pi
            if (groups == 0)
                sizes[groups++] = 0; // a circle with no crossings: one vertex, one edge
            edges += groups;
            for (int g = 0; g < groups; g++)
                shared[sizes[g] + 1]++;
            angles[i] = null;
            if (find(i) == i)
                components++;
        }
        long vertices = 0;
        for (int c = 1; c <= k; c++)
            vertices += shared[c] / c;
        // Euler's formula for a plane graph: faces = edges - vertices + components + 1
        System.out.println(edges - vertices + components + 1);
    }
}
