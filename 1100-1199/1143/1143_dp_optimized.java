import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    private static final class Input {
        private final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        private StringTokenizer fields = new StringTokenizer("");

        String next() throws IOException {
            while (!fields.hasMoreTokens()) {
                fields = new StringTokenizer(reader.readLine());
            }
            return fields.nextToken();
        }
    }

    private static double distance(double[] x, double[] y, int a, int b) {
        return Math.hypot(x[a] - x[b], y[a] - y[b]);
    }

    private static double shortest(double[] x, double[] y) {
        int n = x.length;
        double[] edge = new double[n];
        double[] left = new double[n];
        double[] right = new double[n];
        for (int i = 0; i < n; i++) {
            edge[i] = distance(x, y, i, i == 0 ? n - 1 : i - 1);
        }
        for (int span = 1; span < n; span++) {
            // Save the first arc before overwriting it for the wraparound.
            double firstLeft = left[0], firstRight = right[0];
            int end = span;
            for (int start = 0; start < n; start++) {
                int next = start + 1;
                double nextLeft = next == n ? firstLeft : left[next];
                double nextRight = next == n ? firstRight : right[next];
                double nextEdge = edge[next == n ? 0 : next];
                double chord = distance(x, y, start, end);
                double atRight = Math.min(left[start] + chord, right[start] + edge[end]);
                left[start] = Math.min(nextLeft + nextEdge, nextRight + chord);
                right[start] = atRight;
                end++;
                if (end == n) {
                    end = 0;
                }
            }
        }
        double answer = left[0];
        for (int i = 0; i < n; i++) {
            answer = Math.min(answer, Math.min(left[i], right[i]));
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int n = Integer.parseInt(input.next());
        double[] x = new double[n], y = new double[n];
        for (int i = 0; i < n; i++) {
            x[i] = Double.parseDouble(input.next());
            y[i] = Double.parseDouble(input.next());
        }
        System.out.printf(Locale.ROOT, "%.3f%n", shortest(x, y));
    }
}
