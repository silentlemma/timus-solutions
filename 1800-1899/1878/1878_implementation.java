import java.util.Scanner;

public class Main {
    static final int SIDE = 4;
    static final int TURNS = 4;
    static final int HALF = SIDE / 2;
    // position of each quadrant (top left, top right, bottom left, bottom
    // right) in the order a quarter turn moves a square through them
    static final int[][] RING = {{0, 1}, {TURNS - 1, 2}};

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] count = new int[TURNS];
        for (int r = 0; r < SIDE; r++) {
            for (int c = 0; c < SIDE; c++) {
                if (in.nextInt() == 1) {
                    count[RING[r / HALF][c / HALF]]++;
                }
            }
        }
        // every layer holds one square of each colour, one per quadrant; the
        // cube is solved when the colour 1 squares of all layers share a quadrant
        int best = SIDE * TURNS;
        for (int t = 0; t < TURNS; t++) {
            int moves = 0;
            for (int p = 0; p < TURNS; p++) {
                int d = (p - t + TURNS) % TURNS;
                moves += count[p] * Math.min(d, TURNS - d);
            }
            best = Math.min(best, moves);
        }
        System.out.println(best);
    }
}
