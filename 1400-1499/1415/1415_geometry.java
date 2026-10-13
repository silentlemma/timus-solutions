import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final String[] COLORS = {"VIOLET", "INDIGO", "BLUE", "GREEN", "YELLOW", "ORANGE", "RED"};
    static final int RED = 6;
    static final double PER_DECADE = 5; // a level per 2 dB: five levels per tenfold distance
    static final double TEN = 10;
    static final double EPS = 1e-9; // events closer than this in segment time happen together
    static final double TIE = 1e-9; // powers closer than this relative gap are equal
    static final int BUFFER = 1 << 16;

    static int n;
    static double[] xs, ys, rs;
    static String[] names;
    static double[][] bounds; // squared radii where the level steps up
    static double sx, sy, dx, dy, len2;

    static int level(int i, double px, double py) {
        double d2 = (px - xs[i]) * (px - xs[i]) + (py - ys[i]) * (py - ys[i]);
        int l = 0;
        for (double b : bounds[i])
            if (d2 > b)
                l++;
        return l;
    }

    // the strongest station at (px, py); equal powers go to the smaller name
    static int best(List<Integer> cands, double px, double py) {
        int top = cands.get(0);
        for (int i : cands) {
            // power is r / d: compare r_i * d_top with r_top * d_i
            double a = rs[i] * Math.hypot(px - xs[top], py - ys[top]);
            double b = rs[top] * Math.hypot(px - xs[i], py - ys[i]);
            if (a > b * (1 + TIE) ||
                (Math.abs(a - b) <= TIE * Math.max(a, b) && names[i].compareTo(names[top]) < 0))
                top = i;
        }
        return top;
    }

    // times in (0, 1) where the distance to station i squared is rad2
    static void roots(int i, double rad2, List<Double> out) {
        double px = sx - xs[i], py = sy - ys[i];
        double b = dx * px + dy * py, c = px * px + py * py - rad2;
        double disc = b * b - len2 * c;
        if (disc <= 0)
            return;
        double q = -(b + Math.copySign(Math.sqrt(disc), b));
        for (double t : new double[] {q / len2, c / q})
            if (t > 0 && t < 1)
                out.add(t);
    }

    // the level of station i just after time t, before its own next change
    static int levelAfter(int i, double t) {
        List<Double> ts = new ArrayList<>();
        for (double b : bounds[i])
            roots(i, b, ts);
        double next = 1;
        for (double u : ts)
            if (u > t + EPS)
                next = Math.min(next, u);
        double u = (t + next) / 2;
        return level(i, sx + dx * u, sy + dy * u);
    }

    // events as (time, station) pairs; -1 marks the current station's own circles
    static List<double[]> timeline(List<double[]> reds, int cur, double after) {
        List<double[]> events = new ArrayList<>();
        List<Double> ts = new ArrayList<>();
        for (double b : bounds[cur])
            roots(cur, b, ts);
        for (double t : ts)
            if (t > after)
                events.add(new double[] {t, -1});
        for (double[] e : reds)
            if (e[0] > after)
                events.add(e);
        events.sort(
            (p, q) -> p[0] != q[0] ? Double.compare(p[0], q[0]) : Double.compare(p[1], q[1]));
        return events;
    }

    public static void main(String[] args) throws IOException {
        InputStream in = System.in;
        ByteArrayOutputStream raw = new ByteArrayOutputStream();
        byte[] buf = new byte[BUFFER];
        for (int got; (got = in.read(buf)) > 0;)
            raw.write(buf, 0, got);
        // ISO-8859-1 keeps every byte of a name and compares bytes as unsigned
        StringTokenizer st = new StringTokenizer(raw.toString("ISO-8859-1"));
        n = Integer.parseInt(st.nextToken());
        xs = new double[n];
        ys = new double[n];
        rs = new double[n];
        names = new String[n];
        bounds = new double[n][RED];
        for (int i = 0; i < n; i++) {
            xs[i] = Double.parseDouble(st.nextToken());
            ys[i] = Double.parseDouble(st.nextToken());
            rs[i] = Double.parseDouble(st.nextToken());
            names[i] = st.nextToken();
            for (int k = 0; k < RED; k++) {
                double r = rs[i] * Math.pow(TEN, k / PER_DECADE);
                bounds[i][k] = r * r;
            }
        }
        int m = Integer.parseInt(st.nextToken());
        // the ends of each segment
        double[] ax = new double[m], ay = new double[m], bx = new double[m], by = new double[m];
        for (int j = 0; j < m; j++) {
            ax[j] = Double.parseDouble(st.nextToken());
            ay[j] = Double.parseDouble(st.nextToken());
            bx[j] = Double.parseDouble(st.nextToken());
            by[j] = Double.parseDouble(st.nextToken());
        }
        StringBuilder out = new StringBuilder();
        List<Integer> all = new ArrayList<>();
        for (int i = 0; i < n; i++)
            all.add(i);
        int cur = best(all, ax[0], ay[0]);
        int lev = level(cur, ax[0], ay[0]);
        out.append("Power on. CELL_ID:" + names[cur] + ", SIGNAL_LEVEL:" + COLORS[lev] + "\n");

        for (int j = 0; j < m; j++) {
            sx = ax[j];
            sy = ay[j];
            dx = bx[j] - ax[j];
            dy = by[j] - ay[j];
            len2 = dx * dx + dy * dy;
            if (len2 == 0)
                continue;
            // red and not red switch only on the outer circles
            List<double[]> reds = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                List<Double> ts = new ArrayList<>();
                roots(i, bounds[i][RED - 1], ts);
                for (double t : ts)
                    reds.add(new double[] {t, i});
            }
            List<double[]> events = timeline(reds, cur, -1);
            int k = 0;
            while (k < events.size()) {
                double t0 = events.get(k)[0];
                List<Integer> group = new ArrayList<>();
                while (k < events.size() && events.get(k)[0] - t0 <= EPS)
                    group.add((int)events.get(k++)[1]);
                // the state right after the group holds until the next event
                double tend = events.get(k - 1)[0];
                double t1 = k < events.size() ? events.get(k)[0] : 1;
                double mx = sx + dx * (t0 + t1) / 2, my = sy + dy * (t0 + t1) / 2;
                double px = sx + dx * t0, py = sy + dy * t0;
                boolean searching = false;
                List<Integer> cands = new ArrayList<>();
                if (lev != RED) {
                    int now = level(cur, mx, my);
                    if (now != lev) {
                        lev = now;
                        out.append("Signal changed. SIGNAL_LEVEL:" + COLORS[lev] + "\n");
                        if (lev == RED) {
                            searching = true;
                            for (int i = 0; i < n; i++)
                                if (level(i, mx, my) < RED)
                                    cands.add(i);
                        }
                    }
                } else {
                    searching = true;
                    for (int i : group)
                        if (i >= 0 && level(i, mx, my) < RED)
                            cands.add(i);
                }
                if (!searching || cands.isEmpty())
                    continue;
                int pick = best(cands, px, py);
                lev = levelAfter(pick, tend);
                if (pick == cur) {
                    out.append("Signal changed. SIGNAL_LEVEL:" + COLORS[lev] + "\n");
                } else {
                    cur = pick;
                    out.append("Cell changed. CELL_ID:" + names[cur] +
                               ", SIGNAL_LEVEL:" + COLORS[lev] + "\n");
                    events = timeline(reds, cur, tend + EPS);
                    k = 0;
                }
            }
        }
        System.out.write(out.toString().getBytes(StandardCharsets.ISO_8859_1));
        System.out.flush();
    }
}
