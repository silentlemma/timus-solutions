import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        int[][] grid = new int[n][n];
        int number = 1;
        // diagonals by column minus row, from the top right corner down
        for (int shift = n - 1; shift > -n; shift--) {
            for (int row = Math.max(0, -shift); row < Math.min(n, n - shift); row++)
                grid[row][row + shift] = number++;
        }
        StringBuilder out = new StringBuilder();
        for (int[] line : grid) {
            for (int j = 0; j < n; j++)
                out.append(line[j]).append(j + 1 < n ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
