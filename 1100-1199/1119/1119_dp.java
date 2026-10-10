import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static final int SIDE = 100;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt(), k = in.nextInt();
        int[][] blocks = new int[k][];
        for (int i = 0; i < k; i++) {
            blocks[i] = new int[] {in.nextInt(), in.nextInt()};
        }
        Arrays.sort(blocks, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        // a route can use a chain of diagonal blocks increasing in both
        // coordinates; each one replaces two sides by one diagonal
        int[] chain = new int[k];
        int best = 0;
        for (int i = 0; i < k; i++) {
            chain[i] = 1;
            for (int j = 0; j < i; j++) {
                if (blocks[j][0] < blocks[i][0] && blocks[j][1] < blocks[i][1]) {
                    chain[i] = Math.max(chain[i], chain[j] + 1);
                }
            }
            best = Math.max(best, chain[i]);
        }
        double length = SIDE * (n + m - 2 * best) + SIDE * Math.sqrt(2) * best;
        System.out.println(Math.round(length));
    }
}
