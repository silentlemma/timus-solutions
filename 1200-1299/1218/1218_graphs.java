import java.util.Scanner;

public class Main {
    static final int PARAMS = 3, MAJORITY = 2;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String[] names = new String[n];
        int[][] stats = new int[n][PARAMS];
        for (int i = 0; i < n; i++) {
            names[i] = in.next();
            for (int p = 0; p < PARAMS; p++) {
                stats[i][p] = in.nextInt();
            }
        }
        // reach[i][j]: i beats j, directly or through a chain of wins
        boolean[][] reach = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int better = 0;
                for (int p = 0; p < PARAMS; p++) {
                    if (stats[i][p] > stats[j][p]) {
                        better++;
                    }
                }
                reach[i][j] = i != j && better >= MAJORITY;
            }
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                if (reach[i][k]) {
                    for (int j = 0; j < n; j++) {
                        reach[i][j] |= reach[k][j];
                    }
                }
            }
        }
        StringBuilder out = new StringBuilder();
        // a Jedi can win when every other one can be beaten along such a chain
        for (int i = 0; i < n; i++) {
            boolean all = true;
            for (int j = 0; j < n; j++) {
                all &= i == j || reach[i][j];
            }
            if (all) {
                out.append(names[i]).append('\n');
            }
        }
        System.out.print(out);
    }
}
