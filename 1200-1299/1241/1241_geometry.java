import java.io.*;

public class Main {
    // the four small triangles of a unit square, cut by both its diagonals
    static final int SOUTH = 0, EAST = 1, NORTH = 2, WEST = 3, PARTS = 4;
    // outward directions of a triangle's edges, counterclockwise from +x
    static final int RIGHT = 0;
    static final int UP_RIGHT = 1;
    static final int UP = 2;
    static final int UP_LEFT = 3;
    static final int LEFT = 4;
    static final int DOWN_LEFT = 5;
    static final int DOWN = 6;
    static final int DOWN_RIGHT = 7;
    static final int TRIANGLE = 3;
    static int[] parent, out;

    static int find(int a) {
        while (parent[a] != a)
            a = parent[a] = parent[parent[a]];
        return a;
    }

    // joins two small triangles, or records their outward directions when a
    // cut separates them
    static void side(int a, int da, int b, int db, boolean cut) {
        if (cut) {
            out[a] |= 1 << da;
            out[b] |= 1 << db;
        } else {
            parent[find(a)] = find(b);
        }
    }

    static int next(StreamTokenizer in) throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int m = next(in), n = next(in), k = next(in);
        // a cut runs from border to border, so it is a whole line of one of the
        // four kinds: x = c, y = c, x - y = c or x + y = c
        boolean[] vert = new boolean[m + 1], hor = new boolean[n + 1];
        boolean[] diff = new boolean[m + n + 1], sum = new boolean[m + n + 1];
        while (k-- > 0) {
            int x1 = next(in), y1 = next(in), x2 = next(in), y2 = next(in);
            if (x1 == x2)
                vert[x1] = true;
            else if (y1 == y2)
                hor[y1] = true;
            else if (x2 - x1 == y2 - y1)
                diff[x1 - y1 + n] = true;
            else
                sum[x1 + y1] = true;
        }
        parent = new int[m * n * PARTS];
        out = new int[m * n * PARTS];
        for (int a = 0; a < parent.length; a++)
            parent[a] = a;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                int s = (i * n + j) * PARTS, e = s + EAST, no = s + NORTH, w = s + WEST;
                side(s, UP_RIGHT, e, DOWN_LEFT, sum[i + j + 1]);
                side(s, UP_LEFT, w, DOWN_RIGHT, diff[i - j + n]);
                side(e, UP_LEFT, no, DOWN_RIGHT, diff[i - j + n]);
                side(no, DOWN_LEFT, w, UP_RIGHT, sum[i + j + 1]);
                if (j == 0)
                    out[s] |= 1 << DOWN;
                else
                    side(s, DOWN, s - PARTS + NORTH, UP, hor[j]);
                if (i == 0)
                    out[w] |= 1 << LEFT;
                else
                    side(w, LEFT, s - n * PARTS + EAST, RIGHT, vert[i]);
                if (j == n - 1)
                    out[no] |= 1 << UP;
                if (i == m - 1)
                    out[e] |= 1 << RIGHT;
            }
        // every piece is convex with sides in these 8 directions, one side per
        // direction, so a piece is a triangle when its edges face 3 directions
        int[] faces = new int[out.length];
        for (int a = 0; a < out.length; a++)
            faces[find(a)] |= out[a];
        int count = 0;
        for (int a = 0; a < faces.length; a++)
            if (find(a) == a && Integer.bitCount(faces[a]) == TRIANGLE)
                count++;
        System.out.println(count);
    }
}
