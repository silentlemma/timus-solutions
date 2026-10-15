import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final int WIN = 3;
    static final String[] SIGNS = {"<", "<=", ">=", ">"};

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] left = new int[n];
        for (int i = 0; i < n; i++) {
            left[i] = in.nextInt();
        }
        int[][] got = new int[n][n];
        List<Integer> active = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            active.add(i);
        }
        boolean ok = true;
        // the weakest team plays all its games now: it keeps its own points
        // and hands the rest out, three a game, to the strongest teams first
        while (ok && active.size() > 1) {
            active.sort((a, b) -> left[a] != left[b] ? left[a] - left[b] : a - b);
            int weak = active.get(0);
            int give = WIN * (active.size() - 1) - left[weak];
            if (give < 0) {
                break;
            }
            for (int k = active.size() - 1; k >= 1; k--) {
                int t = active.get(k), share = Math.min(WIN, give);
                give -= share;
                left[t] -= share;
                got[t][weak] = share;
                got[weak][t] = WIN - share;
                if (left[t] < 0) {
                    ok = false;
                }
            }
            left[weak] = 0;
            if (give != 0) {
                ok = false;
            }
            active.remove(0);
        }
        for (int x : left) {
            if (x != 0) {
                ok = false;
            }
        }
        if (!ok) {
            System.out.println("INCORRECT");
            return;
        }
        StringBuilder out = new StringBuilder("CORRECT\n");
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                out.append(i + 1).append(' ').append(SIGNS[got[i][j]]).append(' ').append(j + 1)
                        .append('\n');
            }
        }
        System.out.print(out);
    }
}
