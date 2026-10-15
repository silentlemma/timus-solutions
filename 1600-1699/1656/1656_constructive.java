import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Integer[] heights = new Integer[n * n];
        for (int i = 0; i < n * n; i++)
            heights[i] = in.nextInt();
        Arrays.sort(heights, Collections.reverseOrder());
        int mid = n / 2;
        // cells by (nearer, farther) distance from the centre row and column:
        // along any row or column this grows outwards on each side
        List<int[]> cells = new ArrayList<>();
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++) {
                int a = Math.abs(r - mid), b = Math.abs(c - mid);
                cells.add(new int[] {Math.min(a, b), Math.max(a, b), r * n + c});
            }
        cells.sort(Comparator.<int[]>comparingInt(p -> p[0]).thenComparingInt(p -> p[1]));
        int[][] grid = new int[n][n];
        for (int k = 0; k < n * n; k++)
            grid[cells.get(k)[2] / n][cells.get(k)[2] % n] = heights[k];
        StringBuilder sb = new StringBuilder();
        for (int[] row : grid) {
            for (int c = 0; c < n; c++)
                sb.append(row[c]).append(c + 1 < n ? ' ' : '\n');
        }
        System.out.print(sb);
    }
}
