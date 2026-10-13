import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final double TURN = 2 * Math.PI;

    // signed area of the unit disk at the origin inside the triangle (origin, a, b)
    static double cut(double ax, double ay, double bx, double by) {
        double dx = bx - ax, dy = by - ay;
        double qa = dx * dx + dy * dy, qb = ax * dx + ay * dy, qc = ax * ax + ay * ay - 1;
        List<Double> marks = new ArrayList<>();
        marks.add(0.0);
        marks.add(1.0);
        double disc = qb * qb - qa * qc;
        if (disc > 0) {
            double root = Math.sqrt(disc);
            for (double t : new double[] {(-qb - root) / qa, (-qb + root) / qa})
                if (t > 0 && t < 1)
                    marks.add(t);
        }
        Collections.sort(marks);
        double area = 0;
        for (int i = 0; i + 1 < marks.size(); i++) {
            double s = marks.get(i), t = marks.get(i + 1);
            double px = ax + dx * s, py = ay + dy * s, qx = ax + dx * t, qy = ay + dy * t;
            double mx = (px + qx) / 2, my = (py + qy) / 2;
            double cross = px * qy - py * qx;
            // a piece inside the disk adds its triangle, one outside adds its sector
            area += mx * mx + my * my < 1 ? cross / 2 : Math.atan2(cross, px * qx + py * qy) / 2;
        }
        return area;
    }

    // water that one umbrella moves off or onto the field
    static double change(double x, double y, double width, double length) {
        double[] cx = {-x, length - x, length - x, -x};
        double[] cy = {-y, -y, width - y, width - y};
        double covered = 0;
        for (int i = 0; i < cx.length; i++) {
            int j = (i + cx.length - 1) % cx.length;
            covered += cut(cx[j], cy[j], cx[i], cy[i]);
        }
        // the rim splits into arcs at the field's border lines
        List<Double> angles = new ArrayList<>();
        angles.add(0.0);
        angles.add(TURN);
        for (double d : new double[] {-x, length - x})
            if (Math.abs(d) <= 1) {
                angles.add(Math.acos(d));
                angles.add(TURN - Math.acos(d));
            }
        for (double d : new double[] {-y, width - y})
            if (Math.abs(d) <= 1) {
                angles.add((Math.asin(d) + TURN) % TURN);
                angles.add(Math.PI - Math.asin(d));
            }
        Collections.sort(angles);
        double inside = 0;
        for (int i = 0; i + 1 < angles.size(); i++) {
            double m = (angles.get(i) + angles.get(i + 1)) / 2;
            double px = x + Math.cos(m), py = y + Math.sin(m);
            if (px >= 0 && px <= length && py >= 0 && py <= width)
                inside += angles.get(i + 1) - angles.get(i);
        }
        // rain caught over the whole disk leaves from the rim evenly by angle
        return Math.PI * inside / TURN - covered;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line; (line = in.readLine()) != null;)
            text.append(line).append(' ');
        StringTokenizer st = new StringTokenizer(text.toString());
        int width = Integer.parseInt(st.nextToken()), length = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        double total = (double)width * length;
        for (int i = 0; i < n; i++) {
            double x = Double.parseDouble(st.nextToken()), y = Double.parseDouble(st.nextToken());
            total += change(x, y, width, length);
        }
        System.out.println(String.format(java.util.Locale.US, "%.3f", total));
    }
}
