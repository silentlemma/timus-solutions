import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int w = (int)in.nval;
        in.nextToken();
        int h = (int)in.nval;
        int[] x = new int[n], y = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            x[i] = (int)in.nval;
            in.nextToken();
            y[i] = (int)in.nval;
        }
        // a largest square slides left and down until its sides meet a tree or
        // the park border, so its corner has x = 0 or a tree x and y = 0 or a tree y
        int[] xs = Arrays.copyOf(x, n + 1), ys = Arrays.copyOf(y, n + 1);
        int bestP = 0, bestQ = 0, bestL = 0;
        for (int p : xs) {
            for (int q : ys) {
                int side = Math.min(w - p, h - q);
                // a tree up and to the right of the corner is inside unless the
                // side stops at its larger distance
                for (int i = 0; i < n; i++)
                    if (x[i] > p && y[i] > q)
                        side = Math.min(side, Math.max(x[i] - p, y[i] - q));
                if (side > bestL) {
                    bestP = p;
                    bestQ = q;
                    bestL = side;
                }
            }
        }
        System.out.println(bestP + " " + bestQ + " " + bestL);
    }
}
