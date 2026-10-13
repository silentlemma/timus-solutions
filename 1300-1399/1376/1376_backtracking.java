import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.StringTokenizer;

// Faces: 0 the base, 1..4 the sides clockwise from the one facing +y. On the
// base, side k rests on the edge (v[k - 1], v[k % 4]); on a side, v[0] and
// v[1] are its base corners and v[2] its apex.
public class Main {
    static final int SIDES = 4;
    static final int FACES = 5;
    static final int MAX_ROLLS = 32;
    static final double EPS = 1e-12;
    static final double NONE = -1e100;
    static final int BEAM = 4000;  // states kept per depth by the first, greedy pass
    static final int TRIANGLE = 3; // corners of a side: its centroid is a third of the way up
    static final int START = FACES * FACES; // the key of the starting state

    // a state: xs, ys of the corners on the table, and the centre
    static class State {
        int face;
        int key; // previous face * FACES + face, or START
        double[] xs = new double[SIDES];
        double[] ys = new double[SIDES];
        double cx;
        double cy;
        int[] seq; // the faces so far, kept by the beam only
        double order;
    }

    static double s;
    static double t; // the base edge and the height of a side
    static double px;
    static double py; // the point
    static int n;
    static double[][] reach =
        new double[START + 1][MAX_ROLLS + 1]; // farthest move ending on the base
    static double best;
    static int bestRolls;
    static int[] bestSeq = new int[MAX_ROLLS + 1];
    static int[] seq = new int[MAX_ROLLS + 1];

    static boolean canRoll(int face, int next) {
        return face != next &&
            (face == 0 || next == 0 || (face - next + SIDES) % 2 == 1); // not opposite
    }

    static int prevOf(State st) { return st.key == START ? FACES : st.key / FACES; }

    static double cross(double ax, double ay, double bx, double by, double x, double y) {
        return (bx - ax) * (y - ay) - (by - ay) * (x - ax);
    }

    // the unit normal of a -> b pointing away from q
    static double[] away(double ax, double ay, double bx, double by, double qx, double qy) {
        double dx = bx - ax;
        double dy = by - ay;
        double len = Math.hypot(dx, dy);
        double nx = -dy / len;
        double ny = dx / len;
        if (cross(ax, ay, bx, by, ax + nx, ay + ny) * cross(ax, ay, bx, by, qx, qy) > 0) {
            nx = -nx;
            ny = -ny;
        }
        return new double[] {nx, ny};
    }

    // p reflected over the line a b, into slot i of ns
    static void reflect(State st, int p, int a, int b, State ns, int i) {
        double dx = st.xs[b] - st.xs[a];
        double dy = st.ys[b] - st.ys[a];
        double k = ((st.xs[p] - st.xs[a]) * dx + (st.ys[p] - st.ys[a]) * dy) / (dx * dx + dy * dy);
        ns.xs[i] = 2 * (st.xs[a] + k * dx) - st.xs[p];
        ns.ys[i] = 2 * (st.ys[a] + k * dy) - st.ys[p];
    }

    static void put(State ns, int i, State st, int j) {
        ns.xs[i] = st.xs[j];
        ns.ys[i] = st.ys[j];
    }

    static State roll(State st, int next) {
        State ns = new State();
        ns.face = next;
        ns.key = st.face * FACES + next;
        if (st.face == 0) { // onto side next: its apex beyond the edge
            int a = next - 1;
            int b = next % SIDES;
            double[] nrm = away(st.xs[a], st.ys[a], st.xs[b], st.ys[b], st.cx, st.cy);
            put(ns, 0, st, a);
            put(ns, 1, st, b);
            ns.xs[2] = (st.xs[a] + st.xs[b]) / 2 + nrm[0] * t;
            ns.ys[2] = (st.ys[a] + st.ys[b]) / 2 + nrm[1] * t;
        } else if (next == 0) { // onto the base: the square beyond the edge
            double[] nrm = away(st.xs[0], st.ys[0], st.xs[1], st.ys[1], st.xs[2], st.ys[2]);
            double[] cx = {st.xs[0], st.xs[1], st.xs[1] + nrm[0] * s, st.xs[0] + nrm[0] * s};
            double[] cy = {st.ys[0], st.ys[1], st.ys[1] + nrm[1] * s, st.ys[0] + nrm[1] * s};
            for (int i = 0; i < SIDES; i++) {
                ns.xs[(st.face - 1 + i) % SIDES] = cx[i];
                ns.ys[(st.face - 1 + i) % SIDES] = cy[i];
            }
        } else if (next == st.face % SIDES + 1) { // clockwise over the edge (v[1], apex)
            put(ns, 0, st, 1);
            reflect(st, 0, 1, 2, ns, 1);
            put(ns, 2, st, 2);
        } else { // counterclockwise over the edge (v[0], apex)
            reflect(st, 1, 0, 2, ns, 0);
            put(ns, 1, st, 0);
            put(ns, 2, st, 2);
        }
        int corners = next == 0 ? SIDES : SIDES - 1;
        for (int i = 0; i < corners; i++) {
            ns.cx += ns.xs[i] / corners;
            ns.cy += ns.ys[i] / corners;
        }
        return ns;
    }

    static double dist(State st) { return Math.hypot(st.cx - px, st.cy - py); }

    static double dist2(State st) {
        double dx = st.cx - px;
        double dy = st.cy - py;
        return dx * dx + dy * dy;
    }

    // can this state, with r rolls left, still beat the best?
    static boolean hopeful(State st, int r) {
        double u = reach[st.key][r];
        double lim = best + u + EPS;
        return u > NONE && dist2(st) <= lim * lim;
    }

    static void consider(int[] sequence, int rolls, double d) {
        if (d + EPS < best || (Math.abs(d - best) <= EPS && rolls < bestRolls)) {
            best = d;
            bestRolls = rolls;
            System.arraycopy(sequence, 0, bestSeq, 0, rolls + 1);
        }
    }

    static void search(State st, int depth) {
        if (st.face == 0) {
            consider(seq, depth, dist(st));
        }
        if (depth == n) {
            return;
        }
        State[] next = new State[SIDES];
        int count = 0;
        for (int f = 0; f < FACES; f++) {
            if (!canRoll(st.face, f) || f == prevOf(st)) {
                continue;
            }
            State ns = roll(st, f);
            if (hopeful(ns, n - depth - 1)) {
                ns.order = dist2(ns);
                next[count++] = ns;
            }
        }
        for (int i = 1; i < count; i++) { // nearest first
            for (int j = i; j > 0 && next[j].order < next[j - 1].order; j--) {
                State tmp = next[j];
                next[j] = next[j - 1];
                next[j - 1] = tmp;
            }
        }
        for (int i = 0; i < count; i++) {
            seq[depth + 1] = next[i].face;
            search(next[i], depth + 1);
        }
    }

    // a first answer: a beam search keeping the states that may get closest
    static void beam(State start) {
        start.seq = new int[MAX_ROLLS + 1];
        List<State> states = new ArrayList<>();
        states.add(start);
        for (int depth = 0; depth < n; depth++) {
            List<State> next = new ArrayList<>();
            for (State st : states) {
                for (int f = 0; f < FACES; f++) {
                    if (!canRoll(st.face, f) || f == prevOf(st)) {
                        continue;
                    }
                    State ns = roll(st, f);
                    double r = reach[ns.key][n - depth - 1];
                    if (r <= NONE) {
                        continue;
                    }
                    double d = dist(ns);
                    ns.seq = st.seq.clone();
                    ns.seq[depth + 1] = f;
                    if (f == 0) {
                        consider(ns.seq, depth + 1, d);
                    }
                    ns.order = Math.max(0, d - r);
                    next.add(ns);
                }
            }
            next.sort((a, b) -> Double.compare(a.order, b.order));
            states = next.size() > BEAM ? new ArrayList<>(next.subList(0, BEAM)) : next;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line; (line = reader.readLine()) != null;) {
            text.append(line).append(' ');
        }
        StringTokenizer in = new StringTokenizer(text.toString());
        s = Double.parseDouble(in.nextToken());
        double l = Double.parseDouble(in.nextToken());
        px = Double.parseDouble(in.nextToken());
        py = Double.parseDouble(in.nextToken());
        n = Integer.parseInt(in.nextToken());
        t = Math.sqrt(l * l - (s / 2) * (s / 2));
        // how far one roll moves the centre: base <-> side, and side <-> side
        double baseStep = s / 2 + t / TRIANGLE;
        double sideStep = 2 * s * t / (TRIANGLE * l);
        for (double[] row : reach) {
            java.util.Arrays.fill(row, NONE);
        }
        reach[START][0] = 0;
        for (int prev = 1; prev < FACES; prev++) {
            reach[prev * FACES][0] = 0;
        }
        for (int r = 1; r <= n; r++) {
            for (int face = 0; face < FACES; face++) {
                for (int prev = 0; prev <= FACES; prev++) { // prev == FACES: the start
                    if ((prev == FACES && face != 0) || (prev < FACES && !canRoll(prev, face))) {
                        continue;
                    }
                    int k = prev == FACES ? START : prev * FACES + face;
                    double u = reach[k][r - 1];
                    if (face == 0) {
                        u = Math.max(u, 0);
                    }
                    for (int f = 0; f < FACES; f++) {
                        if (canRoll(face, f) && f != prev &&
                            reach[face * FACES + f][r - 1] > NONE) {
                            double step = face == 0 || f == 0 ? baseStep : sideStep;
                            u = Math.max(u, step + reach[face * FACES + f][r - 1]);
                        }
                    }
                    reach[k][r] = u;
                }
            }
        }
        State start = new State();
        start.key = START;
        double h = s / 2;
        double[] xs = {-h, h, h, -h};
        double[] ys = {h, h, -h, -h};
        start.xs = xs;
        start.ys = ys;
        best = Math.hypot(px, py);
        beam(start);
        search(start, 0);
        StringBuilder out = new StringBuilder();
        out.append(String.format(Locale.US, "%.3f", best + EPS)).append('\n');
        out.append(bestRolls).append('\n');
        for (int i = 0; i <= bestRolls; i++) {
            out.append(i > 0 ? " " : "").append(bestSeq[i]);
        }
        System.out.println(out);
    }
}
