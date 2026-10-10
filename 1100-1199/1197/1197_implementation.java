import java.util.Scanner;

public class Main {
    static final int SIDE = 8;
    static final int[][] JUMPS = {{1, 2},   {2, 1},   {2, -1}, {1, -2},
                                  {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}};

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        StringBuilder out = new StringBuilder();
        for (int t = 0; t < n; t++) {
            String square = in.next();
            int col = square.charAt(0) - 'a', row = square.charAt(1) - '1', count = 0;
            // the knight attacks every square one jump away that is on the board
            for (int[] jump : JUMPS) {
                int c = col + jump[0], r = row + jump[1];
                if (c >= 0 && c < SIDE && r >= 0 && r < SIDE) {
                    count++;
                }
            }
            out.append(count).append('\n');
        }
        System.out.print(out);
    }
}
