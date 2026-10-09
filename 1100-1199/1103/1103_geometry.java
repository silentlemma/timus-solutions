import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static long cross(long[] o, long[] a, long[] b) {
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        long[][] pts = new long[n][];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            long x = (long)in.nval;
            in.nextToken();
            pts[i] = new long[] {x, (long)in.nval};
        }
        // A is the lowest point and B the next one on the hull, so every other
        // point lies on the left of AB and sees it under an angle below 180
        long[] a = pts[0];
        for (long[] p : pts) {
            if (p[1] < a[1] || (p[1] == a[1] && p[0] < a[0])) {
                a = p;
            }
        }
        List<long[]> rest = new ArrayList<>();
        for (long[] p : pts) {
            if (p != a) {
                rest.add(p);
            }
        }
        long[] b = rest.get(0);
        for (long[] p : rest) {
            if (cross(a, b, p) < 0) {
                b = p;
            }
        }
        List<long[]> others = new ArrayList<>();
        List<BigInteger[]> keys = new ArrayList<>();
        for (long[] p : rest) {
            if (p != b) {
                long dot = (a[0] - p[0]) * (b[0] - p[0]) + (a[1] - p[1]) * (b[1] - p[1]);
                others.add(p);
                long side = cross(p, a, b);
                keys.add(new BigInteger[] {BigInteger.valueOf(dot), BigInteger.valueOf(side)});
            }
        }
        // the angle APB grows as its cotangent dot / cross falls; the products
        // reach 10^33, so they are compared as big integers
        Integer[] order = new Integer[others.size()];
        for (int i = 0; i < order.length; i++) {
            order[i] = i;
        }
        Arrays.sort(order, (i, j) -> {
            BigInteger l = keys.get(i)[0].multiply(keys.get(j)[1]);
            BigInteger r = keys.get(j)[0].multiply(keys.get(i)[1]);
            return r.compareTo(l);
        });
        // points seeing AB under a larger angle than C lie inside the circle ABC
        long[] c = others.get(order[order.length / 2]);
        System.out.println(a[0] + " " + a[1] + "\n" + b[0] + " " + b[1] + "\n" + c[0] + " " + c[1]);
    }
}
