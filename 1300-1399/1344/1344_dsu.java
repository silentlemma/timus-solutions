import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final int CEILING = 0, TURNIP = -1, FREE = -2;
    static final int ONE = 0, MASS = 1; // the turnip's weight of 1 and the unknown mass
    static final int FIELDS = 4;
    static int[][] blocks;
    static int[] parent, shift;
    static boolean[] zero; // the whole group must have no tension

    static int rope(int i) {
        return 2 * i + 2; // tension in the rope over block i
    }

    static int axle(int i) {
        return rope(i) + 1; // tension in the rope at the axle of block i
    }

    // every tension is a power of two times the tension at the root of its
    // group: value(x) = 2^shift[x] * value(root)
    static int find(int x) {
        if (parent[x] == x)
            return x;
        int root = find(parent[x]);
        shift[x] += shift[parent[x]];
        parent[x] = root;
        return root;
    }

    // value(x) = 2^k * value(y)
    static void tie(int x, int y, int k) {
        int rx = find(x), ry = find(y);
        if (rx == ry) {
            if (shift[x] != k + shift[y])
                zero[rx] = true;
            return;
        }
        parent[rx] = ry;
        shift[rx] = k + shift[y] - shift[x];
        zero[ry] = zero[ry] || zero[rx];
    }

    // the two rope ends and the axle as {node, target, down}; a first-type
    // block hangs its rope ends down
    static int[][] ports(int i) {
        int down = blocks[i][0] == 1 ? 1 : 0;
        return new int[][] {{rope(i), blocks[i][1], down},
                            {rope(i), blocks[i][2], down},
                            {axle(i), blocks[i][FIELDS - 1], 1 - down}};
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        blocks = new int[n][FIELDS];
        for (int i = 0; i < n; i++) {
            for (int f = 0; f < FIELDS; f++)
                blocks[i][f] = in.nextInt();
        }
        parent = new int[2 * n + 2];
        shift = new int[2 * n + 2];
        zero = new boolean[2 * n + 2];
        for (int v = 0; v < parent.length; v++)
            parent[v] = v;
        for (int i = 0; i < n; i++) {
            tie(axle(i), rope(i), 1); // the axle holds both ends of the rope
            for (int[] p : ports(i)) {
                if (p[1] == TURNIP) {
                    tie(p[0], ONE, 0);
                } else if (p[1] == FREE) {
                    tie(p[0], MASS, 0);
                } else if (p[1] != CEILING) {
                    // the other end leaves block target the opposite way
                    for (int[] q : ports(p[1] - 1)) {
                        if (q[1] == i + 1 && q[2] != p[2]) {
                            tie(p[0], q[0], 0);
                            break;
                        }
                    }
                }
            }
        }
        int one = find(ONE), mass = find(MASS);
        if (zero[one])
            System.out.println("No solution");
        else if (one == mass)
            System.out.println(
                String.format(Locale.US, "%.4f", Math.scalb(1.0, shift[MASS] - shift[ONE])));
        else if (zero[mass])
            System.out.println(String.format(Locale.US, "%.4f", 0.0));
        else
            System.out.println("Any");
    }
}
