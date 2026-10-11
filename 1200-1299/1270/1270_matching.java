import java.io.*;
import java.util.*;

public class Main {
    static final int FACES = 6;
    static final int COORDS = 3; // the cell's place does not matter

    // faces in the input order: front, up, right, down, left, back; a turn p
    // gives face f the colour of face p[f]; SPIN turns the cube about the
    // vertical axis, TIP about the left-right one
    static final int[] SPIN = {2, 1, 5, 3, 0, 4};
    static final int[] TIP = {1, 5, 2, 0, 4, 3};
    static List<List<Integer>> fits = new ArrayList<>();
    static int[] owner;
    static boolean[] seen;

    // all 24 rotations of a cube, from two quarter turns
    static List<int[]> rotations() {
        int[] start = new int[FACES];
        for (int f = 0; f < FACES; f++)
            start[f] = f;
        Set<String> found = new HashSet<>();
        found.add(Arrays.toString(start));
        List<int[]> queue = new ArrayList<>();
        queue.add(start);
        for (int k = 0; k < queue.size(); k++)
            for (int[] g : new int[][] {SPIN, TIP}) {
                int[] q = new int[FACES];
                for (int f = 0; f < FACES; f++)
                    q[f] = queue.get(k)[g[f]];
                if (found.add(Arrays.toString(q)))
                    queue.add(q);
            }
        return queue;
    }

    static boolean augment(int j) {
        for (int i : fits.get(j))
            if (!seen[i]) {
                seen[i] = true;
                if (owner[i] < 0 || augment(owner[i])) {
                    owner[i] = j;
                    return true;
                }
            }
        return false;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[][] cubes = new int[n][FACES];
        for (int[] cube : cubes)
            for (int f = 0; f < FACES; f++) {
                in.nextToken();
                cube[f] = (int)in.nval;
            }
        in.nextToken();
        int m = (int)in.nval;
        List<int[]> turns = rotations();
        // fits[j]: the cubes that can stand in cell j, turned somehow
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < COORDS; k++)
                in.nextToken();
            int[] need = new int[FACES];
            for (int f = 0; f < FACES; f++) {
                in.nextToken();
                need[f] = (int)in.nval;
            }
            List<Integer> list = new ArrayList<>();
            for (int i = 0; i < n; i++)
                for (int[] p : turns) {
                    boolean ok = true;
                    for (int f = 0; f < FACES && ok; f++)
                        ok = need[f] == 0 || need[f] == cubes[i][p[f]];
                    if (ok) {
                        list.add(i);
                        break;
                    }
                }
            fits.add(list);
        }
        // Kuhn's augmenting paths from every cell
        owner = new int[n];
        Arrays.fill(owner, -1);
        for (int j = 0; j < m; j++) {
            seen = new boolean[n];
            if (!augment(j)) {
                System.out.println(0);
                return;
            }
        }
        int[] cubeOf = new int[m];
        for (int i = 0; i < n; i++)
            if (owner[i] >= 0)
                cubeOf[owner[i]] = i + 1;
        StringBuilder out = new StringBuilder();
        for (int c : cubeOf)
            out.append(c).append("\n");
        System.out.print(out);
    }
}
