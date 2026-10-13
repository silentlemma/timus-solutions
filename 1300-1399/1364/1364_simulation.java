import java.util.Scanner;

public class Main {
    // east, south, west, north: turning right moves one step along this list
    static final int[] DR = {0, 1, 0, -1};
    static final int[] DC = {1, 0, -1, 0};

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        int rt = in.nextInt(), ct = in.nextInt(), rl = in.nextInt(), cl = in.nextInt();
        int t = in.nextInt();
        // dig the spiral up to the treasure, remembering the order of the graves,
        // with a frame of dug cells around the cemetery standing for the wall
        boolean[][] seen = new boolean[n + 2][m + 2];
        for (int r = 0; r < n + 2; r++)
            seen[r][0] = seen[r][m + 1] = true;
        for (int c = 0; c < m + 2; c++)
            seen[0][c] = seen[n + 1][c] = true;
        int[] pr = new int[n * m], pc = new int[n * m];
        int len = 1, r = 1, c = 1, d = 0;
        pr[0] = 1;
        pc[0] = 1;
        seen[1][1] = true;
        while (r != rt || c != ct) {
            if (seen[r + DR[d]][c + DC[d]]) {
                d = (d + 1) % DR.length;
                continue;
            }
            r += DR[d];
            c += DC[d];
            seen[r][c] = true;
            pr[len] = r;
            pc[len++] = c;
        }
        // Lara runs along the tunnel, at most t graves either way
        int here = 0;
        while (pr[here] != rl || pc[here] != cl)
            here++;
        int lo = Math.max(0, here - t), hi = Math.min(len - 1, here + t);
        StringBuilder out = new StringBuilder();
        for (int i = lo; i <= hi; i++)
            out.append(pr[i]).append(' ').append(pc[i]).append('\n');
        System.out.print(out);
    }
}
