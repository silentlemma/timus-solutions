import java.util.Scanner;

public class Main {
    // east, south, west, north: turning right moves one step along this list
    static final int[] DR = {0, 1, 0, -1};
    static final int[] DC = {1, 0, -1, 0};

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        int r1 = in.nextInt(), c1 = in.nextInt(), r2 = in.nextInt(), c2 = in.nextInt();
        // dig the whole spiral, numbering the graves by the night they are dug,
        // with a frame of dug cells around the cemetery standing for the wall
        int[][] night = new int[n + 2][m + 2];
        for (int r = 1; r <= n; r++)
            for (int c = 1; c <= m; c++)
                night[r][c] = -1;
        int r = 1, c = 1, d = 0;
        night[1][1] = 1;
        for (int day = 2; day <= n * m; day++) {
            while (night[r + DR[d]][c + DC[d]] >= 0)
                d = (d + 1) % DR.length;
            r += DR[d];
            c += DC[d];
            night[r][c] = day;
        }
        System.out.println(Math.abs(night[r1][c1] - night[r2][c2]));
    }
}
