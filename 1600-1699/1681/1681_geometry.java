import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Main {
    static double cross(double[] a, double[] b, double[] c) {
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]);
    }

    // the part of a convex polygon on the given side (sign of the cross
    // product) of the line through a and b
    static List<double[]> clip(List<double[]> poly, double[] a, double[] b, double sign) {
        List<double[]> out = new ArrayList<>();
        int count = poly.size();
        for (int i = 0; i < count; i++) {
            double[] p = poly.get(i);
            double[] q = poly.get((i + 1) % count);
            double sp = cross(a, b, p) * sign;
            double sq = cross(a, b, q) * sign;
            if (sp >= 0) {
                out.add(p);
            }
            if ((sp > 0 && sq < 0) || (sp < 0 && sq > 0)) {
                double t = sp / (sp - sq);
                out.add(new double[] {p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t});
            }
        }
        return out;
    }

    static double area(List<double[]> poly) {
        double total = 0;
        int count = poly.size();
        for (int i = 0; i < count; i++) {
            double[] a = poly.get((i + count - 1) % count);
            double[] b = poly.get(i);
            total += a[0] * b[1] - b[0] * a[1];
        }
        return total / 2;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int) in.nval;
        in.nextToken();
        int k = (int) in.nval;
        List<double[]> pts = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            in.nextToken();
            double x = in.nval;
            in.nextToken();
            pts.add(new double[] {x, in.nval});
        }
        k = Math.min(k, n - k);
        if (k == 1) {
            // every rope lies along the fence: the rabbit cannot get in at all
            System.out.println(String.format(Locale.US, "%.9f", 1.0));
            return;
        }
        double whole = area(pts);
        double reachable = 0;
        for (int i = 0; i < n; i++) {
            // the face next to side i is on the side's side of every rope; only
            // the ropes from vertices i + 1 - k, ..., i pass over that side
            double[] p = pts.get(i);
            double[] q = pts.get((i + 1) % n);
            double[] mid = {(p[0] + q[0]) / 2, (p[1] + q[1]) / 2};
            List<Integer> ropes = new ArrayList<>();
            ropes.add(i + 1 - k);
            ropes.add(i);
            for (int j = i + 2 - k; j < i; j++) {
                ropes.add(j);
            }
            List<double[]> face = pts;
            for (int j : ropes) {
                double[] a = pts.get((j % n + n) % n);
                double[] b = pts.get((j + k) % n);
                face = clip(face, a, b, cross(a, b, mid) > 0 ? 1 : -1);
                if (face.isEmpty()) {
                    break;
                }
            }
            reachable += area(face);
        }
        System.out.println(String.format(Locale.US, "%.9f", (whole - reachable) / whole));
    }
}
