import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] x = new int[n], y = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            x[i] = (int)in.nval;
            in.nextToken();
            y[i] = (int)in.nval;
        }
        int best = 2;
        // Every line through two input points is tried; cross products are exact.
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int dx = x[j] - x[i], dy = y[j] - y[i], count = 0;
                for (int k = 0; k < n; k++)
                    if ((x[k] - x[i]) * dy == (y[k] - y[i]) * dx)
                        count++;
                best = Math.max(best, count);
                if (best == n) {
                    System.out.println(best);
                    return;
                }
            }
        }
        System.out.println(best);
    }
}
