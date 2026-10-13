import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;
import java.util.Locale;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        StringBuilder out = new StringBuilder();
        while (in.nextToken() != StreamTokenizer.TT_EOF) {
            int m = 2 * (int)in.nval;
            double[] x = new double[m], y = new double[m], total = new double[m];
            for (int i = 0; i < m; i++) {
                in.nextToken();
                x[i] = in.nval;
                in.nextToken();
                y[i] = in.nval;
            }
            // total[i]: the sum of distances from point i to all the others, with
            // Math.sqrt, as Math.hypot is many times slower
            for (int i = 0; i < m; i++)
                for (int j = i + 1; j < m; j++) {
                    double dx = x[i] - x[j], dy = y[i] - y[j], d = Math.sqrt(dx * dx + dy * dy);
                    total[i] += d;
                    total[j] += d;
                }
            // a player's score is half the totals of the own points minus the
            // distances to the other colour, which both sides share: take the
            // largest total left, in turns
            Arrays.sort(total);
            double diff = 0;
            for (int i = 0; i < m; i++)
                diff += (m - 1 - i) % 2 == 0 ? total[i] : -total[i];
            out.append(String.format(Locale.US, "%.3f", Math.abs(diff / 2))).append('\n');
        }
        System.out.print(out);
    }
}
