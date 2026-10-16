import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final int FACES = 6, TURNS = 4, WORD = 64;
    static int n;
    static int[][][] parts = new int[FACES][][];
    // options.get(part).get(face): the different masks of a part on a face
    static List<List<List<long[]>>> options = new ArrayList<>();
    static int[] faceOf = new int[FACES]; // -1 while a part is unused
    static long[][] chosen = new long[FACES][];

    // the cell at depth k under row r, column c of a face; every face is the
    // bottom one turned by a rotation of the cube, so no part is mirrored
    static int cellIndex(int face, int r, int c, int k) {
        int last = n - 1;
        int[][] cells = {{k, r, c}, {last - k, last - r, c}, {r, last - k, c},
            {r, k, last - c}, {r, c, k}, {r, last - c, last - k}};
        int[] at = cells[face];
        return (at[0] * n + at[1]) * n + at[2];
    }

    static long[] placement(int p, int face, int turns) {
        long[] mask = new long[(n * n * n + WORD - 1) / WORD];
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                int rr = r, cc = c;
                for (int t = 0; t < turns; t++) {
                    int keep = rr;
                    rr = cc;
                    cc = n - 1 - keep;
                }
                for (int k = 0; k < parts[p][r][c]; k++) {
                    int id = cellIndex(face, rr, cc, k);
                    mask[id / WORD] |= 1L << (id % WORD);
                }
            }
        }
        return mask;
    }

    static boolean disjoint(long[] a, long[] b) {
        for (int i = 0; i < a.length; i++) {
            if ((a[i] & b[i]) != 0) return false;
        }
        return true;
    }

    static boolean solve(long[] used, int freeFaces) {
        if (freeFaces == 0) return true;
        // fill next the face with the fewest ways left
        int bestFace = -1;
        List<int[]> best = null;
        for (int f = 0; f < FACES; f++) {
            if ((freeFaces >> f & 1) == 0) continue;
            List<int[]> ways = new ArrayList<>();
            for (int p = 0; p < FACES; p++) {
                if (faceOf[p] != -1) continue;
                List<long[]> masks = options.get(p).get(f);
                for (int i = 0; i < masks.size(); i++) {
                    if (disjoint(masks.get(i), used)) ways.add(new int[] {p, i});
                }
            }
            if (ways.isEmpty()) return false;
            if (best == null || ways.size() < best.size()) {
                bestFace = f;
                best = ways;
            }
        }
        for (int[] way : best) {
            int p = way[0];
            faceOf[p] = bestFace;
            chosen[p] = options.get(p).get(bestFace).get(way[1]);
            long[] next = used.clone();
            for (int i = 0; i < next.length; i++) next[i] |= chosen[p][i];
            if (solve(next, freeFaces & ~(1 << bestFace))) return true;
            faceOf[p] = -1;
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> all = new ArrayList<>();
        String line;
        while ((line = in.readLine()) != null) {
            StringTokenizer tokens = new StringTokenizer(line);
            while (tokens.hasMoreTokens()) all.add(Integer.parseInt(tokens.nextToken()));
        }
        n = all.get(0);
        int at = 1;
        int[] volume = new int[FACES];
        for (int p = 0; p < FACES; p++) {
            parts[p] = new int[n][n];
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    parts[p][r][c] = all.get(at++);
                    volume[p] += parts[p][r][c];
                }
            }
        }
        for (int p = 0; p < FACES; p++) {
            options.add(new ArrayList<>());
            for (int f = 0; f < FACES; f++) {
                List<long[]> masks = new ArrayList<>();
                for (int t = 0; t < TURNS; t++) {
                    long[] m = placement(p, f, t);
                    boolean seen = false;
                    for (long[] o : masks) seen = seen || Arrays.equals(o, m);
                    if (!seen) masks.add(m);
                }
                options.get(p).add(masks);
            }
        }
        // a turn of the whole cube brings the largest part onto face 0 unturned
        int anchor = 0;
        for (int p = 1; p < FACES; p++) {
            if (volume[p] > volume[anchor]) anchor = p;
        }
        Arrays.fill(faceOf, -1);
        faceOf[anchor] = 0;
        chosen[anchor] = placement(anchor, 0, 0);
        if (!solve(chosen[anchor], ((1 << FACES) - 1) & ~1)) {
            System.out.println("No");
            return;
        }
        int[] label = new int[n * n * n];
        for (int p = 0; p < FACES; p++) {
            for (int i = 0; i < label.length; i++) {
                if ((chosen[p][i / WORD] >>> (i % WORD) & 1) == 1) label[i] = p + 1;
            }
        }
        StringBuilder out = new StringBuilder("Yes\n");
        for (int row = 0; row < n * n; row++) {
            for (int x = 0; x < n; x++) {
                if (x > 0) out.append(' ');
                out.append(label[row * n + x]);
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
