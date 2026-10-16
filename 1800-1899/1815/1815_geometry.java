import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static final int CITIES = 3;
    static final double EPS = 1e-9; // a tie at the edge gives the same cost either way
    static double[] x = new double[CITIES], y = new double[CITIES], w = new double[CITIES];
    static DataInputStream in = new DataInputStream(System.in);

    static int readInt() throws IOException {
        int c = in.read();
        while (c != '-' && (c < '0' || c > '9')) c = in.read();
        boolean negative = c == '-';
        if (negative) c = in.read();
        int v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + (c - '0');
            c = in.read();
        }
        return negative ? -v : v;
    }

    static double cost(double mx, double my) {
        double total = 0;
        for (int i = 0; i < CITIES; i++) total += w[i] * Math.hypot(x[i] - mx, y[i] - my);
        return total;
    }

    static double solve() {
        // a city is the best place when the pull of the others, the weighted
        // unit vectors towards them, is no stronger than the weight standing
        // on that very spot
        for (int v = 0; v < CITIES; v++) {
            double here = 0, px = 0, py = 0;
            for (int i = 0; i < CITIES; i++) {
                double d = Math.hypot(x[i] - x[v], y[i] - y[v]);
                if (d == 0) {
                    here += w[i];
                } else {
                    px += w[i] * (x[i] - x[v]) / d;
                    py += w[i] * (y[i] - y[v]) / d;
                }
            }
            if (Math.hypot(px, py) <= here + EPS) return cost(x[v], y[v]);
        }
        // otherwise the best point is inside: by Ptolemy's inequality
        // w2 |MB| + w3 |MC| >= w1 |MQ| for the point Q beyond BC with
        // |BQ| : |CQ| : |BC| = w3 : w2 : w1, so the answer is w1 |AQ|
        double base = Math.hypot(x[2] - x[1], y[2] - y[1]);
        double fromB = base * w[2] / w[0], fromC = base * w[1] / w[0];
        double along = (fromB * fromB - fromC * fromC + base * base) / (2 * base);
        double height = Math.sqrt(Math.max(0, fromB * fromB - along * along));
        double ex = (x[2] - x[1]) / base, ey = (y[2] - y[1]) / base, nx = -ey, ny = ex;
        // Q lies on the other side of BC from A
        if ((x[0] - x[1]) * nx + (y[0] - y[1]) * ny > 0) {
            nx = -nx;
            ny = -ny;
        }
        double qx = x[1] + along * ex + height * nx, qy = y[1] + along * ey + height * ny;
        return w[0] * Math.hypot(x[0] - qx, y[0] - qy);
    }

    public static void main(String[] args) throws IOException {
        int t = readInt();
        StringBuilder out = new StringBuilder();
        for (; t > 0; t--) {
            for (int i = 0; i < CITIES; i++) {
                x[i] = readInt();
                y[i] = readInt();
            }
            for (int i = 0; i < CITIES; i++) w[i] = readInt();
            out.append(String.format("%.10f", solve())).append('\n');
        }
        System.out.print(out);
    }
}
