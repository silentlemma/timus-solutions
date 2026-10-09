import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static int n;
    static boolean[][] a;
    static List<int[]> ops = new ArrayList<>();

    static void flip(int[] perm) {
        ops.add(perm.clone());
        for (int r = 0; r < n; r++) {
            a[r][perm[r]] = !a[r][perm[r]];
        }
    }

    static List<List<Integer>> parities() {
        List<Integer> rows = new ArrayList<>(), cols = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int row = 0, col = 0;
            for (int j = 0; j < n; j++) {
                row += a[i][j] ? 1 : 0;
                col += a[j][i] ? 1 : 0;
            }
            if (row % 2 == 1) {
                rows.add(i);
            }
            if (col % 2 == 1) {
                cols.add(i);
            }
        }
        List<List<Integer>> both = new ArrayList<>();
        both.add(rows);
        both.add(cols);
        return both;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = 2 * in.nextInt() + 1;
        a = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            String row = in.next();
            for (int j = 0; j < n; j++) {
                a[i][j] = row.charAt(j) == '+';
            }
        }
        // two transversals that differ in two rows flip the corners of a
        // rectangle, which keeps every row and column parity; one transversal
        // flips all the parities at once
        List<List<Integer>> p = parities();
        if (p.get(0).size() == n || p.get(1).size() == n) {
            int[] diagonal = new int[n];
            for (int i = 0; i < n; i++) {
                diagonal[i] = i;
            }
            flip(diagonal);
            p = parities();
        }
        List<Integer> rows = p.get(0), cols = p.get(1);
        // the target keeps the parities with max(|rows|, |cols|) plus signs,
        // and the unmatched lines come in pairs and share line 0
        boolean[][] t = new boolean[n][n];
        int paired = Math.min(rows.size(), cols.size());
        for (int k = 0; k < paired; k++) {
            t[rows.get(k)][cols.get(k)] = true;
        }
        for (int k = paired; k < rows.size(); k++) {
            t[rows.get(k)][0] = !t[rows.get(k)][0];
        }
        for (int k = paired; k < cols.size(); k++) {
            t[0][cols.get(k)] = !t[0][cols.get(k)];
        }
        int last = n - 1;
        for (int i = 0; i < last; i++) {
            for (int j = 0; j < last; j++) {
                if (a[i][j] == t[i][j]) {
                    continue;
                }
                int[] perm = new int[n];
                int next = 0;
                for (int r = 0; r < n; r++) {
                    if (r == i) {
                        perm[r] = j;
                    } else if (r == last) {
                        perm[r] = last;
                    } else {
                        while (next == j || next == last) {
                            next++;
                        }
                        perm[r] = next++;
                    }
                }
                flip(perm);
                perm[i] = last;
                perm[last] = j;
                flip(perm);
            }
        }
        StringBuilder out = new StringBuilder("There is solution:\n");
        for (int[] perm : ops) {
            for (int r = 0; r < n; r++) {
                out.append(perm[r] + 1).append(r + 1 < n ? " " : "\n");
            }
        }
        System.out.print(out);
    }
}
