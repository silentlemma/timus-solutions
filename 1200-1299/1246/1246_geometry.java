import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        long[] x = new long[n], y = new long[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            x[i] = (long)in.nval;
            in.nextToken();
            y[i] = (long)in.nval;
        }
        // twice the signed area by the shoelace formula: positive when the
        // runner goes counterclockwise, and the rope winds the same way
        long twice = 0;
        for (int i = 0; i < n; i++) {
            int j = (i + 1) % n;
            twice += x[i] * y[j] - x[j] * y[i];
        }
        System.out.println(twice > 0 ? "ccw" : "cw");
    }
}
