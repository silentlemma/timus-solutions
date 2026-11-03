import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int STRIPS = 4096;
    static final double PERCENT = 100, MIDDLE = 0.5;

    public static void main(String[] args) throws Exception {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        double[] cx = new double[n], cy = new double[n], rr = new double[n];
        double[] low = new double[n], high = new double[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            cx[i] = in.nval;
            in.nextToken();
            cy[i] = in.nval;
            in.nextToken();
            rr[i] = in.nval * in.nval;
        }
        double covered = 0;
        // Midpoint error<=2*sum(r)/STRIPS, below0.005 for at most10 discs.
        // Reusable primitive intervals avoid per-strip objects and comparators.
        for (int k = 0; k < STRIPS; k++) {
            double x = (k + MIDDLE) / STRIPS;
            int count = 0;
            for (int i = 0; i < n; i++) {
                double dx = x - cx[i], square = rr[i] - dx * dx;
                if (square <= 0)
                    continue;
                double half = Math.sqrt(square);
                double a = Math.max(0, cy[i] - half), b = Math.min(1, cy[i] + half);
                if (a >= b)
                    continue;
                int j = count++;
                while (j > 0 && low[j - 1] > a) {
                    low[j] = low[j - 1];
                    high[j] = high[j - 1];
                    j--;
                }
                low[j] = a;
                high[j] = b;
            }
            double end = 0;
            for (int i = 0; i < count; i++)
                if (high[i] > end) {
                    covered += high[i] - Math.max(low[i], end);
                    end = high[i];
                }
        }
        System.out.println(covered / STRIPS * PERCENT);
    }
}
