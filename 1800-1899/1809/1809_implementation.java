import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final int SIDE = 20, COUNT = 4;
    static final int[][] STEPS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    // whether potatoes a and b share a line with nobody between them
    static boolean sees(int[] x, int[] y, int a, int b) {
        if (x[a] != x[b] && y[a] != y[b]) return false;
        for (int k = 0; k < COUNT; k++) {
            if (k == a || k == b) continue;
            if (Math.min(x[a], x[b]) <= x[k] && x[k] <= Math.max(x[a], x[b])
                && Math.min(y[a], y[b]) <= y[k] && y[k] <= Math.max(y[a], y[b])) {
                return false;
            }
        }
        return true;
    }

    static boolean good(int[] x, int[] y) {
        for (int a = 0; a < COUNT; a++) {
            if (x[a] < 1 || x[a] > SIDE || y[a] < 1 || y[a] > SIDE) return false;
            for (int b = 0; b < a; b++) {
                if (x[a] == x[b] && y[a] == y[b]) return false;
            }
        }
        for (int a = 0; a < COUNT; a++) {
            int seen = 0;
            for (int b = 0; b < COUNT; b++) {
                if (b != a && sees(x, y, a, b)) seen++;
            }
            if (seen != 1) return false;
        }
        return true;
    }

    static void print(int[] x, int[] y) {
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < COUNT; i++) out.append(x[i]).append(' ').append(y[i]).append('\n');
        System.out.print(out);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] sx = new int[COUNT], sy = new int[COUNT];
        for (int i = 0; i < COUNT; i++) {
            sx[i] = in.nextInt();
            sy[i] = in.nextInt();
        }
        if (good(sx, sy)) {
            print(sx, sy);
            return;
        }
        for (int k = 0; k < COUNT; k++) {
            for (int a = 1; a <= SIDE; a++) {
                for (int b = 1; b <= SIDE; b++) {
                    int[] x = sx.clone(), y = sy.clone();
                    x[k] = a;
                    y[k] = b;
                    if (good(x, y)) {
                        print(x, y);
                        return;
                    }
                }
            }
        }
        // two moves always do: next to the two kept potatoes, or as a pair of
        // their own in rows and columns nobody else uses
        for (int k = 0; k < COUNT; k++) {
            for (int l = k + 1; l < COUNT; l++) {
                List<int[]> kept = new ArrayList<>(), near = new ArrayList<>();
                for (int i = 0; i < COUNT; i++) {
                    if (i != k && i != l) kept.add(new int[] {sx[i], sy[i]});
                }
                for (int[] c : kept) {
                    for (int[] d : STEPS) near.add(new int[] {c[0] + d[0], c[1] + d[1]});
                }
                List<int[][]> options = new ArrayList<>();
                for (int[] a : near) {
                    for (int[] b : near) options.add(new int[][] {a, b});
                }
                int fx = 1, fy = 1;
                while (fx == kept.get(0)[0] || fx == kept.get(1)[0]) fx++;
                while (fy == kept.get(0)[1] || fy == kept.get(1)[1]
                    || fy + 1 == kept.get(0)[1] || fy + 1 == kept.get(1)[1]) {
                    fy++;
                }
                options.add(new int[][] {{fx, fy}, {fx, fy + 1}});
                for (int[][] o : options) {
                    int[] x = sx.clone(), y = sy.clone();
                    x[k] = o[0][0];
                    y[k] = o[0][1];
                    x[l] = o[1][0];
                    y[l] = o[1][1];
                    if (good(x, y)) {
                        print(x, y);
                        return;
                    }
                }
            }
        }
        print(sx, sy);
    }
}
