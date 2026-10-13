import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    static long[] xs, ys;

    static long cross(int o, int a, int b) {
        return (xs[a] - xs[o]) * (ys[b] - ys[o]) - (ys[a] - ys[o]) * (xs[b] - xs[o]);
    }

    // marks the points of one monotone chain, keeping points that lie on its edges
    static void chain(int size, boolean reversed, boolean[] border) {
        int[] stack = new int[size];
        int top = 0;
        for (int k = 0; k < size; k++) {
            int i = reversed ? size - 1 - k : k;
            while (top > 1 && cross(stack[top - 2], stack[top - 1], i) < 0)
                top--;
            stack[top++] = i;
        }
        for (int k = 0; k < top; k++)
            border[stack[k]] = true;
    }

    static boolean flat(int size) {
        for (int i = 0; i < size; i++)
            if (cross(0, size - 1, i) != 0)
                return false;
        return true;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        long[][] points = new long[n][];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            long x = (long)in.nval;
            in.nextToken();
            points[i] = new long[] {x, (long)in.nval};
        }
        Arrays.sort(points,
                    (p, q) -> p[0] != q[0] ? Long.compare(p[0], q[0]) : Long.compare(p[1], q[1]));
        xs = new long[n];
        ys = new long[n];
        for (int i = 0; i < n; i++) {
            xs[i] = points[i][0];
            ys[i] = points[i][1];
        }
        int size = n, layers = 0;
        // peel hulls with their whole border while the rest still has area
        while (size > 2 && !flat(size)) {
            layers++;
            boolean[] border = new boolean[size];
            chain(size, false, border);
            chain(size, true, border);
            int kept = 0;
            for (int i = 0; i < size; i++)
                if (!border[i]) {
                    xs[kept] = xs[i];
                    ys[kept] = ys[i];
                    kept++;
                }
            size = kept;
        }
        System.out.println(layers);
    }
}
