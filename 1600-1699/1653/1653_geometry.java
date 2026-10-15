import java.util.*;

public class Main {
    static final double PHI = (1 + Math.sqrt(5)) / 2;
    static final double TINY = 1e-14;
    static final double SAME = 1e-7; // equal edge lengths up to rounding
    static final int DIM = 3;

    static double dot(double[] a, double[] b) {
        return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
    }

    static double[] unit(double[] v) {
        double n = Math.sqrt(dot(v, v));
        return new double[] {v[0] / n, v[1] / n, v[2] / n};
    }

    static double[] cross(double[] a, double[] b) {
        return new double[] {
            a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]
        };
    }

    static double dist(double[] a, double[] b) {
        double[] d = {a[0] - b[0], a[1] - b[1], a[2] - b[2]};
        return Math.sqrt(dot(d, d));
    }

    static double[] apply(double[][] m, double[] v) {
        return new double[] {dot(m[0], v), dot(m[1], v), dot(m[2], v)};
    }

    static double[][] compose(double[][] a, double[][] b) {
        double[][] r = new double[DIM][DIM];
        for (int i = 0; i < DIM; i++)
            for (int j = 0; j < DIM; j++)
                for (int k = 0; k < DIM; k++)
                    r[i][j] += a[i][k] * b[k][j];
        return r;
    }

    // rotation by angle around axis, right-handed
    static double[][] rotation(double[] axis, double angle) {
        double[] u = unit(axis);
        double x = u[0], y = u[1], z = u[2], c = Math.cos(angle), s = Math.sin(angle), t = 1 - c;
        return new double[][] {
            {t * x * x + c, t * x * y - s * z, t * x * z + s * y},
            {t * x * y + s * z, t * y * y + c, t * y * z - s * x},
            {t * x * z - s * y, t * y * z + s * x, t * z * z + c}
        };
    }

    static List<double[]> solid(String name) {
        double[] signs = {-1, 1};
        List<double[]> pts = new ArrayList<>();
        if (name.equals("tetrahedron")) {
            pts.addAll(Arrays.asList(new double[][] {
                {1, 1, 1}, {1, -1, -1}, {-1, 1, -1}, {-1, -1, 1}}));
        } else if (name.equals("octahedron")) {
            pts.addAll(Arrays.asList(new double[][] {
                {1, 0, 0}, {-1, 0, 0}, {0, 1, 0}, {0, -1, 0}, {0, 0, 1}, {0, 0, -1}}));
        } else if (name.equals("icosahedron")) {
            for (double a : signs)
                for (double b : signs) {
                    pts.add(new double[] {0, a, b * PHI});
                    pts.add(new double[] {a, b * PHI, 0});
                    pts.add(new double[] {b * PHI, 0, a});
                }
        } else {
            for (double x : signs)
                for (double y : signs)
                    for (double z : signs)
                        pts.add(new double[] {x, y, z});
            if (name.equals("dodecahedron"))
                for (double a : signs)
                    for (double b : signs) {
                        pts.add(new double[] {0, a / PHI, b * PHI});
                        pts.add(new double[] {a / PHI, b * PHI, 0});
                        pts.add(new double[] {b * PHI, 0, a / PHI});
                    }
        }
        pts.replaceAll(Main::unit);
        return pts;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        List<double[]> guns = solid(in.next());
        int n = in.nextInt();
        double edge = Double.MAX_VALUE;
        for (double[] a : guns)
            for (double[] b : guns)
                if (dist(a, b) > SAME)
                    edge = Math.min(edge, dist(a, b));
        // turn the solid so that one gun points along z and a neighbour lies
        // in the half-plane x >= 0 of Oxz; any choice is the same up to symmetry
        double[] z = guns.get(0), near = z;
        for (double[] g : guns)
            if (Math.abs(dist(g, z) - edge) < SAME) {
                near = g;
                break;
            }
        double along = dot(near, z);
        double[] x = unit(new double[] {
            near[0] - along * z[0], near[1] - along * z[1], near[2] - along * z[2]});
        double[] y = cross(z, x);
        for (int i = 0; i < guns.size(); i++) {
            double[] g = guns.get(i);
            guns.set(i, unit(new double[] {dot(g, x), dot(g, y), dot(g, z)}));
        }
        double[][] turn = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
        double total = 0;
        for (int i = 0; i < n; i++) {
            double[] v = {in.nextDouble(), in.nextDouble(), in.nextDouble()};
            double[] target = unit(new double[] {-v[0], -v[1], -v[2]}); // the ship comes from there
            double[] gun = apply(turn, guns.get(0));
            for (double[] g : guns) {
                double[] turned = apply(turn, g);
                if (dot(turned, target) > dot(gun, target))
                    gun = turned;
            }
            double angle = Math.acos(Math.max(-1, Math.min(1, dot(gun, target))));
            total += angle;
            double[] axis = cross(gun, target);
            if (angle > TINY && Math.sqrt(dot(axis, axis)) > TINY)
                // the shortest turn: around the axis normal to both directions
                turn = compose(rotation(axis, angle), turn);
        }
        System.out.println(String.format(Locale.US, "%.5f", total));
    }
}
