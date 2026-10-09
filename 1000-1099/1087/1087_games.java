import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        int[] moves = new int[m];
        for (int i = 0; i < m; i++) {
            moves[i] = in.nextInt();
        }
        // win[x]: the player to move with x stones left wins; with none left the
        // other player has just taken the last stone and lost
        boolean[] win = new boolean[n + 1];
        win[0] = true;
        for (int x = 1; x <= n; x++) {
            for (int k : moves) {
                if (k <= x && !win[x - k]) {
                    win[x] = true;
                }
            }
        }
        System.out.println(win[n] ? 1 : 2);
    }
}
