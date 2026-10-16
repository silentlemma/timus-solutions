import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    // a wrong set must move by 1e-5 to become right, so one turn misses by more
    // than 1e-5 / n, while right sets given to 1e-10 miss by far less
    static final double EPS = 1e-8;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        int n = Integer.parseInt(st.nextToken());
        double[] x = new double[n], y = new double[n];
        double cx = 0, cy = 0;
        for (int i = 0; i < n; i++) {
            x[i] = Double.parseDouble(st.nextToken());
            y[i] = Double.parseDouble(st.nextToken());
            cx += x[i];
            cy += y[i];
        }
        cx /= n;
        cy /= n;
        for (int i = 0; i < n; i++) {
            x[i] -= cx;
            y[i] -= cy;
        }
        // the vertices of a regular polygon in order turn into each other by a
        // rotation of 2 pi / n about the centre, one way or the other
        boolean ok = false;
        if (Math.hypot(x[0], y[0]) > EPS) {
            for (int way = -1; way <= 1; way += 2) {
                double c = Math.cos(way * 2 * Math.PI / n), s = Math.sin(way * 2 * Math.PI / n);
                boolean all = true;
                for (int i = 0; i < n; i++) {
                    int j = (i + 1) % n;
                    double rx = x[i] * c - y[i] * s, ry = x[i] * s + y[i] * c;
                    if (Math.hypot(x[j] - rx, y[j] - ry) > EPS) all = false;
                }
                if (all) ok = true;
            }
        }
        System.out.println(ok ? "YES" : "NO");
    }
}
