import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    static final int CORNERS = 3;
    static final double INNER = 0.5; // share of the way from the centre to a vertex
    static final double OUTER = 1 + INNER; // outer points go this far the opposite way

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer words = new StringTokenizer(text.toString());
        double[] x = new double[CORNERS];
        double[] y = new double[CORNERS];
        double gx = 0;
        double gy = 0;
        for (int i = 0; i < CORNERS; i++) {
            x[i] = Double.parseDouble(words.nextToken());
            y[i] = Double.parseDouble(words.nextToken());
            gx += x[i] / CORNERS;
            gy += y[i] / CORNERS;
        }
        StringBuilder out = new StringBuilder();
        for (double k : new double[] {INNER, -OUTER}) {
            for (int i = 0; i < CORNERS; i++) {
                double px = gx + (x[i] - gx) * k;
                double py = gy + (y[i] - gy) * k;
                out.append(String.format(Locale.US, "%.10f %.10f\n", px, py));
            }
        }
        System.out.print(out);
    }
}
