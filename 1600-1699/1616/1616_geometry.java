import java.util.*;

public class Main {
    static final double EPS = 1e-9;
    static final double HALF = 0.5; // a cell goes to an owner who held more than half of it
    static final int LETTERS = 26;
    static final int CORNERS = 4;
    static final double STRAIGHT = 180; // degrees in a half turn
    static final int TRIANGLE = 3; // the fewest corners of a polygon with area

    // the part of a convex polygon with coordinate axis >= bound (or <=)
    static List<double[]> clip(List<double[]> poly, int axis, double bound, boolean keepAbove) {
        List<double[]> out = new ArrayList<>();
        int count = poly.size();
        for (int i = 0; i < count; i++) {
            double[] a = poly.get(i), b = poly.get((i + 1) % count);
            boolean inA = keepAbove ? a[axis] >= bound - EPS : a[axis] <= bound + EPS;
            boolean inB = keepAbove ? b[axis] >= bound - EPS : b[axis] <= bound + EPS;
            if (inA != inB) {
                double t = (bound - a[axis]) / (b[axis] - a[axis]);
                out.add(new double[] {a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t});
            }
            if (inB)
                out.add(b);
        }
        return out;
    }

    static double area(List<double[]> poly) {
        double total = 0;
        for (int i = 0; i < poly.size(); i++) {
            double[] a = poly.get(i), b = poly.get((i + 1) % poly.size());
            total += a[0] * b[1] - b[0] * a[1];
        }
        return Math.abs(total) / 2;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        double alpha = Double.parseDouble(in.next());
        String[] grid = new String[2 * n];
        for (int i = 0; i < 2 * n; i++)
            grid[i] = in.next();
        int size = 2 * (2 * n); // the new map covers twice the old side
        // owned area of each new cell, per owner letter
        double[][] held = new double[size * size][LETTERS];
        double rad = alpha * Math.PI / STRAIGHT, cosA = Math.cos(rad), sinA = Math.sin(rad);
        for (int row = 0; row < 2 * n; row++) {
            int y = n - 1 - row;
            for (int col = 0; col < 2 * n; col++) {
                char owner = grid[row].charAt(col);
                if (owner == '.')
                    continue;
                int x = col - n;
                // the axes turn clockwise, so the cell turns counterclockwise
                int[] cx = {x, x + 1, x + 1, x}, cy = {y, y, y + 1, y + 1};
                List<double[]> square = new ArrayList<>();
                double xLo = Double.POSITIVE_INFINITY, xHi = Double.NEGATIVE_INFINITY;
                double yLo = Double.POSITIVE_INFINITY, yHi = Double.NEGATIVE_INFINITY;
                for (int k = 0; k < CORNERS; k++) {
                    double[] p = {cx[k] * cosA - cy[k] * sinA, cx[k] * sinA + cy[k] * cosA};
                    square.add(p);
                    xLo = Math.min(xLo, p[0]);
                    xHi = Math.max(xHi, p[0]);
                    yLo = Math.min(yLo, p[1]);
                    yHi = Math.max(yHi, p[1]);
                }
                int x0 = Math.max(-2 * n, (int)Math.floor(xLo + EPS));
                int x1 = Math.min(2 * n, (int)Math.ceil(xHi - EPS));
                int y0 = Math.max(-2 * n, (int)Math.floor(yLo + EPS));
                int y1 = Math.min(2 * n, (int)Math.ceil(yHi - EPS));
                int letter = owner - 'a';
                for (int gy = y0; gy < y1; gy++)
                    for (int gx = x0; gx < x1; gx++) {
                        List<double[]> part = clip(square, 0, gx, true);
                        part = clip(part, 0, gx + 1, false);
                        part = clip(part, 1, gy, true);
                        part = clip(part, 1, gy + 1, false);
                        if (part.size() >= TRIANGLE)
                            held[(2 * n - 1 - gy) * size + gx + 2 * n][letter] += area(part);
                    }
            }
        }
        StringBuilder out = new StringBuilder();
        for (int r = 0; r < size; r++) {
            for (int c = 0; c < size; c++) {
                char best = '.';
                for (int i = 0; i < LETTERS; i++)
                    if (held[r * size + c][i] > HALF + EPS) {
                        best = (char)('a' + i);
                        break;
                    }
                out.append(best);
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
