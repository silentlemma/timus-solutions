import java.util.Scanner;

public class Main {
    static int[] balance(String pile) {
        int[] d = new int[pile.length() + 1];
        for (int i = 0; i < pile.length(); i++)
            d[i + 1] = d[i] + (pile.charAt(i) == '1' ? 1 : -1);
        return d;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // after taking i cards of the first pile and j of the second, the red and
        // the black piles differ by d1[i] + d2[j], where d = 2 * reds - taken
        int[] d1 = balance(in.next()), d2 = balance(in.next());
        // reach[i][j]: the state is allowed and comes from (i - 1, j) or (i, j - 1)
        boolean[][] reach = new boolean[n + 1][n + 1];
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= n; j++) {
                if (Math.abs(d1[i] + d2[j]) > 1)
                    continue;
                reach[i][j] =
                    (i == 0 && j == 0) || (i > 0 && reach[i - 1][j]) || (j > 0 && reach[i][j - 1]);
            }
        if (!reach[n][n]) {
            System.out.println("Impossible");
            return;
        }
        // walk back from (n, n): a step left took a card of the second pile
        StringBuilder moves = new StringBuilder();
        for (int i = n, j = n; i > 0 || j > 0;) {
            if (j > 0 && reach[i][j - 1]) {
                moves.append('2');
                j--;
            } else {
                moves.append('1');
                i--;
            }
        }
        System.out.println(moves.reverse());
    }
}
